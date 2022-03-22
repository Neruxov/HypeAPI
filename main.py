import requests

class API:
    def __init__(self, apikey):
        self.apikey = apikey

    def player(self, name):
        data = requests.get(f"https://api.hypixel.net/player?name={name}&key={self.apikey}")
        return Player()

class Player:
    def __init__(self, data):
        self.data = data