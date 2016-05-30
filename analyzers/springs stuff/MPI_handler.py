import os
import sys
from multiprocessing import Pool

SPRINGSPATH = "springs.py"
PEMPATH = "~/laptop.pem"
NO_STRICT_KEY = "-o 'StrictHostKeyChecking no'"


BIG_OL_LIST = [
                ('172.31.58.163', 'ec2-54-85-163-133.compute-1.amazonaws.com'), # node 0
                ('172.31.57.70', 'ec2-54-84-232-149.compute-1.amazonaws.com'),
                ('172.31.57.69', 'ec2-54-85-171-19.compute-1.amazonaws.com'),
                ('172.31.57.68', 'ec2-54-86-44-218.compute-1.amazonaws.com'),
                ('172.31.57.67', 'ec2-54-172-189-241.compute-1.amazonaws.com'),
                ('172.31.57.71', 'ec2-54-174-149-115.compute-1.amazonaws.com'),
            ]

def write_superbash():

    f = open('mpi_setup.sh','w')
    echo = ''
    for ip, dns in BIG_OL_LIST[1:]:
        echo += 'echo {} >> hosts \n'.format(ip)


    here = """#master node
sudo yum install mpich-devel
echo export PATH=/usr/lib64/mpich/bin/:$PATH >> .bashrc 
echo export LD_LIBRARY_PATH=/usr/lib64/mpich/lib/:$LD_LIBRARY_PATHPATH >> .bashrc 
source .bashrc 

{} 
sudo pip install numpy 
wget https://pypi.python.org/packages/source/m/mpi4py/mpi4py-1.3.1.tar.gz 
tar xzf mpi4py-1.3.1.tar.gz 
cd mpi4py-1.3.1 
python setup.py build 
sudo python setup.py install 

echo 'done here'
    """.format(echo)

    f.write(here)

    for ip,dns in BIG_OL_LIST[1:]:
        echo = ''
        for ip2,dns2 in BIG_OL_LIST:
            if ip != ip2:
                echo += 'ssh -i {0} -o StrictHostKeyChecking=no ec2-user@{1} "echo {2} >> hosts" \n'.format(PEMPATH,dns,ip2)
        there ="""
# {1}

scp -i {0} -o StrictHostKeyChecking=no {0} ec2-user@{1}:~/.ssh/id_rsa
scp -i {0} -o StrictHostKeyChecking=no {3} ec2-user@{1}:~
ssh -i {0} -o StrictHostKeyChecking=no ec2-user@{1} "sudo easy_install pip" 
ssh -i {0} -o StrictHostKeyChecking=no ec2-user@{1} "sudo easy_install --upgrade pip" 
ssh -i {0} -o StrictHostKeyChecking=no ec2-user@{1} "sudo /usr/local/bin/pip install numpy" 
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
    for ip,dns in BIG_OL_LIST:
        for ip2,dns2 in BIG_OL_LIST:
            if ip != ip2:
                s = '''ssh -t -i {0} -o StrictHostKeyChecking=no ec2-user@{1} "ssh {2}"\n'''.format(PEMPATH,dns,ip2)
                f.write(s)

    f.close()

if __name__ == '__main__':
    write_superbash()


