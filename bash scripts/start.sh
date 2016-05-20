scp -i csil.pem -r ../.git ec2-user@$1.amazonaws.com:~/123project
ssh -i csil.pem ec2-user@$1.amazonaws.com "sudo yum -y install git-all"
ssh -i csil.pem ec2-user@$1.amazonaws.com "cd ~/123project"
ssh -i csil.pem ec2-user@$1.amazonaws.com " git pull"

ssh -i csil.pem ec2-user@$1.amazonaws.com