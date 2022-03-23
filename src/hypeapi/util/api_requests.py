import requests

from .uuid import *
from ..errorhandler import *

def getPlayerData(api, name=None, uuid=None):
    if name:
        uuid = NameToUUID(name)
    elif not uuid:
        raise NoArgumentsException

    payload = ({
        'uuid': uuid,
        'key': api.apikey
    })

    data = requests.get(f"https://api.hypixel.net/player", json=payload).json()

    if data['success'] == False:
        raise APIException(data['cause'])
    elif not 'player' in data or data['player'] == None:
        raise APIException('Non-existent player')

    return data

def getGuildData(api, name=None, player=None, id=None):
    if player:
        payload = ({
            'player': player,
            'key': api.apikey
        })
    elif name:
        payload = ({
            'name': name,
            'key': api.apikey
        })
    elif id:
        payload = ({
            'id': id,
            'key': api.apikey
        })
    else:
        raise NoArgumentsException

    data = requests.get(f"https://api.hypixel.net/guild", json=payload).json()

    if data['success'] == False:
        raise APIException(data['cause'])
    elif not 'guild' in data or data['guild'] == None:
        raise APIException('Non-existent guild')

    return data