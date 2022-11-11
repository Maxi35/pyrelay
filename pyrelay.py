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

args = parser.parse_args()
accounts = []
try:
    with open("Accounts.json", "r", encoding="utf-8") as file:
        accounts = json.load(file)
except IOError:
    print("Missing Accounts.json file")
    exit(1)

loadPlugins()
clientMan = ClientManager()

if args.servers:
    clientMan.updateServers = True

account_threads = []

for account in accounts:
    thread = threading.Thread(target=clientMan.addClient, args=(account,))
    thread.daemon = True
    thread.start()
    account_threads.append(thread)

for thread in account_threads:
    thread.join()

if len(clientMan.clients) == 0:
    print("No clients connected exiting...")
    exit(0)

try:
    while 1:
        if clientMan.reconnectIfNeeded():
            print("No clients are active - exiting")
            break
        time.sleep(0.5)
except (KeyboardInterrupt, SystemExit):
    clientMan.stop()

