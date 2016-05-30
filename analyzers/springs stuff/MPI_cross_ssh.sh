
echo "pempath" $1
echo "dns" $2
echo "ip" $3

ssh -i $1 -o StrictHostKeyChecking=no ec2-user@$2
ssh -i $3 -o StrictHostKeyChecking=no
exit
exit