import requests
import json
import random 
import threading
import sys
import os
import colorama
from colorama import Fore, init
sys.tracebacklimit = 0
os.system("title adv roblox gen")

def gen():
  try:
    id = random.randint(11900000,13100000)
    data=requests.get(f"https://users.roblox.com/v1/users/{id}",data={'excludeBannedUsers': True}).json()
    username=data["name"]
    lastonline = requests.get(f'https://api.roblox.com/users/{id}/onlinestatus').json() ['LastOnline'].split('-')[0]
    if (int(lastonline) == 2010):
      if (len(username) == 20):
        print(f"{Fore.BLUE} {username}:l0l0l0l:{lastonline}""")
        open('usernames.txt', 'a').write(f"{username}\n")
        open('login.txt', 'a').write(f"{username}:l0l0l0l\n")
        open('lastonlinelogin.txt', 'a').write(f"{username}:l0l0l0l:{lastonline}\n")
  except KeyError:
    pass

x = 0;
while (x < 1):
  if threading.active_count() <= int("500"):
    threading.Thread(target=gen).start()
