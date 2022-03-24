class Duels:
    def __init__(self, player):
        self.player=player
        self.data=self.player.data
        self.dueldata=self.data['stats']['Duels']

    def getWins(self):
        if not 'wins' in self.dueldata:
            return None
        return self.dueldata['wins']

