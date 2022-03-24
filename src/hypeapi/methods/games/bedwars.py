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
        return self.bwdata['kills_bedwars']

    def getWins(self):
        return self.bwdata['wins_bedwars']

    def getFinalKills(self):
        return self.bwdata['final_kills_bedwars']

    def getFinalDeaths(self):
        return self.bwdata['final_deaths_bedwars']

    def getBedsBroken(self):
        return self.bwdata['beds_broken_bedwars']

    def getBedLosses(self):
        return self.bwdata['beds_lost_bedwars']

    def getCoins(self):
        return self.bwdata['coins']

    def getExp(self):
        return self.bwdata['Experience']

    def getLosses(self):
        return self.bwdata['losses_bedwars']

    def getPlayedGames(self):
        return self.bwdata['games_played_bedwars']

    def getKD(self):
        return self.bwdata['kills_bedwars'] \
            / self.bwdata['deaths_bedwars']

    def getDeaths(self):
        return self.bwdata['deaths_bedwars']

    def getFinalKD(self):
        return self.bwdata['final_kills_bedwars'] / self.bwdata['final_deaths_bedwars']