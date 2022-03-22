from engine import *

api = API("d882f221-6cc9-4f95-914c-e75750555a21")

player = api.player(uuid="f12dc326-df8a-468c-891d-b3b1d68056c7")
print(player.getNetworkLevel())