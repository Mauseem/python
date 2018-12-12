#!/bin/bash

# -----------------------------------------------------------------------------

# this script may be called from cron, so beware of PATH
PATH="$PATH:/usr/bin:/opt/sahibinden/system/bin"

# -----------------------------------------------------------------------------

base="/home/pdm/git_repos/farm_sync"
SYSTEM="$base/system"
TOOLS="$base/tools"
DATA="/opt/sahibinden/data"

# -----------------------------------------------------------------------------

usage() {
    cat <<EOF

USAGE: farm_sync.sh [--help|-h|-?] [--no-data] [--no-git] [--mail "<mailAddress>"] [IP ...]

When no ip provided, copies to default destinations.

When one or more IPs are provided, copies only to those IPs.

EOF
    exit 1
}

# -----------------------------------------------------------------------------

systemGroups="
    hg_activemq
    hg_admin
    hg_binden
    hg_cassandra
    hg_cassandra_cnt_rei
    hg_cron
    hg_elastic_search
    hg_elasticsearch_replicator
    hg_farm_sync
    hg_frontend
    hg_hadoop
    hg_hadoop
    hg_image_cleanup
    hg_image_proc
    hg_image_proc_py
    hg_image_store
    hg_iphone_proxy
    hg_kafka
    hg_kafka_temp
    hg_log
    hg_mail
    hg_memcache
    hg_mobile_site
    hg_mobile_site_staging
    hg_mongo
    hg_mongo_replicator
    hg_nativead
    hg_netscaler_weblogs
    hg_new_admin
    hg_projeler
    hg_redis
    hg_service
    hg_service_api
    hg_service_api_staging
    hg_service_staging
    hg_skp
    hg_slo_collector
    hg_static_assets
    hg_sys_util
    hg_sysadm
    hg_tensorflow_serving
    hg_varnish
    hg_zabbix
    hg_zookeeper
    hg_zookeeper_log
"

# -----

dataGroups="
    hg_binden
    hg_hadoop
    hg_log
    hg_mobile_site
    hg_nativead
    hg_service
    hg_service_api
    hg_service_staging
    hg_testbox_base
"

# -----------------------------------------------------------------------------

sortIps() {
    tr ' \t' '\n' | sort -u | sort -t . -k 1,1n -k 2,2n -k 3,3n -k 4,4n | grep -vE '^$'
}

farmList() {
    while [[ -n "$1" ]]
    do
        arg="$1"
        shift

        if [[ "$arg" =~ hg_.* ]]
        then
            if [[ "$arg" =~ .*staging.* ]]
            then
                inventory_list.sh --no-oos -sgh "$arg"
            else
                inventory_list.sh --no-oos -sgh "$arg"
            fi
        else
            echo "$arg"
        fi
    done \
    | grep -v --file <(inventory_list.sh -sgh hg_no_farm_sync) \
    | sortIps
}

# -----------------------------------------------------------------------------

checkRepoWritable() {
    local repo="$1"
    local git="$repo/.git"
    [[ -d "$git" && $(stat -c %U "$git") == $(id -un) ]]
}

gitPullQuiet() {
    local repo="$1"

    checkRepoWritable "$repo" || return

    local result="0"

    pushd "$repo" > /dev/null || err "Git repository '$repo' does not exist"

    git pull -q
    ret="$?"

    popd > /dev/null

    return "$ret"
}




gitPull() {
    local repo="$1"

    checkRepoWritable "$repo" || return

    local result="0"

    printf "%-20s  " "$(basename "$repo")"
    pushd "$repo" > /dev/null || err "Git repository '$repo' does not exist"

    if git pull -q
    then
        echo "  OK  "
    else
        echo "FAILED"
        result="1"
    fi
    popd > /dev/null

    return "$result"
}

unlockOpt() {
# make paths writable before local rsync
    sudo chattr -R -i /opt/sahibinden/system/ && sudo chattr -R -i /opt/sahibinden/tools/


}
rsyncLocal() {
    rsync -rltE \
        --delete --delete-excluded \
        --exclude=".git*"  \
        "$SYSTEM" "$TOOLS" \
        "/opt/sahibinden/" >&2              #for local batch sync
}
lockOpt() {
# lock paths for write after rsync;  even for root #
    sudo chattr -R +i /opt/sahibinden/system/  && sudo chattr -R +i /opt/sahibinden/tools/
}
gitPullAllRepos() {
    result="0"
    if [[ "$noGit" != "true" ]]
    then
        echo
        echo "Git Repo              Pull  "
        echo "--------------------  ------"
        gitPull "$SYSTEM" || result="1"
        gitPull "$TOOLS"  || result="1"

         unlockOpt && rsyncLocal  &&  lockOpt
#        gitPullQuiet "/opt/sahibinden/system"
#        gitPullQuiet "/opt/sahibinden/tools"

    fi

    return "$result"
}

# -----------------------------------------------------------------------------
sshCmd="ssh -o ConnectTimeout=5 -o LogLevel=error -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -o PasswordAuthentication=no"

syncSystem() {


    rsync -e "$sshCmd" --recursive --links --times \
        --delete --delete-excluded \
        --exclude="*~" --exclude=".git*" --exclude="private" \
        --executability \
        "$SYSTEM" "$TOOLS" \
        "root@$host:/opt/sahibinden/" >&2

    rsync -e "$sshCmd" --recursive --links --times \
        --delete --delete-excluded \
        --exclude="*~" --exclude=".git*" \
        --executability \
        "$DATA/zabbix" \
        "root@$host:/opt/sahibinden/data/" >&2
}

syncData() {
    local host="$1"
    rsync -e "$sshCmd" --recursive --links --times \
        --delete \
        --exclude="*~" \
        --executability \
        "$DATA" \
        "root@$host:/opt/sahibinden/" >&2


}

syncHost() {
    local ipList="$1"
    local host="$2"
    local syncFunc="$3"
    local force="$4"

    local result="0"

    echo -n "  "

    if [[ "$force" == "true" ]] || echo "$ipList" | grep -qE "^$host$"
    then
        if [[ "$syncFunc" == "syncData" && "$noData" == "true" ]]
        then
            echo -n "(skip)"
        else
            if "$syncFunc" "$host"
            then
                echo -n "  OK  "
            else
                echo -n "FAILED"
                result="1"
            fi
        fi
    else
        echo -n "      "
    fi

    return "$result"
}

syncAllHosts() {
    local systemIps="$(farmList $systemGroups)"
    local dataIps="$(farmList $dataGroups)"

    local errFile="/tmp/farm_sync.$$.err"

    [[ -z "$hosts" ]] && hosts="$(farmList $systemIps $dataIps)"

    # -----

    echo
    echo "Host             System  Data  "
    echo "---------------  ------  ------"

    result="0"

    for host in $hosts
    do
        printf "%-15s" "$host"

        local res="0"

        rm -f "$errFile"
        syncHost "$systemIps" "$host" "syncSystem" "$force"     2>> "$errFile" || res="1"
        syncHost "$dataIps"   "$host" "syncData"   "$forceData" 2>> "$errFile" || res="1"
        echo

        if [[ "$res" != "0" ]]
        then
            result="1"

            if [[ -s "$errFile" ]]
            then
                echo "-----"
                cat "$errFile"
                echo "-----"
            fi
        fi
    done

    return "$result"
}

# -----------------------------------------------------------------------------
sendMail() {
    local details="$1"

    if [[ -n "$mailTo" ]]
    then
        local mailSent="farm_sync.$(id -un).mailSent.$mailTo"

        find "/tmp/" -maxdepth 1 -type f -name "$mailSent" -mtime -1 | grep -q "mailSent" && return

        echo "Sending error mail to '$mailTo'"
        touch "/tmp/$mailSent"

        {
            cat <<EOF

Please check log file for details and ensure that farm_sync.sh runs without errors.

Details:

$(cat "$details")

EOF
        } | mail -s "Farm synchronization failed on $HOSTNAME ($(date "+%Y-%m-%d %H:%M"))" "$mailTo"
    fi
}
# -----------------------------------------------------------------------------

main() {
    echo -e "\n\nStarting Synchronizing Farms -- $(date '+%Y-%m-%d %H:%M:%S')\n"

    local failed="/tmp/farm_sync.$$.failed"
    local details="/tmp/farm_sync.$$.details"

    {
        gitPullAllRepos   || touch "$failed"
        syncAllHosts      || touch "$failed"
        copyFileForDfpJob || touch "$failed"
    } | tee "$details"

    if [[ -f "$failed" ]]
    then
        echo -e "\nWARNING: There are failures during farm synchronization\n"
        sendMail "$details"
    fi

    echo
}

cleanup() {
    find "/tmp" -maxdepth 1 -name "farm_sync.$$.*" 2> /dev/null | xargs rm -f
}

# -----------------------------------------------------------------------------
copyFileForDfpJob() {
    for host in $(inventory_list.sh -sgh hg_cron)
    do
        rsync -q "$SYSTEM/private/dfp/Sahibinden-a5c95df9c5e6.json" \
            "root@$host:/etc/sahibinden/private/" \
            || return 1
    done
}

# -----------------------------------------------------------------------------
parseOpts() {
    while [[ -n "$1" ]]
    do
        opt="$1"
        shift

        case "$opt" in
            --help|-h|-\?)  usage ;;
            --no-data)      noData=true ;;
            --no-git)       noGit=true ;;
            --force)        force=true ;;
            --force-data)   forceData=true ;;
            --mail)         mailTo="$1" ; shift ;;
            *)              hosts="$hosts $(farmList $opt)" ;;
        esac
    done
}

# -----------------------------------------------------------------------------
parseOpts "$@"
main
cleanup
#-----------------------------------------------------------------------------