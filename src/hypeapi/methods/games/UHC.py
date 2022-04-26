class UHC:
    def __init__(self, player):
        self.player = player
        self.data = self.player.data
        if 'UHC' not in self.data['stats']:
            self.uhcdata = self.data['stats']
        else:
            self.uhcdata = self.data['stats']['UHC']

        self.wins = self.getWins
        self.kills = self.getKills
        self.deaths = self.getDeaths
        self.coins = self.getCoins
        self.kdr = self.getKDR

    @property
    def getWins(self):
        if 'wins' not in self.uhcdata:
            return None
        return self.uhcdata['wins']

    @property
    def getKills(self):
        if 'kills' not in self.uhcdata:
            return None
        return self.uhcdata['kills']

    @property
    def getDeaths(self):
        if 'deaths' not in self.uhcdata:
            return None
        return self.uhcdata['deaths']

    @property
    def getCoins(self):
        if 'coins' not in self.uhcdata:
            return None
        return self.uhcdata['coins']

    @property
    def getKDR(self):
        if 'kills' and 'deaths' not in self.uhcdata:
            return None
        return self.uhcdata['kills'] / self.uhcdata['deaths']
