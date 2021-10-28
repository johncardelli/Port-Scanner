import sys
import socket 
from datetime import datetime

#Target
if len(sys.argv) ==2:
    target = socket.gethostbyname(sys.argv[1]) #Translate to ipv4

else 

    print("Invalid")
    print("Syntax: python scanner")

#Banner 

print("-" * 50)
print("Scanning Target "+target)
print("Time Started: "+str(datetime.now()))
print("-" * 50)

try:
    for port in range(50,65535):
        s = socket.socker(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #returns error
        if result == 0:
            print("Port {} is open".format(port))
        s.close()


except KeyboardInterrupt:
    print("\nExiting Program.")
    sys.exit()

except socket.gaierror:
    print("Hostname couldn't be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't Connect to Server.")
    sys.exit()