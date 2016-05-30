
echo "pempath" $1
echo "dns" $2
echo "springspath" $3

scp -i $1 -o StrictHostKeyChecking=no $1 ec2-user@$2:~/
scp -i $1 -o StrictHostKeyChecking=no $2 ec2-user@$2:~/.ssh/id_rsa
ssh -i $1 -o StrictHostKeyChecking=no ec2-user@$2
sudo yum install pip
sudo pip install --upgreade pip
sudo pip install mpi4py
sudo pip install numpy
