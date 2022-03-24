import requests

from src.hypeapi.engine import *

api = API("d882f221-6cc9-4f95-914c-e75750555a21")
Player = api.player(name="theliryzz")
print(Player.getBuildBattle().wins)
