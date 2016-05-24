import os

VECTORS = "supervectors.txt"
PEM = "~/laptop.pem"


def gen_places( n ):
    """
    breaks up vectors into n pieces
    stolen from lecture code
    """
    f = open(VECTORS,'r')

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
    ranges = gen_places(len(ip_list))

    for ip, start, stop in zip(ip_list, ranges):

        os.system('scp -i %s %s ec2-user@%s.amazonaws.com:~/ '%
                    [PEM, VECTORS, ip] )    # copy vectors 

        os.system('scp -i %s %s ec2-user@%s.amazonaws.com:~/ '%
                [PEM,"homogenous.py",ip])   # copy our function

        runner = "python homogenous.py %s %s"%(start,stop)

        os.system( 'ssh -i %s ec2-user@%s.amazonaws.com "%s" &'%
                    [PEM,ip, runner])       # run dykstra's algorithm




if __name__ == "__main__":

    go(sys.argv)