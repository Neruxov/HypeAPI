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
        return self.bbdata['coins']

    def getCorrect_guesses(self):
        return self.bbdata['correct_guesses']

    def getWins(self):
        return self.bbdata['wins']

    def getSuperVotes(self):
        return self.bbdata['super_votes']

    def getScore(self):
        return self.bbdata['score']


