class Duels:
    def __init__(self, player):
        self.player = player
        self.data = self.player.data
        if 'Duels' not in self.data['stats']:
            self.dueldata = self.data['stats']
        else:
            self.dueldata = self.data['stats']['Duels']

        self.wins = self.getWins()
        self.kills = self.getKills()
        self.losses = self.getLosses()
        self.coins = self.getCoins()
        self.bowHits = self.getBowHits()
        self.deaths = self.getDeaths()
        self.playedGames = self.getPlayedGames()
        self.chests = self.getChests()
        self.wlr = self.getWlr()
        self.kd = self.getKd()
        self.bowShots = self.getBowShots()


    def getWins(self):
        if 'wins' not in self.dueldata:
            return None
        return self.dueldata['wins']

    def getKills(self):
        if 'kills' not in self.dueldata:
            return None
        return self.dueldata['kills']


    def getLosses(self):
        if 'losses' not in self.dueldata:
            return None
        return self.dueldata['losses']

    def getCoins(self):
        if 'coins' not in self.dueldata:
            return None
        return self.dueldata['coins']

    def getLosses(self):
        if 'losses' not in self.dueldata:
            return None
        return self.dueldata['losses']

    def getBowHits(self):
        if 'bowHits' not in self.dueldata:
            return None
        return self.dueldata['bowHits']


    def getWlr(self):
        if 'wins' and 'losses' not in self.dueldata:
            return None
        return self.dueldata['wins'] / self.dueldata['losses']

    def getKd(self):
        if 'kills' and 'losses' not in self.dueldata:
            return None
        return self.dueldata['kills'] / self.dueldata['losses']

    def getDeaths(self):
        if 'deaths' not in self.dueldata:
            return None
        return self.dueldata['deaths']

    def getPlayedGames(self):
        if 'games_played_duels' not in self.dueldata:
            return None
        return self.dueldata['games_played_duels']

    def getChests(self):
        if 'duels_chests' not in self.dueldata:
            return None
        return self.dueldata['duels_chests']

    def getBowShots(self):
        if 'bow_shots' not in self.dueldata:
            return None
        return self.dueldata['bow_shots']