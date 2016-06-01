for dns in ${@};
do
ssh -i $1 -o StrictHostKeyChecking=no ec2-user@$dns $3
done