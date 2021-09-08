import urllib.parse
import Constants.ApiPoints as ApiPoints

def getXML(accessToken):
    import requests
    return requests.get("https://www.realmofthemadgod.com/account/servers?accessToken={}&game_net=Unity&play_playform=Unity&game_net_user_id=".format(urllib.parse.quote_plus(accessToken)), headers=ApiPoints.exaltHeaders).text

def parseServers(xml):
    from xml.etree import ElementTree
    nameToIp = {}
    ipToName = {}
    root = ElementTree.fromstring(xml)
    for tag in root.findall("Server"):
        name, ip = tag.find("Name").text, tag.find("DNS").text
        nameToIp[name] = ip
        ipToName[ip] = name
    return nameToIp, ipToName

def writeServers(servers):
    text = "\nnameToIp = {}\nipToName = {}".format(servers[0], servers[1])

    with open("Constants/Servers.py", "w") as file:
        file.write(text)

def update(accessToken):
    writeServers(parseServers(getXML(accessToken)))
