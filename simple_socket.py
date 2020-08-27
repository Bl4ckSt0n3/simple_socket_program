# import libraries
import socket
import sys

# define port number
port = 80

# get host name as an ip address
try:
    host_ip = socket.gethostbyname('wwww.github.com')

except socket.gaierror:
    print("there was an arror resolving the host !!!")
    sys.exit()

# create a socket object 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:
    # connect to host using ip address and port number
    try:
        sc
        print("socket created !")
        sc.connect((host_ip, port))
        print("The socket has successfully connection to github on port = {}".format(host_ip))
    
    except socket.error as er:
        print("{} error occured when create a socket ".format(er))





