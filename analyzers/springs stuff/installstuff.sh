
sudo yum update
sudo easy_install pip
sudo easy_install --upgrade pip
sudo yum install mpich-devel
echo export PATH=/usr/lib64/mpich/bin/:$PATH >> .bashrc
echo export LD_LIBRARY_PATH=/usr/lib64/mpich/lib/:$LD_LIBRARY_PATHPATH >> .bashrc
source .bashrc
sudo pip install numpy
wget https://pypi.python.org/packages/source/m/mpi4py/mpi4py-1.3.1.tar.gz
tar xzf mpi4py-1.3.1.tar.gz
cd mpi4py-1.3.1
python setup.py build
sudo python setup.py install


