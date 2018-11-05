import os
import time


class ssh:
    def ssh_test(self,hostname):
        print("checking ssh connection...")
        min = 1
        max = 100
        succeed = False
        for x in range(min, max + 1):
            ret = os.system("ssh -tt -p 22 auak@%s " % hostname)
            if ret == 0:
                print ("ssh  succeeds in %s try on host [%s]" % (x, hostname))
                succeed = True
                break
            else:
                print (
                    "ssh failed on host [%s]. will retry 1 seconds later. [trying %s / %s]" % (hostname, x, max))
                time.sleep(1)
        if not succeed:
            print('ssh connection failure on host [%s]. try count : %s' % (hostname, max))




connection = ssh()

connection.ssh_test(raw_input("hostname giriniz"))

