#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time


class ssh:
    def ssh_test(self, port,hostname,username):
        print("checking ssh connection...")
        min = 1
        max = 100
        succeed = False
        for x in range(min, max + 1):
            ret = os.system("ssh -tt -p %s  %s -l %s   ")
            if ret == 0:
                print ("ssh  succeeds in %s try on host [%s]" % (x, hostname))
                succeed = True
                break
            else:

                    "ssh failed on host [%s]. will retry 1 seconds later. [trying %s / %s]" % (hostname, x, max))
                time.sleep(1)
        if not succeed:
            print('ssh connection failure on host [%s]. try count : %s' % (hostname, max))



connection = ssh()

connection.ssh_test(22,"dovpn.vm64.info", "aak")

