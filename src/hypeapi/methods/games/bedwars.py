import requests

class BedWars:
    def __init__(self, player):
        self.player = player
        self.data = self.player.data
        self.bwdata = self.data['stats']['Bedwars']

        self.kills = self.getKills()
        self.wins = self.getWins()
        self.bedsBroken = self.getBedsBroken()
        self.finalKills = self.getFinalKills()
        self.finalDeath = self.getFinalDeaths()
        self.exp = self.getExp()
        self.coins = self.getCoins()
        self.bedsLosses = self.getBedLosses()
        self.losses = self.getBedLosses()
        self.playedGames = self.getPlayedGames()
        self.kd = self.getKD()
        self.deaths = self.getDeaths()
        self.fkdr = self.getFinalKD()

    def getKills(self):
        if not 'kills_bedwars' in self.bwdata:
            return None
        return self.bwdata['kills_bedwars']

    def getWins(self):
        if not 'wins_bedwars' in self.bwdata:
            return None
        return self.bwdata['wins_bedwars']

    def getFinalKills(self):
        if not 'final_kills_bedwars' in self.bwdata:
            return None
        return self.bwdata['final_kills_bedwars']

    def getFinalDeaths(self):
        if not 'final_deaths_bedwars' in self.bwdata:
            return None
        return self.bwdata['final_deaths_bedwars']

    def getBedsBroken(self):
        if not 'beds_broken_bedwars' in self.bwdata:
            return None
        return self.bwdata['beds_broken_bedwars']

    def getBedLosses(self):
        if not 'beds_lost_bedwars' in self.bwdata:
            return None
        return self.bwdata['beds_lost_bedwars']

    def getCoins(self):
        if not 'coins' in self.bwdata:
            return None
        return self.bwdata['coins']

    def getExp(self):
        if not 'Experience' in self.bwdata:
            return None
        return self.bwdata['Experience']

    def getLosses(self):
        if not 'losses_bedwars' in self.bwdata:
            return None
        return self.bwdata['losses_bedwars']

    def getPlayedGames(self):
        if not 'losses_bedwars' in self.bwdata:
            return None
        return self.bwdata['games_played_bedwars']

    def getKD(self):
        if self.getKills() == None and self.getDeaths() == None:
            return 0
        if self.getKills()  == None:
            return 1 / self.getDeaths()
        if self.getDeaths() == None:
            return self.getKills()
        return self.getKills() / self.getDeaths()

    def getDeaths(self):
        if not 'deaths_bedwars' in self.bwdata:
            return None
        return self.bwdata['deaths_bedwars']

    def getFinalKD(self):
        if self.getFinalKills() == None and self.getFinalDeaths() == None:
            return 0
        if self.getFinalKills() == None:
            return 1 / self.getFinalDeaths()
        if self.getFinalDeaths() == None:
            return self.getFinalKills()
        return self.getFinalKills() / self.getFinalDeaths()