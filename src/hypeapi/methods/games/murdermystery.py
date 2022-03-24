import requests


class MurderMystery:
    def __init__(self, player):
        self.player=player
        self.data=self.player.data
        self.mmdata=self.data['stats']['MurderMystery']

        self.wins = self.getWins()
        self.kills = self.getKills()
        self.chests = self.getChests()
        self.deaths = self.getDeaths()
        self.coins = self.getCoins()
        self.games = self.getGames()
        self.detective_wins = self.getDetectiveWins()
        self.murder_wins = self.getMurderWins()

    def getWins(self):
        return self.mmdata['wins']

    def getCoins(self):
        return self.mmdata['coins']

    def getGames(self):
        return self.mmdata['games']

    def getKills(self):
        return self.mmdata['kills']

    def getDeaths(self):
        return self.mmdata['deaths']

    def getChests(self):
        return self.mmdata['mm_chests']

    def getDetectiveWins(self):
        return self.mmdata['detective_wins']

    def getMurderWins(self):
        return self.mmdata['murderer_wins']

