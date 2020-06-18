from Constants.StatTypes import StatTypes

types = StatTypes()

class PlayerData:
    def __init__(self):
        self.name = ""
        self.level = -1
        self.xp = -1
        self.fame = -1
        self.stars = -1
        self.accountId = ""
        self.accountFame = -1
        self.gold = -1
        self.characterClass = -1
        self.nameChosen = False
        self.guildName = ""
        self.guildRank = -1
        self.maxHp = -1
        self.maxHpBoost = -1
        self.maxMp = -1
        self.maxMpBoost = -1
        self.hp = -1
        self.mp = -1
        self.atk = -1
        self.atkBoost = -1
        self.defense = -1#Hmmmm
        self.defenseBoost = -1
        self.spd = -1
        self.spdBoost = -1
        self.dex = -1
        self.dexBoost = -1
        self.wis = -1
        self.wisBoost = -1
        self.vit = -1
        self.vitBoost = -1
        self.hasBackpack = False
        self.inv = [-1 for i in range(20)]
        self.size = -1
        self.nextLevelXp = -1
        self.clothingDye = -1
        self.accessoryDye = -1
        self.nextClassQuestFame = -1
        self.legendaryRank = -1
        self.xpBoosted = False
        self.xpBoostTime = -1
        self.texture = -1
        self.fortuneTokens = -1
        self.projSpeedMult = -1
        self.projLifeMule = -1

    def parse(self, obj):
        self.characterClass = obj.objectType
        for stat in obj.status.stats:
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
                self.maxHP = stat.statValue
            elif stat.statType == types.MAXMPSTAT:
                self.maxMP = stat.statValue
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
                self.maxHPBoost = stat.statValue
            elif stat.statType == types.MAXMPBOOSTSTAT:
                self.maxMPBoost = stat.statValue
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
            elif types.INVENTORY11STAT <= stat.statType <= types.INVENTORY0STAT:
                self.inv[stat.statType-8] = stat.statValue
            elif types.BACKPACK7STAT <= stat.statType <= types.BACKPACK0STAT:
                self.inv[stat.statType-59] = stat.statValue
                
    def __str__(self):
        return "name: {}\nlevel: {}\nxp: {}\nfame: {}\nstars: {}\naccountId: {}\naccountFame: {}\ngold: {}\ncharacterClass: {}\nnameChosen: {}\nguildName: {}\nguildRank: {}\nmaxHp: {}\nmaxHpBoost: {}\nmaxMp: {}\nmaxMpBoost: {}\nhp: {}\nmp: {}\natk: {}\natkBoost: {}\ndefense: {}\ndefenseBoost: {}\nspd: {}\nspdBoost: {}\ndex: {}\ndexBoost: {}\nwis: {}\nwisBoost: {}\nvit: {}\nvitBoost: {}\nhasBackpack: {}\ninv: {}\nsize: {}\nnextLevelXp: {}\nclothingDye: {}\naccessoryDye: {}\nnextClassQuestFame: {}\nlegendaryRank: {}\nxpBoosted: {}\nxpBoostTime: {}\ntexture: {}\nfortuneTokens: {}\nprojSpeedMult: {}\nprojLifeMule: {}".format(self.name, \
        self.level, \
        self.xp, \
        self.fame, \
        self.stars, \
        self.accountId, \
        self.accountFame, \
        self.gold, \
        self.characterClass, \
        self.nameChosen, \
        self.guildName, \
        self.guildRank, \
        self.maxHp, \
        self.maxHpBoost, \
        self.maxMp, \
        self.maxMpBoost, \
        self.hp, \
        self.mp, \
        self.atk, \
        self.atkBoost, \
        self.defense, \
        self.defenseBoost, \
        self.spd, \
        self.spdBoost, \
        self.dex, \
        self.dexBoost, \
        self.wis, \
        self.wisBoost, \
        self.vit, \
        self.vitBoost, \
        self.hasBackpack, \
        self.inv, \
        self.size, \
        self.nextLevelXp, \
        self.clothingDye, \
        self.accessoryDye, \
        self.nextClassQuestFame, \
        self.legendaryRank, \
        self.xpBoosted, \
        self.xpBoostTime, \
        self.texture, \
        self.fortuneTokens, \
        self.projSpeedMult, \
        self.projLifeMule)
            
