import requests


class GuildPlayer:
    def __init__(self, data):
        self.data = data

        self.uuid = self.getUuid()
        self.exp_history = self.getExpHistory()
        self.joindate = self.getJoinedDate()
        self.rank = self.getPlayerRank()
        self.questParticipation = self.getQuestParticipation()

    def getPlayerRank(self):
        return self.data['rank']

    def getJoinedDate(self):
        return self.data['joined']

    def getExpHistory(self):
        return self.data['expHistory']

    def getQuestParticipation(self):
        return self.data['questParticipation']

    def getUuid(self):
        return self.data['uuid']
