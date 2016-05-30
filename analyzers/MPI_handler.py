import os
import sys
from multiprocessing import Pool

SPRINGSPATH = "springs.py"
PEMPATH = "~/laptop.pem"


BIG_OL_LIST = [
                ('172.31.58.163', 'ec2-54-85-163-133.compute-1.amazonaws.com'), # node 0
                ('172.31.57.70', 'ec2-54-84-232-149.compute-1.amazonaws.com'),
                ('172.31.57.69', 'ec2-54-85-171-19.compute-1.amazonaws.com'),
                ('172.31.57.68', 'ec2-54-86-44-218.compute-1.amazonaws.com'),
                ('172.31.57.67', 'ec2-54-172-189-241.compute-1.amazonaws.com'),
                ('172.31.57.71', 'ec2-54-174-149-115.compute-1.amazonaws.com'),
            ]

def setup(dns,iplist):
    """
    copy relavent files to instances
    install stuff
    """
    os.system("scp -i %s %s ec2-user@%s:~/"%[PEMPATH,SPRINGSPATH,dns])
    os.system('scp  -i%s %s ec2-user@%s:~/.ssh/id_rsa'%[PEMPATH,PEMPATH, dns])
    os.system("ssh -i %s ec2-user@%s"%[PEMPATH, dns])
    os.system("sudo yum install pip")
    os.system("sudo pip install --upgrade pip")
    os.system("sudo pip install mpi4py")
    os.system("sudo pip install numpy")

    for ip in iplist:
        os.system('echo %s >> hosts'%ip)

    os.system("exit")


def cross_ssh(ip, dns):
    """
    ssh between different instances so they can cross communicate
    """
    os.system("ssh -i %s ec2-user@%s"%[PEMPATH, dns]) 
    os.system('ssh -i %s -o %s '%[ip, PEMPATH,"'StrictHostKeyChecking no'"])
    os.system("exit")
    os.system("exit")

BIG_OL_LIST = []

def go(BIG_OL_LIST):
    """
    run setup and cross ssh into each instance
    assuming
    """
    for ip, dns in BIG_OL_LIST:
        otherips = []
        for ip2,dns2 in BIG_OL_LIST:
            if ip != ip2:
                otherips.append(ip2)
        setup(dns,otherips)
        for ip2 in otherips:
            cross_ssh(ip2,dns)
    print('Done')

    os.system("mpiexec -f hosts -n {} python {}".format(len(BIG_OL_LIST), SPRINGSPATH))

if __name__ == '__main__':

    if len(sys.argv) > 1 and sys.argv[1] == 'go':
        print('go')
        go(BIG_OL_LIST)