iplist=(
    172.31.56.21
    172.31.56.26
    172.31.56.22
    172.31.56.24
    172.31.56.25
    172.31.56.23
)

dnslist=(
    ec2-52-90-70-187.compute-1.amazonaws.com
    ec2-52-91-27-78.compute-1.amazonaws.com
    ec2-52-201-224-209.compute-1.amazonaws.com
    ec2-54-152-84-87.compute-1.amazonaws.com
    ec2-54-152-87-92.compute-1.amazonaws.com
    ec2-54-174-156-166.compute-1.amazonaws.com
)

bash copyall.sh      ~/laptop.pem  springs.py       ~
bash copyall.sh      ~/laptop.pem  ~/laptop.pem     ~/.ssh/id_rsa 
bash copyall.sh      ~/laptop.pem  ~/laptop.pem     ~
bash copyall.sh      ~/laptop.pem  installstuff.sh  ~
bash commandall.sh   ~/laptop.pem "bash installstuff.sh"

for ip in iplist
do
    bash commandall ~/laptop.pem "echo ip >> hosts"
done

echo