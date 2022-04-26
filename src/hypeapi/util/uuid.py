import requests


def NameToUUID(name):
    try:
        data = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}").json()
    except:
        return None
    return data['id']


def UUIDToName(uuid):
    try:
        data = requests.get(
            f"https://sessionserver.mojang.com/session/minecraft/profile/{uuid.replace('-', '')}").json()
    except:
        return None
    return data['name']
