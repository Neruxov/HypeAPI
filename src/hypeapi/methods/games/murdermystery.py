class MurderMystery:
    def __init__(self, player):
        self.player = player
        self.data = self.player.data
        if 'MurderMystery' not in self.data['stats']:
            self.mmdata = self.data['stats']
        else:
            self.mmdata = self.data['stats']['MurderMystery']

        self.wins = self.getWins()
        self.kills = self.getKills()
        self.chests = self.getChests()
        self.deaths = self.getDeaths()
        self.coins = self.getCoins()
        self.games = self.getGames()
        self.detective_wins = self.getDetectiveWins()
        self.murder_wins = self.getMurderWins()

    def getWins(self):
        if 'wins' not in self.mmdata:
            return None
        return self.mmdata['wins']

    def getCoins(self):
        if 'coins' not in self.mmdata:
            return None
        return self.mmdata['coins']

    def getGames(self):
        if 'games' not in self.mmdata:
            return None
        return self.mmdata['games']

    def getKills(self):
        if 'kills' not in self.mmdata:
            return None
        return self.mmdata['kills']

    def getDeaths(self):
        if 'deaths' not in self.mmdata:
            return None
        return self.mmdata['deaths']

    def getChests(self):
        if 'mm_chests' not in self.mmdata:
            return None
        return self.mmdata['mm_chests']

    def getDetectiveWins(self):
        if 'detective_wins' not in self.mmdata:
            return None
        return self.mmdata['detective_wins']

    def getMurderWins(self):
        if 'murder_wins' not in self.mmdata:
            return None
        return self.mmdata['murderer_wins']
