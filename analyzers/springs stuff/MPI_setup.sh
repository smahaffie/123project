#master node
sudo yum install mpich-devel
echo export PATH=/usr/lib64/mpich/bin/:$PATH >> .bashrc 
echo export LD_LIBRARY_PATH=/usr/lib64/mpich/lib/:$LD_LIBRARY_PATHPATH >> .bashrc 
source .bashrc 

echo 172.31.57.70 >> hosts 
echo 172.31.57.69 >> hosts 
echo 172.31.57.68 >> hosts 
echo 172.31.57.67 >> hosts 
echo 172.31.57.71 >> hosts 
 
sudo pip install numpy 
wget https://pypi.python.org/packages/source/m/mpi4py/mpi4py-1.3.1.tar.gz 
tar xzf mpi4py-1.3.1.tar.gz 
cd mpi4py-1.3.1 
python setup.py build 
sudo python setup.py install 

echo 'done here'
    
# ec2-54-84-232-149.compute-1.amazonaws.com

scp -i ~/laptop.pem -o StrictHostKeyChecking=no ~/laptop.pem ec2-user@ec2-54-84-232-149.compute-1.amazonaws.com:~/.ssh/id_rsa
scp -i ~/laptop.pem -o StrictHostKeyChecking=no springs.py ec2-user@ec2-54-84-232-149.compute-1.amazonaws.com:~
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-84-232-149.compute-1.amazonaws.com "sudo easy_install pip" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-84-232-149.compute-1.amazonaws.com "sudo easy_install --upgrade pip" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-84-232-149.compute-1.amazonaws.com "sudo /usr/local/bin/pip install numpy" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-84-232-149.compute-1.amazonaws.com "sudo yum install mpich-devel"
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-84-232-149.compute-1.amazonaws.com "echo export PATH=/usr/lib64/mpich/bin/:$PATH >> .bashrc" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-84-232-149.compute-1.amazonaws.com "echo export LD_LIBRARY_PATH=/usr/lib64/mpich/lib/:$LD_LIBRARY_PATHPATH >> .bashrc" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-84-232-149.compute-1.amazonaws.com "source .bashrc" 

ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-84-232-149.compute-1.amazonaws.com "echo 172.31.58.163 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-84-232-149.compute-1.amazonaws.com "echo 172.31.57.69 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-84-232-149.compute-1.amazonaws.com "echo 172.31.57.68 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-84-232-149.compute-1.amazonaws.com "echo 172.31.57.67 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-84-232-149.compute-1.amazonaws.com "echo 172.31.57.71 >> hosts" 

ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-84-232-149.compute-1.amazonaws.com "wget https://pypi.python.org/packages/source/m/mpi4py/mpi4py-1.3.1.tar.gz" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-84-232-149.compute-1.amazonaws.com "tar xzf mpi4py-1.3.1.tar.gz" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-84-232-149.compute-1.amazonaws.com "cd mpi4py-1.3.1" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-84-232-149.compute-1.amazonaws.com "python setup.py build" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-84-232-149.compute-1.amazonaws.com "sudo python setup.py install " 
echo 'done ec2-54-84-232-149.compute-1.amazonaws.com'
        
# ec2-54-85-171-19.compute-1.amazonaws.com

scp -i ~/laptop.pem -o StrictHostKeyChecking=no ~/laptop.pem ec2-user@ec2-54-85-171-19.compute-1.amazonaws.com:~/.ssh/id_rsa
scp -i ~/laptop.pem -o StrictHostKeyChecking=no springs.py ec2-user@ec2-54-85-171-19.compute-1.amazonaws.com:~
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-171-19.compute-1.amazonaws.com "sudo easy_install pip" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-171-19.compute-1.amazonaws.com "sudo easy_install --upgrade pip" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-171-19.compute-1.amazonaws.com "sudo /usr/local/bin/pip install numpy" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-171-19.compute-1.amazonaws.com "sudo yum install mpich-devel"
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-171-19.compute-1.amazonaws.com "echo export PATH=/usr/lib64/mpich/bin/:$PATH >> .bashrc" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-171-19.compute-1.amazonaws.com "echo export LD_LIBRARY_PATH=/usr/lib64/mpich/lib/:$LD_LIBRARY_PATHPATH >> .bashrc" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-171-19.compute-1.amazonaws.com "source .bashrc" 

ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-171-19.compute-1.amazonaws.com "echo 172.31.58.163 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-171-19.compute-1.amazonaws.com "echo 172.31.57.70 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-171-19.compute-1.amazonaws.com "echo 172.31.57.68 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-171-19.compute-1.amazonaws.com "echo 172.31.57.67 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-171-19.compute-1.amazonaws.com "echo 172.31.57.71 >> hosts" 

ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-171-19.compute-1.amazonaws.com "wget https://pypi.python.org/packages/source/m/mpi4py/mpi4py-1.3.1.tar.gz" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-171-19.compute-1.amazonaws.com "tar xzf mpi4py-1.3.1.tar.gz" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-171-19.compute-1.amazonaws.com "cd mpi4py-1.3.1" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-171-19.compute-1.amazonaws.com "python setup.py build" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-171-19.compute-1.amazonaws.com "sudo python setup.py install " 
echo 'done ec2-54-85-171-19.compute-1.amazonaws.com'
        
# ec2-54-86-44-218.compute-1.amazonaws.com

scp -i ~/laptop.pem -o StrictHostKeyChecking=no ~/laptop.pem ec2-user@ec2-54-86-44-218.compute-1.amazonaws.com:~/.ssh/id_rsa
scp -i ~/laptop.pem -o StrictHostKeyChecking=no springs.py ec2-user@ec2-54-86-44-218.compute-1.amazonaws.com:~
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-86-44-218.compute-1.amazonaws.com "sudo easy_install pip" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-86-44-218.compute-1.amazonaws.com "sudo easy_install --upgrade pip" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-86-44-218.compute-1.amazonaws.com "sudo /usr/local/bin/pip install numpy" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-86-44-218.compute-1.amazonaws.com "sudo yum install mpich-devel"
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-86-44-218.compute-1.amazonaws.com "echo export PATH=/usr/lib64/mpich/bin/:$PATH >> .bashrc" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-86-44-218.compute-1.amazonaws.com "echo export LD_LIBRARY_PATH=/usr/lib64/mpich/lib/:$LD_LIBRARY_PATHPATH >> .bashrc" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-86-44-218.compute-1.amazonaws.com "source .bashrc" 

ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-86-44-218.compute-1.amazonaws.com "echo 172.31.58.163 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-86-44-218.compute-1.amazonaws.com "echo 172.31.57.70 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-86-44-218.compute-1.amazonaws.com "echo 172.31.57.69 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-86-44-218.compute-1.amazonaws.com "echo 172.31.57.67 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-86-44-218.compute-1.amazonaws.com "echo 172.31.57.71 >> hosts" 

ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-86-44-218.compute-1.amazonaws.com "wget https://pypi.python.org/packages/source/m/mpi4py/mpi4py-1.3.1.tar.gz" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-86-44-218.compute-1.amazonaws.com "tar xzf mpi4py-1.3.1.tar.gz" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-86-44-218.compute-1.amazonaws.com "cd mpi4py-1.3.1" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-86-44-218.compute-1.amazonaws.com "python setup.py build" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-86-44-218.compute-1.amazonaws.com "sudo python setup.py install " 
echo 'done ec2-54-86-44-218.compute-1.amazonaws.com'
        
# ec2-54-172-189-241.compute-1.amazonaws.com

scp -i ~/laptop.pem -o StrictHostKeyChecking=no ~/laptop.pem ec2-user@ec2-54-172-189-241.compute-1.amazonaws.com:~/.ssh/id_rsa
scp -i ~/laptop.pem -o StrictHostKeyChecking=no springs.py ec2-user@ec2-54-172-189-241.compute-1.amazonaws.com:~
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-172-189-241.compute-1.amazonaws.com "sudo easy_install pip" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-172-189-241.compute-1.amazonaws.com "sudo easy_install --upgrade pip" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-172-189-241.compute-1.amazonaws.com "sudo /usr/local/bin/pip install numpy" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-172-189-241.compute-1.amazonaws.com "sudo yum install mpich-devel"
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-172-189-241.compute-1.amazonaws.com "echo export PATH=/usr/lib64/mpich/bin/:$PATH >> .bashrc" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-172-189-241.compute-1.amazonaws.com "echo export LD_LIBRARY_PATH=/usr/lib64/mpich/lib/:$LD_LIBRARY_PATHPATH >> .bashrc" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-172-189-241.compute-1.amazonaws.com "source .bashrc" 

ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-172-189-241.compute-1.amazonaws.com "echo 172.31.58.163 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-172-189-241.compute-1.amazonaws.com "echo 172.31.57.70 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-172-189-241.compute-1.amazonaws.com "echo 172.31.57.69 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-172-189-241.compute-1.amazonaws.com "echo 172.31.57.68 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-172-189-241.compute-1.amazonaws.com "echo 172.31.57.71 >> hosts" 

ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-172-189-241.compute-1.amazonaws.com "wget https://pypi.python.org/packages/source/m/mpi4py/mpi4py-1.3.1.tar.gz" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-172-189-241.compute-1.amazonaws.com "tar xzf mpi4py-1.3.1.tar.gz" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-172-189-241.compute-1.amazonaws.com "cd mpi4py-1.3.1" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-172-189-241.compute-1.amazonaws.com "python setup.py build" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-172-189-241.compute-1.amazonaws.com "sudo python setup.py install " 
echo 'done ec2-54-172-189-241.compute-1.amazonaws.com'
        
# ec2-54-174-149-115.compute-1.amazonaws.com

scp -i ~/laptop.pem -o StrictHostKeyChecking=no ~/laptop.pem ec2-user@ec2-54-174-149-115.compute-1.amazonaws.com:~/.ssh/id_rsa
scp -i ~/laptop.pem -o StrictHostKeyChecking=no springs.py ec2-user@ec2-54-174-149-115.compute-1.amazonaws.com:~
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-149-115.compute-1.amazonaws.com "sudo easy_install pip" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-149-115.compute-1.amazonaws.com "sudo easy_install --upgrade pip" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-149-115.compute-1.amazonaws.com "sudo /usr/local/bin/pip install numpy" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-149-115.compute-1.amazonaws.com "sudo yum install mpich-devel"
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-149-115.compute-1.amazonaws.com "echo export PATH=/usr/lib64/mpich/bin/:$PATH >> .bashrc" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-149-115.compute-1.amazonaws.com "echo export LD_LIBRARY_PATH=/usr/lib64/mpich/lib/:$LD_LIBRARY_PATHPATH >> .bashrc" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-149-115.compute-1.amazonaws.com "source .bashrc" 

ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-149-115.compute-1.amazonaws.com "echo 172.31.58.163 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-149-115.compute-1.amazonaws.com "echo 172.31.57.70 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-149-115.compute-1.amazonaws.com "echo 172.31.57.69 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-149-115.compute-1.amazonaws.com "echo 172.31.57.68 >> hosts" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-149-115.compute-1.amazonaws.com "echo 172.31.57.67 >> hosts" 

ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-149-115.compute-1.amazonaws.com "wget https://pypi.python.org/packages/source/m/mpi4py/mpi4py-1.3.1.tar.gz" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-149-115.compute-1.amazonaws.com "tar xzf mpi4py-1.3.1.tar.gz" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-149-115.compute-1.amazonaws.com "cd mpi4py-1.3.1" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-149-115.compute-1.amazonaws.com "python setup.py build" 
ssh -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-149-115.compute-1.amazonaws.com "sudo python setup.py install " 
echo 'done ec2-54-174-149-115.compute-1.amazonaws.com'
        
echo 'cross ssh'
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-163-133.compute-1.amazonaws.com "ssh 172.31.57.70"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-163-133.compute-1.amazonaws.com "ssh 172.31.57.69"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-163-133.compute-1.amazonaws.com "ssh 172.31.57.68"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-163-133.compute-1.amazonaws.com "ssh 172.31.57.67"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-163-133.compute-1.amazonaws.com "ssh 172.31.57.71"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-84-232-149.compute-1.amazonaws.com "ssh 172.31.58.163"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-84-232-149.compute-1.amazonaws.com "ssh 172.31.57.69"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-84-232-149.compute-1.amazonaws.com "ssh 172.31.57.68"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-84-232-149.compute-1.amazonaws.com "ssh 172.31.57.67"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-84-232-149.compute-1.amazonaws.com "ssh 172.31.57.71"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-171-19.compute-1.amazonaws.com "ssh 172.31.58.163"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-171-19.compute-1.amazonaws.com "ssh 172.31.57.70"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-171-19.compute-1.amazonaws.com "ssh 172.31.57.68"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-171-19.compute-1.amazonaws.com "ssh 172.31.57.67"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-85-171-19.compute-1.amazonaws.com "ssh 172.31.57.71"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-86-44-218.compute-1.amazonaws.com "ssh 172.31.58.163"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-86-44-218.compute-1.amazonaws.com "ssh 172.31.57.70"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-86-44-218.compute-1.amazonaws.com "ssh 172.31.57.69"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-86-44-218.compute-1.amazonaws.com "ssh 172.31.57.67"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-86-44-218.compute-1.amazonaws.com "ssh 172.31.57.71"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-172-189-241.compute-1.amazonaws.com "ssh 172.31.58.163"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-172-189-241.compute-1.amazonaws.com "ssh 172.31.57.70"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-172-189-241.compute-1.amazonaws.com "ssh 172.31.57.69"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-172-189-241.compute-1.amazonaws.com "ssh 172.31.57.68"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-172-189-241.compute-1.amazonaws.com "ssh 172.31.57.71"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-149-115.compute-1.amazonaws.com "ssh 172.31.58.163"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-149-115.compute-1.amazonaws.com "ssh 172.31.57.70"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-149-115.compute-1.amazonaws.com "ssh 172.31.57.69"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-149-115.compute-1.amazonaws.com "ssh 172.31.57.68"
ssh -t -i ~/laptop.pem -o StrictHostKeyChecking=no ec2-user@ec2-54-174-149-115.compute-1.amazonaws.com "ssh 172.31.57.67"
