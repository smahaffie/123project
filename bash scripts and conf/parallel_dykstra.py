import os
import sys

PEM = "~/laptop.pem"

PLACENAMEFILE = "placenames.txt"


def gen_places( n , file):
    """
    breaks up vectors into n pieces
    stolen from lecture code
    """
    f = open( file ,'r')

    f.seek(0,2) #go to end of file
    fsize = f.tell()
    ranges = []
    chunksize = fsize/n
    start = 0
    for i in range(n):
        f.seek(start + chunk_size)
        l = f.readline()
        end = min(start + chunk_size + len(l) - 1, fsize)
        ranges.append( (start, end) )
        start = end + 1
    return ranges

def go(ip_list):
    """
    generate and run commands for many aws instances
    to run homogenous.py in parallel
    """
    ranges = gen_places(len(ip_list), PLACENAMEFILE)

    for ip, r in zip(ip_list, ranges):

        start,stop = r

        files_to_copy = ("json_vectors.json","homogenous.py","placenames.txt")

        for ftc in files_to_copy:
            os.system('scp -i %s %s ec2-user@%s.amazonaws.com:~/ '%
                        [PEM, ftc, ip] )


        runner = ("python homogenous.py %s %s %s %s"%
                ("neighbors.json","json_vectors.json",start,stop))

        os.system( 'ssh -i %s ec2-user@%s.amazonaws.com "%s" &'%
                    [PEM,ip, runner])       # run dykstra's algorithm


def retrieve(ip_list):
    """
    copy outputs back to this computer
    """
    n = 0

    os.system("mkdir dykstra_ress")

    for ip in ip_list:
        os.system("scp -i %s %s:~/dykstra_res.txt /dykstra_ress"%
                    (PEM,ip)    )


