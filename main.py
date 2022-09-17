## roblox ally bot made by outdateddev on github
# Spams ally bot to random group ids in roblox, can get you sales and members.
# This is a free script, you can modify it and sell it, but you must give credit to outdateddev on github.
# This script is not for malicious use, and is only for educational purposes.

from pyexpat.errors import XML_ERROR_RECURSIVE_ENTITY_REF
from turtle import update
import requests
import random
import time
import threading
import os
import sys

# 0import dotenv
from dotenv import load_dotenv
load_dotenv()

# Config from .env file
cookie = os.getenv('COOKIE')
group = os.getenv('GROUP')
delay = os.getenv('DELAY')
threads = os.getenv('THREADS')

if cookie == None:
    print("Please set COOKIE in .env file")
    sys.exit(0)
if group == None:
    print("Please set GROUP in .env file")
    sys.exit(0)
if delay == None:
    print("Please set DELAY in .env file")
    sys.exit(0)
if threads == None:
    print("Please set THREADS in .env file")
    sys.exit(0)

csrfToken = ""

# Log-in via cookie/x-csrf-token
def updatecsrf():
    global csrfToken
    try:
        csrfToken = requests.post('https://catalog.roblox.com/v1/catalog/items/details', cookies=cookie).headers["x-csrf-token"]
    except:
        print("Failed to update csrf token")
    
    print("Logged in successfully")



def groupally():
    while True:
        try:
            randomid = random.randint(10000000, 15000000)
            cookies = {'.ROBLOSECURITY': cookie}

            gathtoken = requests.post('https://auth.roblox.com/v2/logout', cookies=cookies)
            token = gathtoken.headers['x-csrf-token']

            headers = {'x-csrf-token': token}

            sendally = requests.post(f'https://groups.roblox.com/v1/groups/{group}/relationships/allies/{randomid}', headers=headers, cookies=cookies)

            if sendally.status_code == 200:
                print(f'Ally sent to {randomid}')
            elif sendally.status_code == 429:
                print('Rate limited')
            else:
                print(f'Failed to send ally to {randomid}')
        except:
            print("Failed to send ally")
        time.sleep(int(delay))

def main():
    for i in range(1):
        threading.Thread(target=groupally).start()

if __name__ == "__main__":
    main()
