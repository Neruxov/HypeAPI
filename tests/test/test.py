from src.hypeapi.engine import *

api = API("d882f221-6cc9-4f95-914c-e75750555a21")

player = api.player(uuid="164bd0ea-a46e-4db1-8278-dd172409647a")
print(player.playerName)