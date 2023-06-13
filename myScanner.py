#!/bin/python3

import sys
import socket
from datetime import datetime

# define target

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translate hostname to ipv4
else:
    print("Invalid Arguments! Usage:: ./myScanner.py <ipv4>")


#banner
print("-" * 50)
print("Now Scanning", sys.argv[1], "...")
print("Scan Started at " + str(datetime.now()))

try:
    for port in range(50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting Program")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved")
    sys.exit()

except socket.error:
    print("Could not connect to the server")
    sys.exit()
