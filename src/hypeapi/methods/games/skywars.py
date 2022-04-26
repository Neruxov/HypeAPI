class SkyWars:
    def __init__(self, player):
        self.player = player
        self.data = self.player.data
        if 'SkyWars' not in self.data['stats']:
            self.swdata = self.data['stats']
        else:
            self.swdata = self.data['stats']['SkyWars']

        self.exp = self.getExp
        self.level = self.getLevel
        self.coins = self.getCoins
        self.wins = self.getWins
        self.losses = self.getLosses
        self.kills = self.getKills
        self.deaths = self.getDeaths
        self.assists = self.getAssists
        self.souls = self.getSouls
        self.wlr = self.getWlr
        self.kdr = self.getKdr
        self.soulsGathered = self.getSoulsGathered
        self.arrowsShot = self.getArrowsShot
        self.arrowsHit = self.getArrowsHit
        self.arrowsHMR = self.getArrowsHMR
        self.eggsThrown = self.getEggsThrown
        self.enderpearlsThrown = self.getEnderpealsThrown
        self.blocksPlaced = self.getBlocksPlaced
        self.blocksBroken = self.getBlocksBroken
        self.soulWell = self.getSoulWell
        self.soulWellRares = self.getSoulWellRares
        self.soulWellLegendaries = self.getSoulWellLegendaries
        self.totalheads = self.getTotalHeads

    @property
    def getExp(self):
        if 'skywars_experience' not in self.swdata:
            return None
        return self.swdata['skywars_experience']

    @property
    def getLevel(self):
        xp = self.getExp
        if xp is None:
            return 1
        xps = [0, 20, 70, 150, 250, 500, 1000, 2000, 3500, 6000, 10000, 15000]
        if xp >= 15000:
            return (xp - 15000) / 10000. + 12
        else:
            for i in range(len(xps)):
                if xp < xps[i]:
                    return i + float(xp - xps[i - 1]) / (xps[i] - xps[i - 1])

    @property
    def getCoins(self):
        if 'coins' not in self.swdata:
            return None
        return self.swdata['coins']

    @property
    def getWins(self):
        if 'wins' not in self.swdata:
            return None
        return self.swdata['wins']

    @property
    def getLosses(self):
        if 'losses' not in self.swdata:
            return None
        return self.swdata['losses']

    @property
    def getKills(self):
        if 'kills' not in self.swdata:
            return None
        return self.swdata['kills']

    @property
    def getDeaths(self):
        if 'deaths' not in self.swdata:
            return None
        return self.swdata['deaths']

    @property
    def getAssists(self):
        if 'assists' not in self.swdata:
            return None
        return self.swdata['assists']

    @property
    def getSouls(self):
        if 'souls' not in self.swdata:
            return None
        return self.swdata['souls']

    @property
    def getWlr(self):
        if self.getWins is None and self.getLosses is None:
            return 0
        if self.getWins is None:
            return 1 / self.getLosses
        if self.getLosses is None:
            return self.getWins
        return self.getWins / self.getLosses

    @property
    def getKdr(self):
        if self.getKills is None and self.getDeaths is None:
            return 0
        if self.getKills is None:
            return 1 / self.getDeaths
        if self.getDeaths is None:
            return self.getKills
        return self.getKills / self.getDeaths

    @property
    def getSoulsGathered(self):
        if 'souls_gathered' not in self.swdata:
            return None
        return self.swdata['souls_gathered']

    @property
    def getArrowsShot(self):
        if 'arrows_shot' not in self.swdata:
            return None
        return self.swdata['arrows_shot']

    @property
    def getArrowsHit(self):
        if 'arrows_hit' not in self.swdata:
            return None
        return self.swdata['arrows_hit']

    @property
    def getArrowsHMR(self):
        """
        Returns player's arrows hit/miss ratio
        :return: player's hit/miss ratio [float]
        """
        if self.getArrowsHit is None and self.getArrowsShot is None:
            return 0
        if self.getArrowsHit is None:
            return 1 / self.getArrowsShot
        if self.getArrowsShot is None:
            return self.getArrowsHit()
        return self.getArrowsHit / self.getArrowsShot

    @property
    def getEggsThrown(self):
        if 'egg_thrown' not in self.swdata:
            return None
        return self.swdata['egg_thrown']

    @property
    def getEnderpealsThrown(self):
        if 'enderpearls_thrown' not in self.swdata:
            return None
        return self.swdata['enderpearls_thrown']

    @property
    def getBlocksPlaced(self):
        if 'blocks_placed' not in self.swdata:
            return None
        return self.swdata['blocks_placed']

    @property
    def getBlocksBroken(self):
        if 'blocks_broken' not in self.swdata:
            return None
        return self.swdata['blocks_broken']

    @property
    def getSoulWell(self):
        if 'soul_well' not in self.swdata:
            return None
        return self.swdata['soul_well']

    @property
    def getSoulWellRares(self):
        if 'soul_well_rares' not in self.swdata:
            return None
        return self.swdata['soul_well_rares']

    @property
    def getSoulWellLegendaries(self):
        if 'soul_well_legendaries' not in self.swdata:
            return None
        return self.swdata['soul_well_legendaries']

    @property
    def getTotalHeads(self):
        if 'heads' not in self.swdata:
            return None
        return self.swdata['heads']
