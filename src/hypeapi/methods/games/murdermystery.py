class MurderMystery:
    def __init__(self, player):
        self.player = player
        self.data = self.player.data
        if 'MurderMystery' not in self.data['stats']:
            self.mmdata = self.data['stats']
        else:
            self.mmdata = self.data['stats']['MurderMystery']

        self.wins = self.getWins
        self.kills = self.getKills
        self.chests = self.getChests
        self.deaths = self.getDeaths
        self.coins = self.getCoins
        self.games = self.getGames
        self.detective_wins = self.getDetectiveWins
        self.murder_wins = self.getMurderWins

    @property
    def getWins(self):
        if 'wins' not in self.mmdata:
            return None
        return self.mmdata['wins']

    @property
    def getCoins(self):
        if 'coins' not in self.mmdata:
            return None
        return self.mmdata['coins']

    @property
    def getGames(self):
        if 'games' not in self.mmdata:
            return None
        return self.mmdata['games']

    @property
    def getKills(self):
        if 'kills' not in self.mmdata:
            return None
        return self.mmdata['kills']

    @property
    def getDeaths(self):
        if 'deaths' not in self.mmdata:
            return None
        return self.mmdata['deaths']

    @property
    def getChests(self):
        if 'mm_chests' not in self.mmdata:
            return None
        return self.mmdata['mm_chests']

    @property
    def getDetectiveWins(self):
        if 'detective_wins' not in self.mmdata:
            return None
        return self.mmdata['detective_wins']

    @property
    def getMurderWins(self):
        if 'murder_wins' not in self.mmdata:
            return None
        return self.mmdata['murderer_wins']
