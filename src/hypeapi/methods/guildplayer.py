from .player import *
from..util.api_requests import *

class GuildPlayer(Player):
    def __init__(self, api, data):
        super().__init__(api, getPlayerData(api, uuid=data['uuid']))

        self.data = data

        self.uuid = self.getUuid()
        self.exp_history = self.getEXPHistory()
        self.joinDate = self.getJoinDate()
        self.rank = self.getPlayerRank()
        self.questParticipation = self.getQuestParticipation()

    def getPlayerRank(self):
        return self.data['rank']

    def getJoinDate(self):
        return self.data['joined']

    def getEXPHistory(self):
        return self.data['expHistory']

    def getQuestParticipation(self):
        return self.data['questParticipation']

    def getUuid(self):
        return self.data['uuid']