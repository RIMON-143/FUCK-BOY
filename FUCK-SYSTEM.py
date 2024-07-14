import threading
from queue import Queue
import requests
import random
import string
import json
import hashlib
from faker import Faker
import os
os.system('clear')
logo = (f"""\033[1;32m
   88""Yb 88 8b    d8  dP"Yb  88b 88 
   88__dP 88 88b  d88 dP   Yb 88Yb88 
   88"Yb  88 88YbdP88 Yb   dP 88 Y88 
   88  Yb 88 88 YY 88  YbodP  88  Y8 
\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
\33[1;91m[\33[1;97m=\33[1;91m] \33[1;92mFACEBOOK  \x1b[1;97m : \33[1;92m MD RIMON            
\33[1;91m[\33[1;97m=\33[1;91m] \33[1;92mGITHUB    \x1b[1;97m : \33[1;92m RIMON-143      
\33[1;91m[\33[1;97m=\33[1;91m] \33[1;92mTOOLTYPE  \x1b[1;97m : \33[1;92m AUTO CREAT
\x1b[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
def linex():
        print(f"\033[1;97m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

def generate_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(length))

def get_mail_domains(proxy=None):
    url = "https://api.mail.tm/domains"
    try:
        response = requests.get(url, proxies=proxy)
        if response.status_code == 200:
            return response.json()['hydra:member']
        else:
            print(f'[×] E-mail Error : {response.text}')
            return None
    except Exception as e:
        print(f'[×] Error : {e}')
        return None

def create_mail_tm_account(proxy=None):
    fake = Faker()
    mail_domains = get_mail_domains(proxy)
    if mail_domains:
        domain = random.choice(mail_domains)['domain']
        username = generate_random_string(10)
        password = fake.password()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=45)
        first_name = fake.first_name()
        last_name = fake.last_name()
        url = "https://api.mail.tm/accounts"
        headers = {"Content-Type": "application/json"}
        data = {"address": f"{username}@{domain}", "password":password}       
        try:
            response = requests.post(url, headers=headers, json=data, proxies=proxy)
            if response.status_code == 201:
                return f"{username}@{domain}", password, first_name, last_name, birthday
            else:
                print(f'[×] Email Error : {response.text}')
                return None, None, None, None, None
        except Exception as e:
            print(f'[×] Error : {e}')
            return None, None, None, None, None

def register_facebook_account(email, password, first_name, last_name, birthday, proxy=None):
    api_key = '882a8490361da98702bf97a021ddc14d'
    secret = '62f8ce9f74b12f84c123cc23437a4a32'
    gender = random.choice(['M', 'F'])
    req = {'api_key': api_key,'attempt_login': True,'birthday': birthday.strftime('%Y-%m-%d'),'client_country_code': 'EN','fb_api_caller_class': 'com.facebook.registration.protocol.RegisterAccountMethod','fb_api_req_friendly_name': 'registerAccount','firstname': first_name,'format': 'json','gender': gender,'lastname': last_name,'email': email,'locale': 'en_US','method': 'user.register','password': password,'reg_instance': generate_random_string(32),'return_multiple_errors': True}
    sorted_req = sorted(req.items(), key=lambda x: x[0])
    sig = ''.join(f'{k}={v}' for k, v in sorted_req)
    ensig = hashlib.md5((sig + secret).encode()).hexdigest()
    req['sig'] = ensig
    api_url = 'https://b-api.facebook.com/method/user.register'
    reg = _call(api_url, req, proxy)
    id = reg['new_user_id']
    token = reg['session_info']['access_token']
    os.system('clear')
    print(logo)
    print(f'''
\x1b[1;97m━━━━━━━━━━\x1b[1;93mCREAT ID━━━━━━━━━━'
\33[1;91m[\33[1;97m=\33[1;91m] \33[1;92mEMAIL    \33[1;37m: \33[1;32m{email}
\33[1;91m[\33[1;97m=\33[1;91m] \33[1;92mUID      \33[1;37m: \33[1;32m{id}
\33[1;91m[\33[1;97m=\33[1;91m] \33[1;92mPASSWORD \33[1;37m: \33[1;32m{password}
\33[1;91m[\33[1;97m=\33[1;91m] \33[1;92mID NAME  \33[1;37m: \33[1;32m{first_name} {last_name}
\33[1;91m[\33[1;97m=\33[1;91m] \33[1;92mBIRTHDAY \33[1;37m: \33[1;32m{birthday} 
\33[1;91m[\33[1;97m=\33[1;91m] \33[1;92mGENDER   \33[1;37m: \33[1;32m{gender}
\x1b[1;97m━━━━━━━━━━\x1b[1;93mTOKEN━━━━━━━━━━ 
\33[1;91m[\33[1;97m=\33[1;91m] \33[1;92mTOKEN \33[1;37m: \33[1;35m{token}
\x1b[1;97m━━━━━━━━━━\x1b[1;93mCREAT ID━━━━━━━━━━''')
    open('username.txt', 'a')

def _call(url, params, proxy=None, post=True):
    headers = {'User-Agent': '[FBAN/FB4A;FBAV/35.0.0.48.273;FBDM/{density=1.33125,width=800,height=1205};FBLC/en_US;FBCR/;FBPN/com.facebook.katana;FBDV/Nexus 7;FBSV/4.1.1;FBBK/0;]'}
    if post:
        response = requests.post(url, data=params, headers=headers, proxies=proxy)
    else:
        response = requests.get(url, params=params, headers=headers, proxies=proxy)
    return response.json()

def test_proxy(proxy, q, valid_proxies):
    if test_proxy_helper(proxy):
        valid_proxies.append(proxy)
    q.task_done()

def test_proxy_helper(proxy):
    try:
        response = requests.get('https://api.mail.tm', proxies=proxy, timeout=5)
        print(f'Pass: {proxy}')
        return response.status_code == 200
    except:
        print(f'Fail: {proxy}')
        return False

def load_proxies():
    with open('proxies.txt', 'r') as file:
        proxies = [line.strip() for line in file]
    return [{'http': f'http://{proxy}'} for proxy in proxies]

def get_working_proxies():
    proxies = load_proxies()
    valid_proxies = []
    q = Queue()
    for proxy in proxies:
        q.put(proxy)
    
    for _ in range(10):  
        worker = threading.Thread(target=worker_test_proxy, args=(q, valid_proxies))
        worker.daemon = True
        worker.start()
    
    q.join()  
    return valid_proxies

def worker_test_proxy(q, valid_proxies):
    while True:
        proxy = q.get()
        if proxy is None:
            break
        test_proxy(proxy, q, valid_proxies)

working_proxies = get_working_proxies()

if not working_proxies:
    print('[×] No working proxies found. Please check your proxies.')
else:
    for i in range(int(input('\33[1;91m[\33[1;97m=\33[1;91m] \33[1;92mHow Many Accounts You Want \33[1;37m: \33[1;32m '))):
        proxy = random.choice(working_proxies)
        email, password, first_name, last_name, birthday = create_mail_tm_account(proxy)
        if email and password and first_name and last_name and birthday:
            register_facebook_account(email, password, first_name, last_name, birthday, proxy)

print(f'\33[1;91m[\33[1;97m✓\33[1;91m]\x1b[38;5;46m PRESS ENTER TO BACK ')
