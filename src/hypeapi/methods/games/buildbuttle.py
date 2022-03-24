import requests

class BuildBattle:
    def __init__(self, player):
        self.player=player
        self.data=self.player.data
        self.bbdata=self.data['stats']['BuildBattle']

        self.coins = self.getCoins()
        self.correct_guesses = self.getCorrect_guesses()
        self.wins = self.getWins()
        self.super_votes = self.getSuperVotes()
        self.score = self.getScore()

    def getCoins(self):
        if not 'coins' in self.bbdata:
            return None
        return self.bbdata['coins']

    def getCorrect_guesses(self):
        if not 'correct_guesses' in self.bbdata:
            return None
        return self.bbdata['correct_guesses']

    def getWins(self):
        if not 'wins' in self.bbdata:
            return None
        return self.bbdata['wins']

    def getSuperVotes(self):
        if not 'super_votes' in self.bbdata:
            return None
        return self.bbdata['super_votes']

    def getScore(self):
        if not 'score' in self.bbdata:
            return None
        return self.bbdata['score']


