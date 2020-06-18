
def getXML():
    import requests
    return requests.get("https://www.realmofthemadgod.com/char/list?guid=None").text

def parseServers(xml):
    from xml.etree import ElementTree
    nameToIp = {}
    ipToName = {}
    root = ElementTree.fromstring(xml)
    for tag in root.find("Servers").findall("Server"):
        name, ip = tag.find("Name").text, tag.find("DNS").text
        nameToIp[name] = ip
        ipToName[ip] = name
    return nameToIp, ipToName

def writeServers(servers):
    text = "\nnameToIp = {}\nipToName = {}".format(servers[0], servers[1])

    with open("Constants/Servers.py", "w") as file:
        file.write(text)
    
