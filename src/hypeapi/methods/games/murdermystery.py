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
        if not 'wins' in self.mmdata:
            return None
        return self.mmdata['wins']

    def getCoins(self):
        if not 'coins' in self.mmdata:
            return None
        return self.mmdata['coins']

    def getGames(self):
        if not 'games' in self.mmdata:
            return None
        return self.mmdata['games']

    def getKills(self):
        if not 'kills' in self.mmdata:
            return None
        return self.mmdata['kills']

    def getDeaths(self):
        if not 'deaths' in self.mmdata:
            return None
        return self.mmdata['deaths']

    def getChests(self):
        if not 'mm_chests' in self.mmdata:
            return None
        return self.mmdata['mm_chests']

    def getDetectiveWins(self):
        if not 'detective_wins' in self.mmdata:
            return None
        return self.mmdata['detective_wins']

    def getMurderWins(self):
        if not 'murder_wins' in self.mmdata:
            return None
        return self.mmdata['murderer_wins']

