from src.hypeapi import API

api = API("d882f221-6cc9-4f95-914c-e75750555a21", debug=True)
player = api.getPlayer('quiu')
print(player.skywars.kills)