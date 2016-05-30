import os
import sys
from multiprocessing import Pool


"""
THIS FILE WRITES THE INSTRUCTIONS FOR SETTING UP MULTIPLE
"""


SPRINGSPATH = "springs.py"
PEMPATH = "~/laptop.pem"
NO_STRICT_KEY = "-o 'StrictHostKeyChecking no'"


IP_DNS_LIST = [
                ('172.31.48.191', 'ec2-52-90-136-20.compute-1.amazonaws.com'), # node 0
                ('172.31.48.189', 'ec2-54-85-253-140.compute-1.amazonaws.com'),
                ('172.31.48.192', 'ec2-54-89-105-133.compute-1.amazonaws.com'),
                ('172.31.48.190', 'ec2-54-174-186-93.compute-1.amazonaws.com'),
                ('172.31.48.187', 'ec2-54-175-177-251.compute-1.amazonaws.com'),
                ('172.31.48.188', 'ec2-54-175-234-57.compute-1.amazonaws.com'),
            ]

def write_superbash():

    f = open('mpi_setup.sh','w')
    echo = ''
    for ip, dns in IP_DNS_LIST[1:]:
        echo += 'echo {} >> hosts \n'.format(ip)


    here = """#master node
sudo yum install mpich-devel
echo export PATH=/usr/lib64/mpich/bin/:$PATH >> .bashrc 
echo export LD_LIBRARY_PATH=/usr/lib64/mpich/lib/:$LD_LIBRARY_PATHPATH >> .bashrc 
source .bashrc 

{} 
sudo pip install numpy 
sudo pip install matplotlib
wget https://pypi.python.org/packages/source/m/mpi4py/mpi4pLSy-1.3.1.tar.gz 
tar xzf mpi4py-1.3.1.tar.gz 
cd mpi4py-1.3.1 
python setup.py build 
sudo python setup.py install 

echo 'done here'
    """.format(echo)

    f.write(here)

    for ip,dns in IP_DNS_LIST[1:]:
        echo = ''
        for ip2,dns2 in IP_DNS_LIST:
            if ip != ip2:
                echo += 'ssh -i {0} -o StrictHostKeyChecking=no ec2-user@{1} "echo {2} >> hosts" \n'.format(PEMPATH,dns,ip2)
        there ="""
# {1}

scp -i {0} -o StrictHostKeyChecking=no {0} ec2-user@{1}:~/.ssh/id_rsa
scp -i {0} -o StrictHostKeyChecking=no {3} ec2-user@{1}:~
ssh -i {0} -o StrictHostKeyChecking=no ec2-user@{1} "sudo easy_install pip" 
ssh -i {0} -o StrictHostKeyChecking=no ec2-user@{1} "sudo easy_install --upgrade pip" 
ssh -i {0} -o StrictHostKeyChecking=no ec2-user@{1} "sudo /usr/local/bin/pip install numpy" 
ssh -i {0} -o StrictHostKeyChecking=no ec2-user@{1} "sudo /usr/local/bin/pip install matplotlib" 
ssh -i {0} -o StrictHostKeyChecking=no ec2-user@{1} "sudo yum install mpich-devel"
ssh -i {0} -o StrictHostKeyChecking=no ec2-user@{1} "echo export PATH=/usr/lib64/mpich/bin/:$PATH >> .bashrc" 
ssh -i {0} -o StrictHostKeyChecking=no ec2-user@{1} "echo export LD_LIBRARY_PATH=/usr/lib64/mpich/lib/:$LD_LIBRARY_PATHPATH >> .bashrc" 
ssh -i {0} -o StrictHostKeyChecking=no ec2-user@{1} "source .bashrc" 

{2}
ssh -i {0} -o StrictHostKeyChecking=no ec2-user@{1} "wget https://pypi.python.org/packages/source/m/mpi4py/mpi4py-1.3.1.tar.gz" 
ssh -i {0} -o StrictHostKeyChecking=no ec2-user@{1} "tar xzf mpi4py-1.3.1.tar.gz" 
ssh -i {0} -o StrictHostKeyChecking=no ec2-user@{1} "cd mpi4py-1.3.1" 
ssh -i {0} -o StrictHostKeyChecking=no ec2-user@{1} "python setup.py build" 
ssh -i {0} -o StrictHostKeyChecking=no ec2-user@{1} "sudo python setup.py install " 
echo 'done {1}'
        """.format(PEMPATH,dns,echo,SPRINGSPATH)
        f.write(there)

    #cross ssh
    f.write("\necho 'cross ssh'\n")
    for ip,dns in IP_DNS_LIST:
        for ip2,dns2 in IP_DNS_LIST:
            if ip != ip2:
                s = '''ssh -t -i {0} -o StrictHostKeyChecking=no ec2-user@{1} "ssh {2}"\n'''.format(PEMPATH,dns,ip2)
                f.write(s)

    f.close()

if __name__ == '__main__':
    write_superbash()


