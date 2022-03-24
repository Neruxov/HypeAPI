from ...player import *
from ....util.api_requests import *

class SkyBlockMember(Player):
    def __init__(self, api, data):
        super().__init__(api, getPlayerData(api, uuid=data['uuid']))

        self.api = api
        self.data = data