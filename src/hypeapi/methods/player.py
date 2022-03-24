import requests
import math

from .games.skywars import *
from .games.bedwars import *
from .games.murdermystery import *
from .games.buildbuttle import *

class Player:
    def __init__(self, api, data):
        self.api = api
        self.data = data['player']
        self.name = self.data['playername']
        self.uuid = self.data['uuid']
        self.fulldata = data

        self.id = self.getID()
        self.displayname = self.getDisplayName()
        self.firstLogin = self.getFirstLogin()
        self.knownAliases = self.getKnownAliases()
        self.knownAliasesLower = self.getKnownAliasesLower()
        self.lastLogin = self.getLastLogin()
        self.playerName = self.getPlayerName()
        self.achievementsOneTime = self.getAchievementsOneTime()
        self.userLanguage = self.getUserLanguage()
        self.networkExp = self.getNetworkExp()
        self.networkLevel = self.getNetworkLevel()
        self.karma = self.getKarma()
        self.mcVersion = self.getMcVersion()
        self.hypixelForums = self.getHypixelForums()
        self.discord = self.getDiscord()
        self.twitter = self.getTwitter()
        self.youtube = self.getYoutube()
        self.rank = self.getRank()
        self.rankColor = self.getRankColor()
        self.monthlyPlusColor = self.getMonthlyRankColor()
        self.monthlyPackageRank = self.getMonthlyPackageRank()
        self.mostRecentMonthlyPackageRank = self.getMostRecentMonthlyPackageRank()

        self.skywars = SkyWars(self)
        self.bedwars = BedWars(self)
        self.murdermystery = MurderMystery(self)
        self.buildbattle = BuildBattle(self)

    def refresh(self):
        data = requests.get(f"https://api.hypixel.net/player?uuid={self.uuid}&key={self.api.apikey}").json()

        self.id = self.getID()
        self.displayname = self.getDisplayName()
        self.firstLogin = self.getFirstLogin()
        self.knownAliases = self.getKnownAliases()
        self.knownAliasesLower = self.getKnownAliasesLower()
        self.lastLogin = self.getLastLogin()
        self.playerName = self.getPlayerName()
        self.achievementsOneTime = self.getAchievementsOneTime()
        self.userLanguage = self.getUserLanguage()
        self.networkExp = self.getNetworkExp()
        self.networkLevel = self.getNetworkLevel()
        self.karma = self.getKarma()
        self.mcVersion = self.getMcVersion()
        self.hypixelForums = self.getHypixelForums()
        self.discord = self.getDiscord()
        self.twitter = self.getTwitter()
        self.youtube = self.getYoutube()
        self.rank = self.getRank()
        self.rankColor = self.getRankColor()
        self.monthlyPlusColor = self.getMonthlyRankColor()
        self.monthlyPackageRank = self.getMonthlyPackageRank()
        self.mostRecentMonthlyPackageRank = self.getMostRecentMonthlyPackageRank()

    def getGuild(self):
        return self.api.guild(player=self.uuid)

    def getID(self):
        '''
        No wonder what this means .-. (probably hypixel player id)
        :return: id [string]
        '''
        return self.data['_id']

    def getUUID(self):
        '''
        Returns the player's uuid (Unique User ID)
        :return: uuid [string]
        '''
        return self.data['uuid']

    def getDisplayName(self):
        '''
        Returns the player's display name
        :return: display name [string]
        '''
        return self.data['displayname']

    def getFirstLogin(self):
        '''
        Returns the player's first login time
        :return: first login time [integer, unix ms]
        '''
        return self.data['firstLogin']

    def getKnownAliases(self):
        '''
        Returns plauer's known nicknames
        :return: player's known nicknames [list of strings]
        '''
        return self.data['knownAliases']

    def getKnownAliasesLower(self):
        '''
        Returns plauer's known nicknames (all lowercase)
        :return: player's known nicknames (all lowercase) [list of strings]
        '''
        return self.data['knownAliasesLower']

    def getLastLogin(self):
        '''
        Returns player's last login time
        :return: last login time [integer, unix ms]
        '''
        if 'lastLogin' in self.data:
            return self.data['lastLogin']
        return None

    def getPlayerName(self):
        '''
        Returns player's nickname
        :return: player's name
        '''
        return self.data['playername']

    def getAchievementsOneTime(self):
        '''
        Returns all player's achievements
        :return: player's achievements [list of strings]
        '''
        return self.data['achievementsOneTime']

    def getHasAchievement(self, achievement):
        '''
        Returns whether player has an achievement or not
        :param achievement: achievement name
        :return: whether the player has the achievement or not [bool]
        '''
        return achievement in self.data['achievementsOneTime']

    def getLastLogout(self):
        '''
        Returns player's last logout time
        :return: last logout time [integer, unix ms]
        '''
        if 'lastLogout' in self.data:
            return self.data['lastLogout']
        return None

    def getUserLanguage(self):
        return self.data['userLanguage']

    def getNetworkExp(self):
        return self.data['networkExp']

    def getNetworkLevel(self):
        return (1 - 3.5 + math.sqrt(12.25 + 0.0008 * self.getNetworkExp()))

    def getKarma(self):
        return self.data['karma']

    def getMcVersion(self):
        if 'mcVersionRp' in self.data:
            return self.data['mcVersionRp']
        return None

    def getHypixelForums(self):
        if 'socialMedia' in self.data:
            if 'links' in self.data['socialMedia']:
                if 'HYPIXEL' in self.data['socialMedia']['links']:
                    return self.data['socialMedia']['links']['HYPIXEL']
        return None

    def getInstagram(self):
        if 'socialMedia' in self.data:
            if 'links' in self.data['socialMedia']:
                if 'INSTAGRAM' in self.data['socialMedia']['links']:
                    return self.data['socialMedia']['links']['INSTAGRAM']
        return None

    def getDiscord(self):
        if 'socialMedia' in self.data:
            if 'links' in self.data['socialMedia']:
                if 'DISCORD' in self.data['socialMedia']['links']:
                    return self.data['socialMedia']['links']['DISCORD']
        return None

    def getTwitter(self):
        if 'socialMedia' in self.data:
            if 'links' in self.data['socialMedia']:
                if 'TWITTER' in self.data['socialMedia']['links']:
                    return self.data['socialMedia']['links']['TWITTER']
        return None

    def getYoutube(self):
        if 'socialMedia' in self.data:
            if 'links' in self.data['socialMedia']:
                if 'YOUTUBE' in self.data['socialMedia']['links']:
                    return self.data['socialMedia']['links']['YOUTUBE']
        return None

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

    def getRankColor(self):
        if 'rankPlusColor' in self.data:
            return self.data['rankPlusColor']
        return None

    def getMonthlyRankColor(self):
        if 'monthlyPlusColor' in self.data:
            return self.data['monthlyPlusColor']
        return None

    def getMonthlyPackageRank(self):
        if 'monthlyPackageRank' in self.data:
            return self.data['monthlyPackageRank']
        return None

    def getMostRecentMonthlyPackageRank(self):
        if 'mostRecentMonthlyPackageRank' in self.data:
            return self.data['mostRecentMonthlyPackageRank']
        return None

    def getSkyWars(self):
        return self.skywars

    def getBedWars(self):
        return self.bedwars

    def getMurderMystery(self):
        return self.murdermystery

    def getBuildBattle(self):
        return self.buildbattle