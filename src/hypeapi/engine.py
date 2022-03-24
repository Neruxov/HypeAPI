import requests

from .errorhandler import *
from .methods.player import *
from .methods.guild import *
from .util.api_requests import *

class API:
    def __init__(self, apikey):
        self.apikey = apikey
        checkKeyValidity(self)

    def player(self, name=None, uuid=None):
        """
        Gets player object
        :param name: name of the player (use one of these)
        :param uuid: uuid of the player (use one of these)
        :return: player object
        """
        return Player(self, getPlayerData(self, name=name, uuid=uuid))

    def guild(self, name=None, player=None, id=None, members=False):
        return Guild(self, getGuildData(self, name=name, player=player, id=id), members=members)