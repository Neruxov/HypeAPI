class Duels:
    def __init__(self, player):
        self.player = player
        self.data = self.player.data
        if 'Duels' not in self.data['stats']:
            self.dueldata = self.data['stats']
        else:
            self.dueldata = self.data['stats']['Duels']

        self.wins = self.getWins
        self.kills = self.getKills
        self.losses = self.getLosses
        self.coins = self.getCoins
        self.bowHits = self.getBowHits
        self.deaths = self.getDeaths
        self.playedGames = self.getPlayedGames
        self.chests = self.getChests
        self.wlr = self.getWlr
        self.kd = self.getKd
        self.bowShots = self.getBowShots

    @property
    def getWins(self):
        if 'wins' not in self.dueldata:
            return None
        return self.dueldata['wins']

    @property
    def getKills(self):
        if 'kills' not in self.dueldata:
            return None
        return self.dueldata['kills']

    @property
    def getCoins(self):
        if 'coins' not in self.dueldata:
            return None
        return self.dueldata['coins']

    @property
    def getLosses(self):
        if 'losses' not in self.dueldata:
            return None
        return self.dueldata['losses']

    @property
    def getBowHits(self):
        if 'bowHits' not in self.dueldata:
            return None
        return self.dueldata['bowHits']

    @property
    def getWlr(self):
        if 'wins' and 'losses' not in self.dueldata:
            return None
        return self.dueldata['wins'] / self.dueldata['losses']

    @property
    def getKd(self):
        if 'kills' and 'losses' not in self.dueldata:
            return None
        return self.dueldata['kills'] / self.dueldata['losses']

    @property
    def getDeaths(self):
        if 'deaths' not in self.dueldata:
            return None
        return self.dueldata['deaths']

    @property
    def getPlayedGames(self):
        if 'games_played_duels' not in self.dueldata:
            return None
        return self.dueldata['games_played_duels']

    @property
    def getChests(self):
        if 'duels_chests' not in self.dueldata:
            return None
        return self.dueldata['duels_chests']

    @property
    def getBowShots(self):
        if 'bow_shots' not in self.dueldata:
            return None
        return self.dueldata['bow_shots']
