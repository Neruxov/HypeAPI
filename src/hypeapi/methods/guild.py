from ..util.uuid import *

class Guild:
    def __init__(self, api, data):
        self.api = api
        self.fulldata = data
        self.data =  self.fulldata['guild']

        

    def getID(self):
        return self.data['_id']

    def getName(self):
        return self.data['name']

    def getNameLower(self):
        return self.data['name_lower']

    def getCoins(self):
        return self.data['coins']

    def getCoinsEver(self):
        return self.data['coinsEver']

    def getTimeCreated(self):
        return self.data['created']

    def getMembers(self):
        return self.data['members']

    def getMember(self, name='', uuid=''):
        if not name:
            uuid = NameToUUID(name)

        for member in self.getMembers():
            if member['uuid'] == uuid:
                return self.api.player(uuid=uuid)

    def getRanks(self):
        return self.data['ranks']

    def getExperienceKings(self):
        return self.data['achievements']['EXPERIENCE_KINGS']

    def getWinners(self):
        return self.data['achievements']['WINNERS']

    def getOnlinePlayers(self):
        return self.data['achievements']['ONLINE_PLAYERS']

    def getEXP(self):
        return self.data['exp']

    def getPreferredGames(self):
        return self.data['preferredGames']

    def isPublic(self):
        return self.data['publiclyListed']

    def getTag(self):
        return self.data['tag']

    def getTagColor(self):
        return self.data['tagColor']

    def getDescription(self):
        return self.data['description']

    def getQuakecraftEXP(self):
        return self.data['guildExpByGameType']['QUAKECRAFT']

    def getSurvivalGamesEXP(self):
        return self.data['guildExpByGameType']['SURVIVAL_GAMES']

    def getBuildBattleEXP(self):
        return self.data['guildExpByGameType']['BUILDBATTLE']

    def getSMPEXP(self):
        return self.data['guildExpByGameType']['SMP']

    def getGingerbreadEXP(self):
        return self.data['guildExpByGameType']['GINGERBREAD']

    def getArcadeEXP(self):
        return self.data['guildExpByGameType']['ARCADE']

    def getArenaEXP(self):
        return self.data['guildExpByGameType']['ARENA']

    def getSkyblockEXP(self):
        return self.data['guildExpByGameType']['SKYBLOCK']

    def getLegacyEXP(self):
        return self.data['guildExpByGameType']['LEGACY']

    def getHousingEXP(self):
        return self.data['guildExpByGameType']['HOUSING']

    def getPrototypeEXP(self):
        return self.data['guildExpByGameType']['PROTOTYPE']

    def getReplayEXP(self):
        return self.data['guildExpByGameType']['REPLAY']

    def getPitEXP(self):
        return self.data['guildExpByGameType']['PIT']

    def getSuperSmashEXP(self):
        return self.data['guildExpByGameType']['SUPER_SMASH']

    def getDuelsEXP(self):
        return self.data['guildExpByGameType']['DUELS']

    def getWalls3EXP(self):
        return self.data['guildExpByGameType']['WALLS3']

    def getSpeedUHCEXP(self):
        return self.data['guildExpByGameType']['SPEED_UHC']

    def getTNTGamesEXP(self):
        return self.data['guildExpByGameType']['TNTGAMES']

    def getWallsEXP(self):
        return self.data['guildExpByGameType']['WALLS']

    def getPaintballEXP(self):
        return self.data['guildExpByGameType']['PAINTBALL']

    def getMCGOEXP(self):
        return self.data['guildExpByGameType']['MCGO']

    def getSkyWarsEXP(self):
        return self.data['guildExpByGameType']['SKYWARS']

    def getUHCEXP(self):
        return self.data['guildExpByGameType']['UHC']

    def getVampireZEXP(self):
        return self.data['guildExpByGameType']['VAMPIREZ']

    def getBedWarsEXP(self):
        return self.data['guildExpByGameType']['BEDWARS']

    def getBattleGroundEXP(self):
        return self.data['guildExpByGameType']['BATTLEGROUND']

    def getMurderMysteryEXP(self):
        return self.data['guildExpByGameType']['MURDER_MYSTERY']