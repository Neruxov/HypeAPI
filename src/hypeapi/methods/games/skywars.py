import requests

class SkyWars:
    def __init__(self, player):
        self.player = player
        self.data = self.player.data
        if not 'SkyWars' in self.data['stats']:
            self.swdata = self.data['stats']
        else:
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
        if not 'skywars_experience' in self.swdata:
            return None
        return self.swdata['skywars_experience']

    def getLevel(self):
        xp = self.getExp()
        if xp == None:
            return 1
        xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
        if xp >= 15000:
            return (xp - 15000) / 10000. + 12
        else:
            for i in range(len(xps)):
                if xp < xps[i]:
                    return i + float(xp - xps[i - 1]) / (xps[i] - xps[i - 1])

    def getCoins(self):
        if not 'coins' in self.swdata:
            return None
        return self.swdata['coins']

    def getWins(self):
        if not 'wins' in self.swdata:
            return None
        return self.swdata['wins']

    def getLosses(self):
        if not 'losses' in self.swdata:
            return None
        return self.swdata['losses']

    def getKills(self):
        if not 'kills' in self.swdata:
            return None
        return self.swdata['kills']

    def getDeaths(self):
        if not 'deaths' in self.swdata:
            return None
        return self.swdata['deaths']

    def getAssists(self):
        if not 'assists' in self.swdata:
            return None
        return self.swdata['assists']

    def getSouls(self):
        if not 'souls' in self.swdata:
            return None
        return self.swdata['souls']

    def getWlr(self):
        if self.getWins() == None and self.getLosses() == None:
            return 0
        if self.getWins() == None:
            return 1 / self.getLosses()
        if self.getLosses() == None:
            return self.getWins()
        return self.getWins() / self.getLosses()

    def getKdr(self):
        if self.getKills() == None and self.getDeaths() == None:
            return 0
        if self.getKills() == None:
            return 1 / self.getDeaths()
        if self.getDeaths() == None:
            return self.getKills()
        return self.getKills() / self.getDeaths()

    def getSoulsGathered(self):
        if not 'souls_gathered' in self.swdata:
            return None
        return self.swdata['souls_gathered']

    def getArrowsShot(self):
        if not 'arrows_shot' in self.swdata:
            return None
        return self.swdata['arrows_shot']

    def getArrowsHit(self):
        if not 'arrows_hit' in self.swdata:
            return None
        return self.swdata['arrows_hit']

    def getArrowsHMR(self):
        '''
        Returns player's arrows hit/miss ratio
        :return: player's hit/miss ratio [float]
        '''
        if self.getArrowsHit() == None and self.getArrowsShot() == None:
            return 0
        if self.getArrowsHit() == None:
            return 1 / self.getArrowsShot()
        if self.getArrowsShot() == None:
            return self.getArrowsHit()
        return self.getArrowsHit() / self.getArrowsShot()

    def getEggsThrown(self):
        if not 'egg_thrown' in self.swdata:
            return None
        return self.swdata['egg_thrown']

    def getEnderpealsThrown(self):
        if not 'enderpearls_thrown' in self.swdata:
            return None
        return self.swdata['enderpearls_thrown']

    def getBlocksPlaced(self):
        if not 'blocks_placed' in self.swdata:
            return None
        return self.swdata['blocks_placed']

    def getBlocksBroken(self):
        if not 'blocks_broken' in self.swdata:
            return None
        return self.swdata['blocks_broken']

    def getSoulWell(self):
        if not 'soul_well' in self.swdata:
            return None
        return self.swdata['soul_well']

    def getSoulWellRares(self):
        if not 'soul_well_rares' in self.swdata:
            return None
        return self.swdata['soul_well_rares']

    def getSoulWellLegendaries(self):
        if not 'soul_well_legendaries' in self.swdata:
            return None
        return self.swdata['soul_well_legendaries']

    def getTotalHeads(self):
        if not 'heads' in self.swdata:
            return None
        return self.swdata['heads']