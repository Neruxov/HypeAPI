import requests

def NameToUUID(name):
    data = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}").json()
    return data['id']

def UUIDToName(uuid):
    data = requests.get(f"https://sessionserver.mojang.com/session/minecraft/profile/{uuid.replace('-', '')}").json()
    return data['name']