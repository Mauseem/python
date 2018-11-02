import requests

import pdm_import_path

from pdm.base.context import PdmContext


class InstanceInfo(object):
    def __init__(self, host, port, version):
        self.host = host
        self.port = port
        self.version = version


def get_instance_info(host, port):
    tomcat_api = "http://%(host)s:%(port)s/sahibinden-web/rest/mgmt/packageInfo" % {"host": host, "port": port}
    request_data = requests.get(tomcat_api)
    return InstanceInfo(host, port, request_data.json()['data']['version'])


if __name__ == '__main__':
    """
    for i in range(1, 10, 1):
        host = ("isvc%02d" % i)
        info = get_instance_info(host, 20001)
        print("%(host)s %(port)s %(version)s" % info.__dict__)
"""

    args = {"project": "service"}

    ctx = PdmContext(MODE_PRODUCTION, RAW_CONFIGURATION, args)
    ctx.initializeLogging()
    ctx.initialize()

    # -----

    # WARNING: argument checking order is important

    # -----

    try:
        ctx.printToOut(ctx.loadCurrent().currentVersion)
    except Error as e:
        print("Ohh noo %s" % e)