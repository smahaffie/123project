#master node
sudo yum install mpich-devel
echo export PATH=/usr/lib64/mpich/bin/:$PATH >> .bashrc 
echo export LD_LIBRARY_PATH=/usr/lib64/mpich/lib/:$LD_LIBRARY_PATHPATH >> .bashrc 
source .bashrc 

echo 172.31.48.189 >> hosts 
echo 172.31.48.192 >> hosts 
echo 172.31.48.190 >> hosts 
echo 172.31.48.187 >> hosts 
echo 172.31.48.188 >> hosts 
 
sudo pip install numpy 
sudo pip install matplotlib
wget https://pypi.python.org/packages/source/m/mpi4py/mpi4pLSy-1.3.1.tar.gz 
tar xzf mpi4py-1.3.1.tar.gz 
cd mpi4py-1.3.1 
python setup.py build 
sudo python setup.py install 

echo 'done here'
    
# ec2-54-85-253-140.compute-1.amazonaws.com

scp -i ~/laptop.pem -o StrictHostKeyChecking=no ~/laptop.pem ec2-user@ec2-54-85-253-140.compute-1.amazonaws.com:~/.ssh/id_rsa
scp -i ~/laptop.pem -o StrictHostKeyChecking=no springs.py ec2-user@ec2-54-85-253-140.compute-1.amazonaws.com:~
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-253-140.compute-1.amazonaws.com "sudo easy_install pip" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-253-140.compute-1.amazonaws.com "sudo easy_install --upgrade pip" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-253-140.compute-1.amazonaws.com "sudo /usr/local/bin/pip install numpy" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-253-140.compute-1.amazonaws.com "sudo /usr/local/bin/pip install matplotlib" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-253-140.compute-1.amazonaws.com "sudo yum install mpich-devel"
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-253-140.compute-1.amazonaws.com "echo export PATH=/usr/lib64/mpich/bin/:$PATH >> .bashrc" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-253-140.compute-1.amazonaws.com "echo export LD_LIBRARY_PATH=/usr/lib64/mpich/lib/:$LD_LIBRARY_PATHPATH >> .bashrc" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-253-140.compute-1.amazonaws.com "source .bashrc" 

ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-253-140.compute-1.amazonaws.com "echo 172.31.48.191 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-253-140.compute-1.amazonaws.com "echo 172.31.48.192 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-253-140.compute-1.amazonaws.com "echo 172.31.48.190 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-253-140.compute-1.amazonaws.com "echo 172.31.48.187 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-253-140.compute-1.amazonaws.com "echo 172.31.48.188 >> hosts" 

ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-253-140.compute-1.amazonaws.com "wget https://pypi.python.org/packages/source/m/mpi4py/mpi4py-1.3.1.tar.gz" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-253-140.compute-1.amazonaws.com "tar xzf mpi4py-1.3.1.tar.gz" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-253-140.compute-1.amazonaws.com "cd mpi4py-1.3.1" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-253-140.compute-1.amazonaws.com "python setup.py build" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-253-140.compute-1.amazonaws.com "sudo python setup.py install " 
echo 'done ec2-54-85-253-140.compute-1.amazonaws.com'
        
# ec2-54-89-105-133.compute-1.amazonaws.com

scp -i ~/laptop.pem -o StrictHostKeyChecking=no ~/laptop.pem ec2-user@ec2-54-89-105-133.compute-1.amazonaws.com:~/.ssh/id_rsa
scp -i ~/laptop.pem -o StrictHostKeyChecking=no springs.py ec2-user@ec2-54-89-105-133.compute-1.amazonaws.com:~
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-89-105-133.compute-1.amazonaws.com "sudo easy_install pip" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-89-105-133.compute-1.amazonaws.com "sudo easy_install --upgrade pip" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-89-105-133.compute-1.amazonaws.com "sudo /usr/local/bin/pip install numpy" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-89-105-133.compute-1.amazonaws.com "sudo /usr/local/bin/pip install matplotlib" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-89-105-133.compute-1.amazonaws.com "sudo yum install mpich-devel"
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-89-105-133.compute-1.amazonaws.com "echo export PATH=/usr/lib64/mpich/bin/:$PATH >> .bashrc" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-89-105-133.compute-1.amazonaws.com "echo export LD_LIBRARY_PATH=/usr/lib64/mpich/lib/:$LD_LIBRARY_PATHPATH >> .bashrc" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-89-105-133.compute-1.amazonaws.com "source .bashrc" 

ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-89-105-133.compute-1.amazonaws.com "echo 172.31.48.191 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-89-105-133.compute-1.amazonaws.com "echo 172.31.48.189 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-89-105-133.compute-1.amazonaws.com "echo 172.31.48.190 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-89-105-133.compute-1.amazonaws.com "echo 172.31.48.187 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-89-105-133.compute-1.amazonaws.com "echo 172.31.48.188 >> hosts" 

ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-89-105-133.compute-1.amazonaws.com "wget https://pypi.python.org/packages/source/m/mpi4py/mpi4py-1.3.1.tar.gz" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-89-105-133.compute-1.amazonaws.com "tar xzf mpi4py-1.3.1.tar.gz" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-89-105-133.compute-1.amazonaws.com "cd mpi4py-1.3.1" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-89-105-133.compute-1.amazonaws.com "python setup.py build" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-89-105-133.compute-1.amazonaws.com "sudo python setup.py install " 
echo 'done ec2-54-89-105-133.compute-1.amazonaws.com'
        
# ec2-54-174-186-93.compute-1.amazonaws.com

scp -i ~/laptop.pem -o StrictHostKeyChecking=no ~/laptop.pem ec2-user@ec2-54-174-186-93.compute-1.amazonaws.com:~/.ssh/id_rsa
scp -i ~/laptop.pem -o StrictHostKeyChecking=no springs.py ec2-user@ec2-54-174-186-93.compute-1.amazonaws.com:~
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-186-93.compute-1.amazonaws.com "sudo easy_install pip" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-186-93.compute-1.amazonaws.com "sudo easy_install --upgrade pip" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-186-93.compute-1.amazonaws.com "sudo /usr/local/bin/pip install numpy" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-186-93.compute-1.amazonaws.com "sudo /usr/local/bin/pip install matplotlib" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-186-93.compute-1.amazonaws.com "sudo yum install mpich-devel"
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-186-93.compute-1.amazonaws.com "echo export PATH=/usr/lib64/mpich/bin/:$PATH >> .bashrc" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-186-93.compute-1.amazonaws.com "echo export LD_LIBRARY_PATH=/usr/lib64/mpich/lib/:$LD_LIBRARY_PATHPATH >> .bashrc" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-186-93.compute-1.amazonaws.com "source .bashrc" 

ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-186-93.compute-1.amazonaws.com "echo 172.31.48.191 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-186-93.compute-1.amazonaws.com "echo 172.31.48.189 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-186-93.compute-1.amazonaws.com "echo 172.31.48.192 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-186-93.compute-1.amazonaws.com "echo 172.31.48.187 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-186-93.compute-1.amazonaws.com "echo 172.31.48.188 >> hosts" 

ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-186-93.compute-1.amazonaws.com "wget https://pypi.python.org/packages/source/m/mpi4py/mpi4py-1.3.1.tar.gz" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-186-93.compute-1.amazonaws.com "tar xzf mpi4py-1.3.1.tar.gz" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-186-93.compute-1.amazonaws.com "cd mpi4py-1.3.1" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-186-93.compute-1.amazonaws.com "python setup.py build" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-186-93.compute-1.amazonaws.com "sudo python setup.py install " 
echo 'done ec2-54-174-186-93.compute-1.amazonaws.com'
        
# ec2-54-175-177-251.compute-1.amazonaws.com

scp -i ~/laptop.pem -o StrictHostKeyChecking=no ~/laptop.pem ec2-user@ec2-54-175-177-251.compute-1.amazonaws.com:~/.ssh/id_rsa
scp -i ~/laptop.pem -o StrictHostKeyChecking=no springs.py ec2-user@ec2-54-175-177-251.compute-1.amazonaws.com:~
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-177-251.compute-1.amazonaws.com "sudo easy_install pip" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-177-251.compute-1.amazonaws.com "sudo easy_install --upgrade pip" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-177-251.compute-1.amazonaws.com "sudo /usr/local/bin/pip install numpy" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-177-251.compute-1.amazonaws.com "sudo /usr/local/bin/pip install matplotlib" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-177-251.compute-1.amazonaws.com "sudo yum install mpich-devel"
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-177-251.compute-1.amazonaws.com "echo export PATH=/usr/lib64/mpich/bin/:$PATH >> .bashrc" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-177-251.compute-1.amazonaws.com "echo export LD_LIBRARY_PATH=/usr/lib64/mpich/lib/:$LD_LIBRARY_PATHPATH >> .bashrc" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-177-251.compute-1.amazonaws.com "source .bashrc" 

ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-177-251.compute-1.amazonaws.com "echo 172.31.48.191 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-177-251.compute-1.amazonaws.com "echo 172.31.48.189 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-177-251.compute-1.amazonaws.com "echo 172.31.48.192 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-177-251.compute-1.amazonaws.com "echo 172.31.48.190 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-177-251.compute-1.amazonaws.com "echo 172.31.48.188 >> hosts" 

ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-177-251.compute-1.amazonaws.com "wget https://pypi.python.org/packages/source/m/mpi4py/mpi4py-1.3.1.tar.gz" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-177-251.compute-1.amazonaws.com "tar xzf mpi4py-1.3.1.tar.gz" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-177-251.compute-1.amazonaws.com "cd mpi4py-1.3.1" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-177-251.compute-1.amazonaws.com "python setup.py build" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-177-251.compute-1.amazonaws.com "sudo python setup.py install " 
echo 'done ec2-54-175-177-251.compute-1.amazonaws.com'
        
# ec2-54-175-234-57.compute-1.amazonaws.com

scp -i ~/laptop.pem -o StrictHostKeyChecking=no ~/laptop.pem ec2-user@ec2-54-175-234-57.compute-1.amazonaws.com:~/.ssh/id_rsa
scp -i ~/laptop.pem -o StrictHostKeyChecking=no springs.py ec2-user@ec2-54-175-234-57.compute-1.amazonaws.com:~
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-234-57.compute-1.amazonaws.com "sudo easy_install pip" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-234-57.compute-1.amazonaws.com "sudo easy_install --upgrade pip" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-234-57.compute-1.amazonaws.com "sudo /usr/local/bin/pip install numpy" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-234-57.compute-1.amazonaws.com "sudo /usr/local/bin/pip install matplotlib" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-234-57.compute-1.amazonaws.com "sudo yum install mpich-devel"
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-234-57.compute-1.amazonaws.com "echo export PATH=/usr/lib64/mpich/bin/:$PATH >> .bashrc" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-234-57.compute-1.amazonaws.com "echo export LD_LIBRARY_PATH=/usr/lib64/mpich/lib/:$LD_LIBRARY_PATHPATH >> .bashrc" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-234-57.compute-1.amazonaws.com "source .bashrc" 

ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-234-57.compute-1.amazonaws.com "echo 172.31.48.191 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-234-57.compute-1.amazonaws.com "echo 172.31.48.189 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-234-57.compute-1.amazonaws.com "echo 172.31.48.192 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-234-57.compute-1.amazonaws.com "echo 172.31.48.190 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-234-57.compute-1.amazonaws.com "echo 172.31.48.187 >> hosts" 

ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-234-57.compute-1.amazonaws.com "wget https://pypi.python.org/packages/source/m/mpi4py/mpi4py-1.3.1.tar.gz" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-234-57.compute-1.amazonaws.com "tar xzf mpi4py-1.3.1.tar.gz" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-234-57.compute-1.amazonaws.com "cd mpi4py-1.3.1" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-234-57.compute-1.amazonaws.com "python setup.py build" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-234-57.compute-1.amazonaws.com "sudo python setup.py install " 
echo 'done ec2-54-175-234-57.compute-1.amazonaws.com'
        
echo 'cross ssh'
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-52-90-136-20.compute-1.amazonaws.com "ssh 172.31.48.189"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-52-90-136-20.compute-1.amazonaws.com "ssh 172.31.48.192"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-52-90-136-20.compute-1.amazonaws.com "ssh 172.31.48.190"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-52-90-136-20.compute-1.amazonaws.com "ssh 172.31.48.187"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-52-90-136-20.compute-1.amazonaws.com "ssh 172.31.48.188"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-253-140.compute-1.amazonaws.com "ssh 172.31.48.191"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-253-140.compute-1.amazonaws.com "ssh 172.31.48.192"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-253-140.compute-1.amazonaws.com "ssh 172.31.48.190"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-253-140.compute-1.amazonaws.com "ssh 172.31.48.187"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-253-140.compute-1.amazonaws.com "ssh 172.31.48.188"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-89-105-133.compute-1.amazonaws.com "ssh 172.31.48.191"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-89-105-133.compute-1.amazonaws.com "ssh 172.31.48.189"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-89-105-133.compute-1.amazonaws.com "ssh 172.31.48.190"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-89-105-133.compute-1.amazonaws.com "ssh 172.31.48.187"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-89-105-133.compute-1.amazonaws.com "ssh 172.31.48.188"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-186-93.compute-1.amazonaws.com "ssh 172.31.48.191"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-186-93.compute-1.amazonaws.com "ssh 172.31.48.189"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-186-93.compute-1.amazonaws.com "ssh 172.31.48.192"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-186-93.compute-1.amazonaws.com "ssh 172.31.48.187"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-186-93.compute-1.amazonaws.com "ssh 172.31.48.188"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-177-251.compute-1.amazonaws.com "ssh 172.31.48.191"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-177-251.compute-1.amazonaws.com "ssh 172.31.48.189"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-177-251.compute-1.amazonaws.com "ssh 172.31.48.192"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-177-251.compute-1.amazonaws.com "ssh 172.31.48.190"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-177-251.compute-1.amazonaws.com "ssh 172.31.48.188"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-234-57.compute-1.amazonaws.com "ssh 172.31.48.191"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-234-57.compute-1.amazonaws.com "ssh 172.31.48.189"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-234-57.compute-1.amazonaws.com "ssh 172.31.48.192"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-234-57.compute-1.amazonaws.com "ssh 172.31.48.190"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-175-234-57.compute-1.amazonaws.com "ssh 172.31.48.187"
