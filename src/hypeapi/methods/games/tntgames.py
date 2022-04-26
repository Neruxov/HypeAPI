class TNTGames:
    def __init__(self, player):
        self.player = player
        self.data = self.player.data
        if 'TNTGames' not in self.data['stats']:
            self.tntdata = self.data['stats']
        else:
            self.tntdata = self.data['stats']['TNTGames']

        self.coins = self.getCoins
        self.TntRunDeaths = self.getTntRunDeaths
        self.TntRunRecord = self.getTntRunRecord
        self.TntTagKills = self.getTntTagKills
        self.TntTagDeaths = self.getTntTagDeaths
        self.wins = self.getWins
        self.pvprunrecord = self.getPvpRunRecord

    @property
    def getWins(self):
        if 'wins' not in self.tntdata:
            return None
        return self.tntdata['wins']

    @property
    def getCoins(self):
        if 'coins' not in self.tntdata:
            return None
        return self.tntdata['coins']

    @property
    def getTntRunDeaths(self):
        if 'deaths_tntrun' not in self.tntdata:
            return None
        return self.tntdata['deaths_tntrun']

    @property
    def getTntRunRecord(self):
        if 'record_tntrun' not in self.tntdata:
            return None
        return self.tntdata['record_tntrun']

    @property
    def getTntTagKills(self):
        if 'kills_tnttag' not in self.tntdata:
            return None
        return self.tntdata['kills_tnttag']

    @property
    def getTntTagDeaths(self):
        if 'deaths_tntag' not in self.tntdata:
            return None
        return self.tntdata['deaths_tntag']

    @property
    def getPvpRunRecord(self):
        if 'record_pvprun' not in self.tntdata:
            return None
        return self.tntdata['record_pvprun']
