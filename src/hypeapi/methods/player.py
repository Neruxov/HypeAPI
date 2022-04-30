import math

from .games.skywars import *
from .games.bedwars import *
from .games.murdermystery import *
from .games.buildbuttle import *
from .games.skyblock_player import *
from .games.duels import *
from .games.tntgames import *
from .games.UHC import *
from ..util.api_requests import *


class Player:
    def __init__(self, api, data):

        self.api = api
        self.data = data['player']
        self.name = self.data['playername']
        self.uuid = self.data['uuid']
        self.fulldata = data

        self.setVariabes()

    def setVariabes(self):
        self.id = self.getID
        self.displayname = self.getDisplayName
        self.firstLogin = self.getFirstLogin
        self.knownAliases = self.getKnownAliases
        self.knownAliasesLower = self.getKnownAliasesLower
        self.lastLogin = self.getLastLogin
        self.playerName = self.getPlayerName
        self.achievementsOneTime = self.getAchievementsOneTime
        self.userLanguage = self.getUserLanguage
        self.networkExp = self.getNetworkExp
        self.networkLevel = self.getNetworkLevel
        self.karma = self.getKarma
        self.mcVersion = self.getMcVersion
        self.hypixelForums = self.getHypixelForums
        self.discord = self.getDiscord
        self.twitter = self.getTwitter
        self.youtube = self.getYoutube
        self.rank = self.getRank
        self.rankColor = self.getRankColor
        self.monthlyPlusColor = self.getMonthlyRankColor
        self.monthlyPackageRank = self.getMonthlyPackageRank
        self.mostRecentMonthlyPackageRank = self.getMostRecentMonthlyPackageRank

        self.skywars = SkyWars(self)
        self.bedwars = BedWars(self)
        self.murdermystery = MurderMystery(self)
        self.buildbattle = BuildBattle(self)
        self.skyblock = SkyBlockPlayer(self)
        self.duels = Duels(self)
        self.tntgames = TNTGames(self)
        self.uhc = UHC(self)

    def refresh(self):
        data = requests.get(f"https://api.hypixel.net/player?uuid={self.uuid}&key={self.api.apikey}").json()
        self.fulldata = data
        self.data = data['player']

        self.id = self.getID
        self.displayname = self.getDisplayName
        self.firstLogin = self.getFirstLogin
        self.knownAliases = self.getKnownAliases
        self.knownAliasesLower = self.getKnownAliasesLower
        self.lastLogin = self.getLastLogin
        self.playerName = self.getPlayerName
        self.achievementsOneTime = self.getAchievementsOneTime
        self.userLanguage = self.getUserLanguage
        self.networkExp = self.getNetworkExp
        self.networkLevel = self.getNetworkLevel
        self.karma = self.getKarma
        self.mcVersion = self.getMcVersion
        self.hypixelForums = self.getHypixelForums
        self.discord = self.getDiscord
        self.twitter = self.getTwitter
        self.youtube = self.getYoutube
        self.rank = self.getRank
        self.rankColor = self.getRankColor
        self.monthlyPlusColor = self.getMonthlyRankColor
        self.monthlyPackageRank = self.getMonthlyPackageRank
        self.mostRecentMonthlyPackageRank = self.getMostRecentMonthlyPackageRank

    @property
    def getGuild(self):
        return self.api.guild(player=self.uuid)

    def getSkyBlockProfiles(self):
        data = getSkyBlockProfiles(self.api, self.uuid)

        if data is None:
            return None

        profiles = []

        for i in data['profiles']:
            profiles.append(SkyBlockProfile(i))

        return profiles

    @property
    def getID(self):
        """
        No wonder what this means .-. (probably hypixel player id)
        :return: id [string]
        """
        return self.data['_id']

    @property
    def getUUID(self):
        """
        Returns the player's uuid (Unique User ID)
        :return: uuid [string]
        """
        return self.data['uuid']

    @property
    def getDisplayName(self):
        """
        Returns the player's display name
        :return: display name [string]
        """
        return self.data['displayname']

    @property
    def getFirstLogin(self):
        """
        Returns the player's first login time
        :return: first login time [integer, unix ms]
        """
        return self.data['firstLogin']

    @property
    def getKnownAliases(self):
        """
        Returns player's known nicknames
        :return: player's known nicknames [list of strings]
        """
        return self.data['knownAliases']

    @property
    def getKnownAliasesLower(self):
        """
        Returns player's known nicknames (all lowercase)
        :return: player's known nicknames (all lowercase) [list of strings]
        """
        return self.data['knownAliasesLower']

    @property
    def getLastLogin(self):
        """
        Returns player's last login time
        :return: last login time [integer, unix ms]
        """
        if 'lastLogin' in self.data:
            return self.data['lastLogin']
        return None

    @property
    def getPlayerName(self):
        """
        Returns player's nickname
        :return: player's name
        """
        return self.data['playername']

    @property
    def getAchievementsOneTime(self):
        """
        Returns all player's achievements
        :return: player's achievements [list of strings]
        """
        return self.data['achievementsOneTime']

    def getHasAchievement(self, achievement):
        """
        Returns whether player has an achievement or not
        :param achievement: achievement name
        :return: whether the player has the achievement or not [bool]
        """
        return achievement in self.data['achievementsOneTime']

    @property
    def getLastLogout(self):
        """
        Returns player's last logout time
        :return: last logout time [integer, unix ms]
        """
        if 'lastLogout' in self.data:
            return self.data['lastLogout']
        return None

    @property
    def getUserLanguage(self):
        if 'userLanguage' not in self.data:
            return None
        return self.data['userLanguage']

    @property
    def getNetworkExp(self):
        if 'networkExp' not in self.data:
            return None
        return self.data['networkExp']

    @property
    def getNetworkLevel(self):
        if self.getNetworkExp is None:
            return 1
        return 1 - 3.5 + math.sqrt(12.25 + 0.0008 * self.getNetworkExp)

    @property
    def getKarma(self):
        if 'karma' not in self.data:
            return None
        return self.data['karma']

    @property
    def getMcVersion(self):
        if 'mcVersionRp' not in self.data:
            return None
        return self.data['mcVersionRp']

    @property
    def getHypixelForums(self):
        if 'socialMedia' in self.data:
            if 'links' in self.data['socialMedia']:
                if 'HYPIXEL' in self.data['socialMedia']['links']:
                    return self.data['socialMedia']['links']['HYPIXEL']
        return None

    @property
    def getInstagram(self):
        if 'socialMedia' in self.data:
            if 'links' in self.data['socialMedia']:
                if 'INSTAGRAM' in self.data['socialMedia']['links']:
                    return self.data['socialMedia']['links']['INSTAGRAM']
        return None

    @property
    def getDiscord(self):
        if 'socialMedia' in self.data:
            if 'links' in self.data['socialMedia']:
                if 'DISCORD' in self.data['socialMedia']['links']:
                    return self.data['socialMedia']['links']['DISCORD']
        return None

    @property
    def getTwitter(self):
        if 'socialMedia' in self.data:
            if 'links' in self.data['socialMedia']:
                if 'TWITTER' in self.data['socialMedia']['links']:
                    return self.data['socialMedia']['links']['TWITTER']
        return None

    @property
    def getYoutube(self):
        if 'socialMedia' in self.data:
            if 'links' in self.data['socialMedia']:
                if 'YOUTUBE' in self.data['socialMedia']['links']:
                    return self.data['socialMedia']['links']['YOUTUBE']
        return None

    @property
    def getRank(self):
        rank = "DEFAULT"
        if 'newPackageRank' in self.data:
            rank = self.data['newPackageRank']
            if rank == "YOUTUBER":
                rank = "YOUTUBE"
            elif rank == "MVP_PLUS_PLUS":
                rank = "MVP++"
            elif rank == "MVP_PLUS":
                rank = "MVP+"
            elif rank == "VIP_PLUS":
                rank = "VIP+"
        return rank

    @property
    def getRankColor(self):
        if 'rankPlusColor' not in self.data:
            return None
        return self.data['rankPlusColor']

    @property
    def getMonthlyRankColor(self):
        if 'monthlyPlusColor' not in self.data:
            return None
        return self.data['monthlyPlusColor']

    @property
    def getMonthlyPackageRank(self):
        if 'monthlyPackageRank' not in self.data:
            return None
        return self.data['monthlyPackageRank']

    @property
    def getMostRecentMonthlyPackageRank(self):
        if 'mostRecentMonthlyPackageRank' not in self.data:
            return None
        return self.data['mostRecentMonthlyPackageRank']

    @property
    def getSkyWars(self):
        return self.skywars

    @property
    def getBedWars(self):
        return self.bedwars

    @property
    def getMurderMystery(self):
        return self.murdermystery

    @property
    def getBuildBattle(self):
        return self.buildbattle

    @property
    def getSkyBlock(self):
        return self.skyblock

    @property
    def getDuels(self):
        return self.duels

    @property
    def getTntGames(self):
        return self.tntgames

    @property
    def getUhc(self):
        return self.uhc
