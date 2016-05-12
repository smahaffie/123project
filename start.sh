scp -i csil.pem -r ../123project ec2-user@$1.amazonaws.com:~/123project


ssh -i csil.pem ec2-user@$1.amazonaws.com