## roblox ally bot made by outdateddev on github
# Spams ally bot to random group ids in roblox, can get you sales and members.
# This is a free script, you can modify it and sell it, but you must give credit to outdateddev on github.
# This script is not for malicious use, and is only for educational purposes.

import math
from pyexpat.errors import XML_ERROR_RECURSIVE_ENTITY_REF
import requests
import random
import time
import threading
import os
import sys
import json
import urllib.request
import urllib.parse
import urllib.error
import http.cookiejar
import re
import string
import math

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
        r = requests.get("https://www.roblox.com/home", cookies={".ROBLOSECURITY": cookie})
        csrfToken = r.headers["x-csrf-token"]
    except:
        print("Failed to login, check your cookie")
        sys.exit(0)
    
    print("Logged in successfully")


def spam():
    while True:
        try:
            id = random(10000000, 14000000)
            r = requests.post("https://groups.roblox.com/v1/groups/" + group + "relationships/allies" + id, headers={"x-csrf-token": csrfToken}, cookies={".ROBLOSECURITY": cookie})
            print("Sent ally request to " + id)
            time.sleep(delay)
        except:
            print("Failed to send ally request to " + id)
            time.sleep(delay)

def main():
    updatecsrf()
    for i in range(threads):
        threading.Thread(target=spam).start()

if __name__ == "__main__":
    main()
