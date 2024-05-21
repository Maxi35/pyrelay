from Constants.StatTypes import StatTypes

class PlayerData:
    def __init__(self):
        self.name = ""
        self.level = 0
        self.xp = 0
        self.fame = 0
        self.stars = 0
        self.accountId = ""
        self.accountFame = 0
        self.gold = 0
        self.characterClass = 0
        self.nameChosen = False
        self.guildName = ""
        self.guildRank = 0
        self.maxHp = 0
        self.maxHpBoost = 0
        self.maxMp = 0
        self.maxMpBoost = 0
        self.hp = 0
        self.mp = 0
        self.atk = 0
        self.atkBoost = 0
        self.defense = 0
        self.defenseBoost = 0
        self.spd = 0
        self.spdBoost = 0
        self.dex = 0
        self.dexBoost = 0
        self.wis = 0
        self.wisBoost = 0
        self.vit = 0
        self.vitBoost = 0
        self.condition = []
        self.hasBackpack = False
        self.inv = [-1 for i in range(20)]
        self.size = 0
        self.nextLevelXp = 0
        self.clothingDye = 0
        self.accessoryDye = 0
        self.nextClassQuestFame = 0
        self.legendaryRank = 0
        self.xpBoosted = False
        self.xpBoostTime = 0
        self.texture = 0
        self.fortuneTokens = 0
        self.projSpeedMult = 1
        self.projLifeMult = 1
        self.opendAtTimestamp = 0
        self.exaltedHp = 0
        self.exaltedMp = 0
        self.exaltedAtk = 0
        self.exaltedDefense = 0
        self.exaltedSpd = 0
        self.exaltedDex = 0
        self.exaltedWis = 0
        self.exaltedVit = 0
        self.exaltationBonusDmg = 0
        self.exaltationICReduction = 0
        self.graveAccountId = -1
        self.potionOneType = -1
        self.potionTwoType = -1
        self.potionThreeType = -1
        self.potionBelt = 0
        self.forgeFire = 0
        self.characterClass = 0
        self.pos = None
        self.objectId = 0

    def parse(self, obj):
        self.characterClass = obj.objectType
        self.pos = obj.status.pos
        self.objectId = obj.status.objectId
        self.parseStats(obj.status.stats)

    def parseStats(self, stats):
        for stat in stats:
            if stat.statType == StatTypes.NAMESTAT:
                self.name = stat.strStatValue
            elif stat.statType == StatTypes.LEVELSTAT:
                self.level = stat.statValue
            elif stat.statType == StatTypes.EXPSTAT:
                self.xp = stat.statValue
            elif stat.statType == StatTypes.CURRFAMESTAT:
                self.fame = stat.statValue
            elif stat.statType == StatTypes.NUMSTARSSTAT:
                self.stars = stat.statValue
            elif stat.statType == StatTypes.ACCOUNTIDSTAT:
                self.accountId = stat.strStatValue
            elif stat.statType == StatTypes.FAMESTAT:
                self.accountFame = stat.statValue
            elif stat.statType == StatTypes.CREDITSSTAT:
                self.gold = stat.statValue
            elif stat.statType == StatTypes.MAXHPSTAT:
                self.maxHp = stat.statValue
            elif stat.statType == StatTypes.MAXMPSTAT:
                self.maxMp = stat.statValue
            elif stat.statType == StatTypes.HPSTAT:
                self.hp = stat.statValue
            elif stat.statType == StatTypes.MPSTAT:
                self.mp = stat.statValue
            elif stat.statType == StatTypes.ATTACKSTAT:
                self.atk = stat.statValue
            elif stat.statType == StatTypes.ATTACKBOOSTSTAT:
                self.atkBoost = stat.statValue
            elif stat.statType == StatTypes.DEFENSESTAT:
                self.defense = stat.statValue
            elif stat.statType == StatTypes.DEFENSEBOOSTSTAT:
                self.defenseBoost = stat.statValue
            elif stat.statType == StatTypes.SPEEDSTAT:
                self.spd = stat.statValue
            elif stat.statType == StatTypes.SPEEDBOOSTSTAT:
                self.spdBoost = stat.statValue
            elif stat.statType == StatTypes.DEXTERITYSTAT:
                self.dex = stat.statValue
            elif stat.statType == StatTypes.DEXTERITYBOOSTSTAT:
                self.dexBoost = stat.statValue
            elif stat.statType == StatTypes.VITALITYSTAT:
                self.vit = stat.statValue
            elif stat.statType == StatTypes.VITALITYBOOSTSTAT:
                self.vitBoost = stat.statValue
            elif stat.statType == StatTypes.CONDITIONSTAT:
                self.condition = stat.statValue
            elif stat.statType == StatTypes.WISDOMSTAT:
                self.wis = stat.statValue
            elif stat.statType == StatTypes.WISDOMBOOSTSTAT:
                self.wisBoost = stat.statValue
            elif stat.statType == StatTypes.HEALTHPOTIONSTACKSTAT:
                self.hpPots = stat.statValue
            elif stat.statType == StatTypes.MAGICPOTIONSTACKSTAT:
                self.mpPots = stat.statValue
            elif stat.statType == StatTypes.HASBACKPACKSTAT:
                self.hasBackpack = stat.statValue == 1
            elif stat.statType == StatTypes.NAMECHOSENSTAT:
                self.nameChosen = stat.statValue != 0
            elif stat.statType == StatTypes.GUILDNAMESTAT:
                self.guildName = stat.strStatValue
            elif stat.statType == StatTypes.GUILDRANKSTAT:
                self.guildRank = stat.statValue
            elif stat.statType == StatTypes.SIZESTAT:
                self.size = stat.statValue
            elif stat.statType == StatTypes.NEXTLEVELEXPSTAT:
                self.nextLevelXp = stat.statValue
            elif stat.statType == StatTypes.TEX1STAT:
                self.clothingDye = stat.statValue
            elif stat.statType == StatTypes.TEX2STAT:
                self.accessoryDye = stat.statValue
            elif stat.statType == StatTypes.MAXHPBOOSTSTAT:
                self.maxHpBoost = stat.statValue
            elif stat.statType == StatTypes.MAXMPBOOSTSTAT:
                self.maxMpBoost = stat.statValue
            elif stat.statType == StatTypes.NEXTCLASSQUESTFAMESTAT:
                self.nextClassQuestFame = stat.statValue
            elif stat.statType == StatTypes.LEGENDARYRANKSTAT:
                self.legendaryRank = stat.statValue
            elif stat.statType == StatTypes.XPBOOSTEDSTAT:
                self.xpBoosted = stat.statValue == 1
            elif stat.statType == StatTypes.XPTIMERSTAT:
                self.xpBoostTime = stat.statValue
            elif stat.statType == StatTypes.TEXTURESTAT:
                self.texture = stat.statValue
            elif stat.statType == StatTypes.FORTUNETOKENSTAT:
                self.fortuneTokens = stat.statValue
            elif stat.statType == StatTypes.PROJECTILESPEEDMULT:
                self.projSpeedMult = stat.statValue / 1000
            elif stat.statType == StatTypes.PROJECTILELIFEMULT:
                self.projLifeMult = stat.statValue / 1000
            elif StatTypes.INVENTORY0STAT <= stat.statType <= StatTypes.INVENTORY11STAT:
                self.inv[stat.statType-StatTypes.INVENTORY0STAT] = stat.statValue
            elif StatTypes.BACKPACK0STAT <= stat.statType <= StatTypes.BACKPACK7STAT:
                self.inv[stat.statType-StatTypes.BACKPACK0STAT+12] = stat.statValue
            elif stat.statType == StatTypes.OPENEDATTIMESTAMP:
                self.opendAtTimestamp = stat.statValue
            elif stat.statType == StatTypes.EXALTEDHP:
                self.exaltedHp = stat.statValue
            elif stat.statType == StatTypes.EXALTEDMP:
                self.exaltedMp = stat.statValue
            elif stat.statType == StatTypes.EXALTEDATK:
                self.exaltedAtk = stat.statValue
            elif stat.statType == StatTypes.EXALTEDDEFENSE:
                self.exaltedDefense = stat.statValue
            elif stat.statType == StatTypes.EXALTEDSPD:
                self.exaltedSpd = stat.statValue
            elif stat.statType == StatTypes.EXALTEDDEX:
                self.exaltedDex = stat.statValue
            elif stat.statType == StatTypes.EXALTEDWIS:
                self.exaltedWis = stat.statValue
            elif stat.statType == StatTypes.EXALTEDVIT:
                self.exaltedVit = stat.statValue
            elif stat.statType == StatTypes.EXALTATIONBONUSDMG:
                self.exaltationBonusDmg = stat.statValue/1000
            elif stat.statType == StatTypes.EXALTATIONICREDUCTION:
                self.exaltationICReduction = stat.statValue
            elif stat.statType == StatTypes.GRAVEACCOUNTID:
                self.graveAccountId = stat.statValue
            elif stat.statType == StatTypes.POTIONONETYPE:
                self.potionOneType = stat.statValue
            elif stat.statType == StatTypes.POTIONTWOTYPE:
                self.potionTwoType = stat.statValue
            elif stat.statType == StatTypes.POTIONTHREETYPE:
                self.potionThreeType = stat.statValue
            elif stat.statType == StatTypes.POTIONBELT:
                self.potionBelt = stat.statValue
            elif stat.statType == StatTypes.FORGEFIRE:
                self.forgeFire = stat.statValue
				
    def __str__(self):
        out = ""
        for key in self.__dict__:
            out += "{}: {}\n".format(key, self.__dict__[key])
        return out[:-1]
