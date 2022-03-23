import requests

from errorhandler import *
from methods.player import *


class API:
    def __init__(self, apikey):
        self.apikey = apikey

    def player(self, name='', uuid=''):
        """
        Gets player object
        :param name: Name of the player (use one of these)
        :param uuid: Uuid of the player (use one of these)
        :return: player object
        """
        if name:
            data = requests.get(f"https://api.hypixel.net/player?name={name}&key={self.apikey}").json()
            if data['success'] == False:
                raise APIException(data['cause'])
            elif not 'player' in data or data['player'] == None:
                raise APIException("Non-existing player")
        elif uuid:
            data=requests.get(f"https://api.hypixel.net/player?uuid={uuid}&key={self.apikey}").json()
        else:
            raise NoArgumentsException
        return Player(self, data)

    def guild(self, name='', id='', player=''):
        if name:
            data=requests.get(f"https://api.hypixel.net/guild?name={name}&key={self.apikey}").json()
            if data['success'] == False:
                raise APIException(data['cause'])
            elif not 'guild' in data or data['guild'] == None:
                raise APIException("Non-existing guild")

        if id:
            data=requests.get(f"https://api.hypixel.net/guild?id={id}&key={self.apikey}").json()
            if data['success'] == False:
                raise APIException(data['cause'])
            elif not 'guild' in data or data['guild'] == None:
                raise APIException("Non-existing guild")

        if player:
            data=requests.get(f"https://api.hypixel.net/guild?player={player}&key={self.apikey}")
            if data['success'] == False:
                raise APIException(data['cause'])
            elif not 'guild' in data or data['guild'] == None:
                raise APIException("Non-existing guild")
        return Guild(self, data)