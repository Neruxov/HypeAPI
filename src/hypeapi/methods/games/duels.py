class Duels:
    def __init__(self, player):
        self.player = player
        self.data = self.player.data
        if 'Duels' not in self.data['stats']:
            self.dueldata = self.data['stats']
        else:
            self.dueldata = self.data['stats']['Duels']

    def getWins(self):
        if 'wins' not in self.dueldata:
            return None
        return self.dueldata['wins']
