import requests

from .uuid import *
from ..errorhandler import *

def jsonToString(payload):
    string = ""
    for i in payload:
        string += f"{i}={payload[i]}&"
    return string[:-1]

def checkKeyValidity(api):
    payload = ({
        'key': api.apikey
    })

    if api.debug:
        api.logger.log(f"Sending a request to /key with payload: {jsonToString(payload)}", file=__name__)

    data = requests.get(f"https://api.hypixel.net/key?{jsonToString(payload)}").json()

    if api.debug:
        if len(str(data)) > 250:
            api.logger.log(f"Received a response from /key: Data too long", file=__name__)
        else:
            api.logger.log(f"Received a response from /key: {data}", file=__name__)

    if data['success'] == False:
        if api.debug:
            api.logger.log(f"Received an error from /key: {data['cause']}", file=__name__)
        return None

    if api.debug:
        api.logger.log(f"Loaded a valid api key: Owner: {UUIDToName(data['record']['owner'])}, Limit: {data['record']['limit']}, Total Requests: {data['record']['totalQueries']}", file=__name__)

def getPlayerData(api, name=None, uuid=None):
    if name:
        uuid = NameToUUID(name)
    elif not uuid:
        raise NoArgumentsException

    payload = ({
        'uuid': uuid,
        'key': api.apikey
    })

    if api.debug:
        api.logger.log(f"Sending a request to /player with payload: {jsonToString(payload)}", file=__name__)

    data = requests.get(f"https://api.hypixel.net/player?{jsonToString(payload)}").json()

    if api.debug:
        if len(str(data)) > 250:
            api.logger.log(f"Received a response from /player: Data too long", file=__name__)
        else:
            api.logger.log(f"Received a response from /player: {data}", file=__name__)

    if data['success'] == False:
        raise APIException(data['cause'])
    elif not 'player' in data or data['player'] == None:
        raise APIException('Non-existent player')

    if api.debug:
        api.logger.log(f"Successfully loaded player data for {uuid}", file=__name__)

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

    if api.debug:
        api.logger.log(f"Sending a request to /guild with payload: {jsonToString(payload)}", file=__name__)

    data = requests.get(f"https://api.hypixel.net/guild?{jsonToString(payload)}").json()

    if api.debug:
        if len(str(data)) > 250:
            api.logger.log(f"Received a response from /guild: Data too long", file=__name__)
        else:
            api.logger.log(f"Received a response from /guild: {data}", file=__name__)

    if data['success'] == False:
        raise APIException(data['cause'])
    elif not 'guild' in data or data['guild'] == None:
        raise APIException('Non-existent guild')

    if api.debug:
        api.logger.log(f"Successfully loaded guild data ({id}, {player}, {name})", file=__name__)

    return data

def getSkyBlockProfiles(api, uuid=None):
    payload = ({
        'uuid': uuid,
        'key': api.apikey
    })

    if api.debug:
        api.logger.log(f"Sending a request to /skyblock/profile with payload: {jsonToString(payload)}", file=__name__)

    data = requests.get(f"https://api.hypixel.net/skyblock/profiles?{jsonToString(payload)}").json()

    if api.debug:
        if len(str(data)) > 250:
            api.logger.log(f"Received a response from /skyblock/profile: Data too long", file=__name__)
        else:
            api.logger.log(f"Received a response from /skyblock/profile: {data}", file=__name__)

    if data['success'] == False:
        raise APIException(data['cause'])
    elif not 'profiles' in data or data['profiles'] == None:
        return None

    if api.debug:
        api.logger.log(f"Successfully loaded skyblock profiles for {uuid}", file=__name__)

    return data

def getSkyBlockAuctions(api, page=0):
    payload = ({
        'page': page
    })

    if api.debug:
        api.logger.log(f"Sending a request to /skyblock/auctions with payload: {jsonToString(payload)}", file=__name__)

    data = requests.get(f"https://api.hypixel.net/skyblock/auctions?{jsonToString(payload)}").json()

    if api.debug:
        if len(str(data)) > 250:
            api.logger.log(f"Received a response from /skyblock/auctions: Data too long", file=__name__)
        else:
            api.logger.log(f"Received a response from /skyblock/auctions: {data}", file=__name__)

    if data['success'] == False:
        raise APIException(data['cause'])
    elif not 'auctions' in data or data['auctions'] == None:
        return None

    if api.debug:
        api.logger.log(f"Successfully loaded skyblock auctions page {page}", file=__name__)

    return data

def getSkyBlockAuction(api, auction_uuid=None, player=None, profile=None):
    if auction_uuid:
        payload = ({
            'uuid': auction_uuid,
            'key': api.apikey
        })
    elif player:
        payload = ({
            'player': player,
            'key': api.apikey
        })
    elif profile:
        payload = ({
            'profile': profile,
            'key': api.apikey
        })
    else:
        raise NoArgumentsException

    if api.debug:
        api.logger.log(f"Sending a request to /skyblock/auction with payload: {jsonToString(payload)}", file=__name__)

    data = requests.get(f"https://api.hypixel.net/skyblock/auction?{jsonToString(payload)}").json()

    if api.debug:
        if len(str(data)) > 250:
            api.logger.log(f"Received a response from /skyblock/auction: Data too long", file=__name__)
        else:
            api.logger.log(f"Received a response from /skyblock/auction: {data}", file=__name__)

    if data['success'] == False:
        raise APIException(data['cause'])
    elif not 'auctions' in data or data['auctions'] == None:
        return None

    return data

def getSkyBlockItems(api):
    if api.debug:
        api.logger.log(f"Sending a request to /resources/skyblock/items with payload: None", file=__name__)

    data = requests.get(f"https://api.hypixel.net/resources/skyblock/items").json()

    if api.debug:
        if len(str(data)) > 250:
            api.logger.log(f"Received a response from /resources/skyblock/items: Data too long", file=__name__)
        else:
            api.logger.log(f"Received a response from /resources/skyblock/items: {data}", file=__name__)

    if data['success'] == False:
        raise APIException(data['cause'])
    elif not 'items' in data or data['items'] == None:
        return None

    if api.debug:
        api.logger.log(f"Successfully loaded skyblock items", file=__name__)

    return data