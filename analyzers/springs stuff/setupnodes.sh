echo "need to copy over vectors, neighbors, allplacenames"

iplist=(
    172.31.48.191
)

dnslist=(
    ec2-52-90-136-20.compute-1.amazonaws.com

)

copyall.sh      ~/laptop.pem ${dnslist[*]} ~/laptop.pem     ~/.ssh/id_rsa 
copyall.sh      ~/laptop.pem ${dnslist[*]} ~/laptop.pem     ~
copyall.sh      ~/laptop.pem ${dnslist[*]} installstuff.sh  ~
commandall.sh   ~/laptop.pem ${dnslist[*]} "bash installstuff.sh"

for ip in iplist
do
    commandall ~/laptop.pem ${dnslist[*]} "echo ip >> hosts"
done

echo