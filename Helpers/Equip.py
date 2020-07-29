class Weapon:
    def __init__(self, obj):
        self.parse(obj)

    def parse(self, obj):
        self.name = obj.attrib["id"]
        self.itemId = int(obj.attrib["type"], 16)
        self.rof = float(obj.find("RateOfFire").text)
        numProj = obj.find("NumProjectiles")
        if not numProj is None:
            self.numProjectiles = int(numProj.text)
        else:
            self.numProjectiles = 1
        arcGap = obj.find("ArcGap")
        if not arcGap is None:
            self.arcGap = int(arcGap.text)
        else:
            self.arcGap = 11.25  
        self.projectile = Projectile(obj.find("Projectile"))
        

class Projectile:
    def __init__(self, proj):
        self.parse(proj)

    def parse(self, proj):
        self.speed = float(proj.find("Speed").text)
        self.lifetime = float(proj.find("LifetimeMS").text)
        dmg = proj.find("Damage")
        if not dmg is None:
            self.minDmg = int(proj.find("Damage").text)
            self.maxDmg = self.minDmg
        else:
            self.minDmg = int(proj.find("MinDamage").text)
            self.maxDmg = int(proj.find("MaxDamage").text)


from xml.etree import ElementTree

WEAPONIDS = [17, 8, 1, 24, 3, 2]

def parseWeapons(path):
    idToWeapon = {}
    tree = ElementTree.parse(path)
    root = tree.getroot()
    for obj in root:
        slotType = obj.find("SlotType")
        if not slotType is None:
            slotType = int(slotType.text)
            if slotType in WEAPONIDS:
                weapon = Weapon(obj)
                idToWeapon[weapon.itemId] = weapon
    return idToWeapon
