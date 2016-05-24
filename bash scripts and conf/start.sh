scp -i $2 -r ../../123project ec2-user@$1.amazonaws.com:~/123project
ssh -i $2 ec2-user@$1.amazonaws.com "sudo yum -y install git-all"
ssh -i $2 ec2-user@$1.amazonaws.com "cd ~/123project"
ssh -i $2 ec2-user@$1.amazonaws.com " git pull"

ssh -i $2 ec2-user@$1.amazonaws.com