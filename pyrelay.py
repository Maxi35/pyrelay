from ClientManager import ClientManager
from PluginManager import loadPlugins
from Client.Client import Client
from Helpers.Servers import update
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
parser.add_argument("-u", "--update", action="store_true", help="Checks for RotMG updates")
parser.add_argument("--force-update", action="store_true", help="Force update RotMG resources")

args = parser.parse_args()
if args.servers:
    update()
    print("Servers updated")
if args.update or args.force_update:
    print("Checking for updates...")
    if os.path.exists(VERSION_PATH) and not args.force_update:
        sVersion = int(open(VERSION_PATH).read())
        t = requests.get(api.VERSION)
        nVersion = int(t.text)
        if nVersion > sVersion:
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
input()
accounts = []
try:
    with open("Accounts.json", "r", encoding='utf-8') as file:
        accounts = json.load(file)
except IOError:
    print("Missing Accounts.json file")
    exit(1)

loadPlugins()
clientMan = ClientManager()

for account in accounts:
    thread = threading.Thread(target=clientMan.addClient, args=(account))
    thread.deamon = True
    thread.start()

try:
    while 1:
        clientMan.reconnectIfNeeded()
        time.sleep(0.5)
except (KeyboardInterrupt, SystemExit):
    clientMan.stop()






