
dnslist=(
    ec2-52-90-70-187.compute-1.amazonaws.com
    ec2-52-91-27-78.compute-1.amazonaws.com
    ec2-52-201-224-209.compute-1.amazonaws.com
    ec2-54-152-84-87.compute-1.amazonaws.com
    ec2-54-152-87-92.compute-1.amazonaws.com
    ec2-54-174-156-166.compute-1.amazonaws.com
)

for dns in ${dnslist[*]};
do
scp -i $1 $2 ec2-user@$dns:$3
done