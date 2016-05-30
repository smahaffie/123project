for dns in ${@};
do
scp -i $1 $3 ec2-user@$dns:$4
done