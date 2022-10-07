# roblox ally bot made by outdateddev on github
import string
import requests
from random import randint, choice
import time
import threading
import os
import sys
from discord import Webhook
import aiohttp

from dotenv import load_dotenv
load_dotenv()

# config
cookie = os.getenv('COOKIE')
group = os.getenv('GROUP')
allies = os.getenv('TYPE')
delay = os.getenv('DELAY')
threads = os.getenv('THREADS')
type = os.getenv('TYPE')
webhook = os.getenv('WEBHOOK')

if cookie == "":
    print("Please set .roblosecurity cookie in .env file (COOKIE)")
    sys.exit(0)
if group == "":
    print("Please set the Group ID in .env file (GROUP)")
    sys.exit(0)
if delay == None:
    print("Delay not set, defaulting to 5 seconds.")
    delay = 5
if webhook == "":
    print("Webhook not set, not sending webhook.")
if threads == None:
    print("Threads not set, defaulting to 1 thread")
    threads = 1
if type not in ['allies', 'enemies']:
    print("Type not set or invalid, defaulting to allies.")
    type = "allies"

def groupally():
    while True:
        try:
            randint(15900000, 16010000)
            cookies = {'.ROBLOSECURITY': cookie}

            gathtoken = requests.post(
                'https://auth.roblox.com/v2/logout', cookies=cookies)
            token = gathtoken.headers['x-csrf-token']

            headers = {'x-csrf-token': token}

            sendally = requests.post(
                f'https://groups.roblox.com/v1/groups/{group}/relationships/{allies}/{randomid}', headers=headers, cookies=cookies)

            if sendally.status_code == 200:
                print(f'Ally sent to {randomid} | ')
            elif sendally.status_code == 429:
                print('Rate limited')
            else:
                print(f'Failed to send {allies} request to {randomid}')
        except:
            print('Error')
        time.sleep(int(delay))

def main():
    print("""\

                ________          __ ________               
                \_____  \  __ ___/  |\______ \   _______  __
                 /   |   \|  |  \   __\    |  \_/ __ \  \/ /
                /    |    \  |  /|  | |    `   \  ___/\   / 
                \_______  /____/ |__|/_______  /\___  >\_/  
                        \/                   \/     \/     


                    """)
    print("""\

                  /$$$$$$  /$$ /$$                 /$$$$$$$              /$$    
                 /$$__  $$| $$| $$                | $$__  $$            | $$    
                | $$  \ $$| $$| $$ /$$   /$$      | $$  \ $$  /$$$$$$  /$$$$$$  
                | $$$$$$$$| $$| $$| $$  | $$      | $$$$$$$  /$$__  $$|_  $$_/  
                | $$__  $$| $$| $$| $$  | $$      | $$__  $$| $$  \ $$  | $$    
                | $$  | $$| $$| $$| $$  | $$      | $$  \ $$| $$  | $$  | $$ /$$
                | $$  | $$| $$| $$|  $$$$$$$      | $$$$$$$/|  $$$$$$/  |  $$$$/
                |__/  |__/|__/|__/ \____  $$      |_______/  \______/    \___/  
                                   /$$  | $$                                    
                                  |  $$$$$$/                                    
                                   \______/                                     


                    """)
    print(f"Starting {threads} threads")
    print()
    time.sleep(0.5)
    print(f"Delay: {delay}")
    print(f"Type: {type}")
    print(f"Group: {group}")
    time.sleep(1)
    print()
    for i in range(int(threads)):
        t = threading.Thread(target=groupally)
        t.start()

if __name__ == "__main__":
    main()