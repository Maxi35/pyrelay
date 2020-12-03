from ClientManager import ClientManager
from PluginManager import loadPlugins
from Client.Client import Client
from Helpers.Servers import update
import Helpers.Equip as EquipParser
import Constants.ApiPoints as api
import json
import time
import threading
import argparse
import os
import requests

VERSION_PATH = "Resources/version.txt"
EQUIP_PATH = "Resources/equip.xml"

parser = argparse.ArgumentParser(description="pyrelay")

parser.add_argument("-s", "--servers", action="store_true", help="Update the server ips")
parser.add_argument("--no-update", action="store_true", help="Don't check for new a RotMG update")
parser.add_argument("--force-update", action="store_true", help="Force update RotMG resources")

args = parser.parse_args()
if args.servers:
    update()
    print("Servers updated")
if not args.no_update:
    print("Checking for updates...")
    if os.path.exists(VERSION_PATH) and not args.force_update:
        try:
            sVersion = int(open(VERSION_PATH).read())
        except ValueError:
            sVersion = 0
        t = requests.get(api.VERSION)
        nVersion = t.text
        if int(nVersion) > sVersion:
            print("Updating...")
            with open(VERSION_PATH, "w") as file:
                file.write(nVersion)
            t = requests.get(api.EQUIP)
            with open(EQUIP_PATH, "w") as file:
                file.write(t.text)
        else:
            print("Resources is up to date")
    else:
        print("Updating...")
        t = requests.get(api.VERSION)
        with open(VERSION_PATH, "w") as file:
            file.write(t.text)
        t = requests.get(api.EQUIP)
        with open(EQUIP_PATH, "w") as file:
            file.write(t.text)

accounts = []
try:
    with open("Accounts.json", "r", encoding='utf-8') as file:
        accounts = json.load(file)
except IOError:
    print("Missing Accounts.json file")
    exit(1)
    
if not os.path.exists(EQUIP_PATH):
    print("The file \"equip.xml\" does not exist, to create it run \"pyrelay.py --force-update\"")
    print()
    r = input("Continue anyway? Note shooting won't be possible: ")
    if "n" in r:
        exit(0)

loadPlugins()
clientMan = ClientManager()

account_threads = []

for account in accounts:
    thread = threading.Thread(target=clientMan.addClient, args=(account,))
    thread.deamon = True
    thread.start()
    account_threads.append(thread)

for thread in account_threads:
    thread.join()

if len(clientMan.clients) == 0:
    print("No clients connected exiting...")
    exit(0)

weapons = None

if os.path.exists(EQUIP_PATH):
    weapons = EquipParser.parseWeapons(EQUIP_PATH)
   
clientMan.weapons = weapons

try:
    while 1:
        if clientMan.reconnectIfNeeded():
            print("No clients are active - exiting")
            break
        time.sleep(0.5)
except (KeyboardInterrupt, SystemExit):
    clientMan.stop()

