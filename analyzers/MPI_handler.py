import os
import sys
from multiprocessing import Pool

SPRINGSPATH = "springs.py"
PEMPATH = "~/laptop.pem"


BIG_OL_LIST = [ ('172.31.58.163', 'ec2-54-85-163-133.compute-1.amazonaws.com'),
                ('172.31.59.167', 'ec2-52-87-193-118.compute-1.amazonaws.com'),
                ('172.31.59.165', 'ec2-52-91-203-100.compute-1.amazonaws.com'),
                ('172.31.59.168', 'ec2-52-201-217-26.compute-1.amazonaws.com'),
                ('172.31.59.166', 'ec2-54-86-48-88.compute-1.amazonaws.com'),
                ('172.31.59.164', 'ec2-54-152-90-85.compute-1.amazonaws.com')]


def setup(dns,iplist):
    """
    copy relavent files to instances
    install stuff
    """
    os.system("scp -i %s %s ec2-user@%s:~/"%[PEMPATH,SPRINGSPATH,dns])
    os.system("ssh -i %s ec2-user@%s"%[PEMPATH, dns])
    os.system("""
        sudo yum install mpich-devel    \n
        echo export PATH=/usr/lib64/mpich/bin/:$PATH >> .bashrc\n
        echo export LD_LIBRARY_PATH=/usr/lib64/mpich/lib/:$LD_LIBRARY_PATHPATH >> .bashrc\n
        source .bashrc\n """)

    for ip in iplist:
        os.system('echo %s >> hosts'%ip)

    os.system("""
        sudo pip install numpy\n
        wget https://pypi.python.org/packages/source/m/mpi4py/mpi4py-1.3.1.tar.gz\n
        tar xzf mpi4py-1.3.1.tar.gz\n
        cd mpi4py-1.3.1\n
        python setup.py build\n
        sudo python setup.py install\n """)
    os.system("exit")
    os.system('scp  -i%s %s ec2-user@%s:~/.ssh/id_rsa'%[PEMPATH,PEMPATH, dns])

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

    os.system("mpiexec -f hosts -n %d python %s"%[len(BIG_OL_LIST), SPRINGSPATH])


if __name__ == '__main__':

    if len(sys.argv) > 1 and sys.argv[1] == 'go':
        print('go')
        go(BIG_OL_LIST)