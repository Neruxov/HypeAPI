from .methods.games.skyblock import *
from .methods.guild import *
from .util.logger import *


class API:
    def __init__(self, apikey, debug=False):
        self.debug = debug
        self.logger = Logger()
        self.apikey = apikey
        if not checkKeyValidity(self):
            raise APIException("Invalid API key")
        self.skyblock = self.getSkyBlock()

    def getPlayer(self, name=None, uuid=None):
        """
        Gets player object
        :param name: name of the player (use one of these)
        :param uuid: uuid of the player (use one of these)
        :return: player object
        """
        return Player(self, getPlayerData(self, name=name, uuid=uuid))

    def getGuild(self, name=None, player=None, id=None, members=False):
        return Guild(self, getGuildData(self, name=name, player=player, id=id), members=members)

    def getSkyBlock(self):
        return SkyBlock(self)
