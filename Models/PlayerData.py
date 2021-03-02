from Constants.StatTypes import StatTypes

types = StatTypes()

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
        self.defense = 0#Hmmmm
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

    def parse(self, obj):
        self.characterClass = obj.objectType
        self.parseStats(obj.status.stats)

    def parseStats(self, stats):
        for stat in stats:
            if stat.statType == types.NAMESTAT:
                self.name = stat.strStatValue
            elif stat.statType == types.LEVELSTAT:
                self.level = stat.statValue
            elif stat.statType == types.EXPSTAT:
                self.xp = stat.statValue
            elif stat.statType == types.CURRFAMESTAT:
                self.fame = stat.statValue
            elif stat.statType == types.NUMSTARSSTAT:
                self.stars = stat.statValue
            elif stat.statType == types.ACCOUNTIDSTAT:
                self.accountId = stat.strStatValue
            elif stat.statType == types.FAMESTAT:
                self.accountFame = stat.statValue
            elif stat.statType == types.CREDITSSTAT:
                self.gold = stat.statValue
            elif stat.statType == types.MAXHPSTAT:
                self.maxHp = stat.statValue
            elif stat.statType == types.MAXMPSTAT:
                self.maxMp = stat.statValue
            elif stat.statType == types.HPSTAT:
                self.hp = stat.statValue
            elif stat.statType == types.MPSTAT:
                self.mp = stat.statValue
            elif stat.statType == types.ATTACKSTAT:
                self.atk = stat.statValue
            elif stat.statType == types.ATTACKBOOSTSTAT:
                self.atkBoost = stat.statValue
            elif stat.statType == types.DEFENSESTAT:
                self.defense = stat.statValue
            elif stat.statType == types.DEFENSEBOOSTSTAT:
                self.defenseBoost = stat.statValue
            elif stat.statType == types.SPEEDSTAT:
                self.spd = stat.statValue
            elif stat.statType == types.SPEEDBOOSTSTAT:
                self.spdBoost = stat.statValue
            elif stat.statType == types.DEXTERITYSTAT:
                self.dex = stat.statValue
            elif stat.statType == types.DEXTERITYBOOSTSTAT:
                self.dexBoost = stat.statValue
            elif stat.statType == types.VITALITYSTAT:
                self.vit = stat.statValue
            elif stat.statType == types.VITALITYBOOSTSTAT:
                self.vitBoost = stat.statValue
            elif stat.statType == types.CONDITIONSTAT:
                self.condition = stat.statValue
            elif stat.statType == types.WISDOMSTAT:
                self.wis = stat.statValue
            elif stat.statType == types.WISDOMBOOSTSTAT:
                self.wisBoost = stat.statValue
            elif stat.statType == types.HEALTHPOTIONSTACKSTAT:
                self.hpPots = stat.statValue
            elif stat.statType == types.MAGICPOTIONSTACKSTAT:
                self.mpPots = stat.statValue
            elif stat.statType == types.HASBACKPACKSTAT:
                self.hasBackpack = stat.statValue == 1
            elif stat.statType == types.NAMECHOSENSTAT:
                self.nameChosen = stat.statValue != 0
            elif stat.statType == types.GUILDNAMESTAT:
                self.guildName = stat.strStatValue
            elif stat.statType == types.GUILDRANKSTAT:
                self.guildRank = stat.statValue
            elif stat.statType == types.SIZESTAT:
                self.size = stat.statValue
            elif stat.statType == types.NEXTLEVELEXPSTAT:
                self.nextLevelXp = stat.statValue
            elif stat.statType == types.TEX1STAT:
                self.clothingDye = stat.statValue
            elif stat.statType == types.TEX2STAT:
                self.accessoryDye = stat.statValue
            elif stat.statType == types.MAXHPBOOSTSTAT:
                self.maxHpBoost = stat.statValue
            elif stat.statType == types.MAXMPBOOSTSTAT:
                self.maxMpBoost = stat.statValue
            elif stat.statType == types.NEXTCLASSQUESTFAMESTAT:
                self.nextClassQuestFame = stat.statValue
            elif stat.statType == types.LEGENDARYRANKSTAT:
                self.legendaryRank = stat.statValue
            elif stat.statType == types.XPBOOSTEDSTAT:
                self.xpBoosted = stat.statValue == 1
            elif stat.statType == types.XPTIMERSTAT:
                self.xpBoostTime = stat.statValue
            elif stat.statType == types.TEXTURESTAT:
                self.texture = stat.statValue
            elif stat.statType == types.FORTUNETOKENSTAT:
                self.fortuneTokens = stat.statValue
            elif stat.statType == types.PROJECTILESPEEDMULT:
                self.projSpeedMult = stat.statValue / 1000
            elif stat.statType == types.PROJECTILELIFEMULT:
                self.projLifeMult = stat.statValue / 1000
            elif types.INVENTORY0STAT <= stat.statType <= types.INVENTORY11STAT:
                self.inv[stat.statType-8] = stat.statValue
            elif types.BACKPACK0STAT <= stat.statType <= types.BACKPACK7STAT:
                self.inv[stat.statType-59] = stat.statValue
            elif stat.statType == types.OPENEDATTIMESTAMP:
                self.opendAtTimestamp = stat.statValue
            elif stat.statType == types.EXALTEDHP:
                self.exaltedHp = stat.statValue
            elif stat.statType == types.EXALTEDMP:
                self.exaltedMp = stat.statValue
            elif stat.statType == types.EXALTEDATK:
                self.exaltedAtk = stat.statValue
            elif stat.statType == types.EXALTEDDEFENSE:
                self.exaltedDefense = stat.statValue
            elif stat.statType == types.EXALTEDSPD:
                self.exaltedSpd = stat.statValue
            elif stat.statType == types.EXALTEDDEX:
                self.exaltedDex = stat.statValue
            elif stat.statType == types.EXALTEDWIS:
                self.exaltedWis = stat.statValue
            elif stat.statType == types.EXALTEDVIT:
                self.exaltedVit = stat.statValue
            elif stat.statType == types.EXALTATIONBONUSDMG:
                self.exaltationBonusDmg = stat.statValue/1000
            elif stat.statType == types.EXALTATIONICREDUCTION:
                self.exaltationICReduction = stat.statValue
            elif stat.statType == types.GRAVEACCOUNTID:
                self.graveAccountId = stat.statValue
            elif stat.statType == types.POTIONONETYPE:
                self.potionOneType = stat.statValue
            elif stat.statType == types.POTIONTWOTYPE:
                self.potionTwoType = stat.statValue
            elif stat.statType == types.POTIONTHREETYPE:
                self.potionThreeType = stat.statValue
            elif stat.statType == types.POTIONBELT:
                self.potionBelt = stat.statValue
            elif stat.statType == types.FORGEFIRE:
                self.forgeFire = stat.statValue
				
    def __str__(self):
        out = ""
        for key in self.__dict__:
            out += "{}: {}\n".format(key, self.__dict__[key])
        return out[:-1]
