from src.hypeapi.engine import *

api = API("d882f221-6cc9-4f95-914c-e75750555a21")
player = api.player(uuid="fcd4a146-cb09-4d87-9e84-80f6aa35603f")
print(player.getGuild().getGuildPlayer(uuid=player.uuid).joinDate)