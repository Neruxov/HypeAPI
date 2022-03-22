import requests

from errorhandler import *
from methods.player import *

class API:
    def __init__(self, apikey):
        self.apikey = apikey

    def player(self, name='', uuid=''):
        '''
        Gets player object
        :param name: Name of the player (use one of these)
        :param uuid: Uuid of the player (use one of these)
        :return: player object
        '''
        if name:
            data = requests.get(f"https://api.hypixel.net/player?name={name}&key={self.apikey}").json()
        elif uuid:
            data = requests.get(f"https://api.hypixel.net/player?uuid={uuid}&key={self.apikey}").json()
        else:
            raise NoArguments
        return Player(data)