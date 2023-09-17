import urllib.parse
import Constants.ApiPoints as ApiPoints

def getXML(accessToken, proxies={}):
    import requests
    return requests.post(ApiPoints.SERVERS, data={"accessToken": accessToken,
                                                  "game_net": "Unity", "play_platform": "Unity", "game_net_user_id": ""}, headers=ApiPoints.exaltHeaders, proxies=proxies).text

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

def update(accessToken, proxies={}):
    writeServers(parseServers(getXML(accessToken, proxies={})))
