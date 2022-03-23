import requests

class SkyWars:
    def __init__(self, player):
        self.player = player
        self.data = self.player.data
        self.swdata = self.data['stats']['SkyWars']

        self.exp = self.getExp()
        self.level = self.getLevel()
        self.coins = self.getCoins()
        self.wins = self.getWins()
        self.losses = self.getLosses()
        self.kills = self.getKills()
        self.deaths = self.getDeaths()
        self.assists = self.getAssists()
        self.souls = self.getSouls()
        self.wlr = self.getWlr()
        self.kdr = self.getKdr()
        self.soulsGathered = self.getSoulsGathered()
        self.arrowsShot = self.getArrowsShot()
        self.arrowsHit = self.getArrowsHit()
        self.arrowsHMR = self.getArrowsHMR()
        self.eggsThrown = self.getEggsThrown()
        self.enderpearlsThrown = self.getEnderpealsThrown()
        self.blocksPlaced = self.getBlocksPlaced()
        self.blocksBroken = self.getBlocksBroken()
        self.soulWell = self.getSoulWell()
        self.soulWellRares = self.getSoulWellRares()
        self.soulWellLegendaries = self.getSoulWellLegendaries()
        self.totalheads = self.getTotalHeads()

    def getExp(self):
        return self.swdata['skywars_experience']

    def getLevel(self):
        xp = self.getExp()
        xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
        if xp >= 15000:
            return (xp - 15000) / 10000. + 12
        else:
            for i in range(len(xps)):
                if xp < xps[i]:
                    return i + float(xp - xps[i - 1]) / (xps[i] - xps[i - 1])

    def getCoins(self):
        return self.swdata['coins']

    def getWins(self):
        return self.swdata['wins']

    def getLosses(self):
        return self.swdata['losses']

    def getKills(self):
        return self.swdata['kills']

    def getDeaths(self):
        return self.swdata['deaths']

    def getAssists(self):
        return self.swdata['assists']

    def getSouls(self):
        return self.swdata['souls']

    def getWlr(self):
        return self.getWins() / self.getLosses()

    def getKdr(self):
        return self.getKills() / self.getDeaths()

    def getSoulsGathered(self):
        return self.swdata['souls_gathered']

    def getArrowsShot(self):
        return self.swdata['arrows_shot']

    def getArrowsHit(self):
        return self.swdata['arrows_hit']

    def getArrowsHMR(self):
        '''
        Returns player's arrows hit/miss ratio
        :return: player's hit/miss ratio [float]
        '''
        return self.getArrowsHit() / self.getArrowsShot()

    def getEggsThrown(self):
        return self.swdata['egg_thrown']

    def getEnderpealsThrown(self):
        return self.swdata['enderpearls_thrown']

    def getBlocksPlaced(self):
        return self.swdata['blocks_placed']

    def getBlocksBroken(self):
        return self.swdata['blocks_broken']

    def getSoulWell(self):
        return self.swdata['soul_well']

    def getSoulWellRares(self):
        return self.swdata['soul_well_rares']

    def getSoulWellLegendaries(self):
        return self.swdata['soul_well_legendaries']

    def getTotalHeads(self):
        return self.swdata['heads']