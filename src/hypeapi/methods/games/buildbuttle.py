class BuildBattle:
    def __init__(self, player):
        self.player = player
        self.data = self.player.data
        if 'BuildBattle' not in self.data['stats']:
            self.bbdata = self.data['stats']
        else:
            self.bbdata = self.data['stats']['BuildBattle']

        self.coins = self.getCoins
        self.correct_guesses = self.getCorrect_guesses
        self.wins = self.getWins
        self.super_votes = self.getSuperVotes
        self.score = self.getScore

    @property
    def getCoins(self):
        if 'coins' not in self.bbdata:
            return None
        return self.bbdata['coins']

    @property
    def getCorrect_guesses(self):
        if 'correct_guesses' not in self.bbdata:
            return None
        return self.bbdata['correct_guesses']

    @property
    def getWins(self):
        if 'wins' not in self.bbdata:
            return None
        return self.bbdata['wins']

    @property
    def getSuperVotes(self):
        if 'super_votes' not in self.bbdata:
            return None
        return self.bbdata['super_votes']

    @property
    def getScore(self):
        if 'score' not in self.bbdata:
            return None
        return self.bbdata['score']
