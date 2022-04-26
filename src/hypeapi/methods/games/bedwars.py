class BedWars:
    def __init__(self, player):
        self.player = player
        self.data = self.player.data
        self.bwdata = self.data['stats']['Bedwars']

        self.kills = self.getKills
        self.wins = self.getWins
        self.bedsBroken = self.getBedsBroken
        self.finalKills = self.getFinalKills
        self.finalDeath = self.getFinalDeaths
        self.exp = self.getExp
        self.coins = self.getCoins
        self.bedsLosses = self.getBedLosses
        self.losses = self.getBedLosses
        self.playedGames = self.getPlayedGames
        self.kd = self.getKD
        self.deaths = self.getDeaths
        self.fkdr = self.getFinalKD


    @property
    def getKills(self):
        if 'kills_bedwars' not in self.bwdata:
            return None
        return self.bwdata['kills_bedwars']

    @property
    def getWins(self):
        if 'wins_bedwars' not in self.bwdata:
            return None
        return self.bwdata['wins_bedwars']

    @property
    def getFinalKills(self):
        if 'final_kills_bedwars' not in self.bwdata:
            return None
        return self.bwdata['final_kills_bedwars']

    @property
    def getFinalDeaths(self):
        if 'final_deaths_bedwars' not in self.bwdata:
            return None
        return self.bwdata['final_deaths_bedwars']

    @property
    def getBedsBroken(self):
        if 'beds_broken_bedwars' not in self.bwdata:
            return None
        return self.bwdata['beds_broken_bedwars']

    @property
    def getBedLosses(self):
        if 'beds_lost_bedwars' not in self.bwdata:
            return None
        return self.bwdata['beds_lost_bedwars']

    @property
    def getCoins(self):
        if 'coins' not in self.bwdata:
            return None
        return self.bwdata['coins']

    @property
    def getExp(self):
        if 'Experience' in self.bwdata:
            return None
        return self.bwdata['Experience']

    @property
    def getLosses(self):
        if 'losses_bedwars' not in self.bwdata:
            return None
        return self.bwdata['losses_bedwars']

    @property
    def getPlayedGames(self):
        if 'losses_bedwars' not in self.bwdata:
            return None
        return self.bwdata['games_played_bedwars']

    @property
    def getKD(self):
        if self.getKills is None and self.getDeaths is None:
            return 0
        if self.getKills is None:
            return 1 / self.getDeaths
        if self.getDeaths is None:
            return self.getKills
        return self.getKills / self.getDeaths

    @property
    def getDeaths(self):
        if 'deaths_bedwars' not in self.bwdata:
            return None
        return self.bwdata['deaths_bedwars']

    @property
    def getFinalKD(self):
        if self.getFinalKills is None and self.getFinalDeaths is None:
            return 0
        if self.getFinalKills is None:
            return 1 / self.getFinalDeaths
        if self.getFinalDeaths is None:
            return self.getFinalKills
        return self.getFinalKills / self.getFinalDeaths
