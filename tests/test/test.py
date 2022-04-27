from src.hypeapi.util.logger import Logger
from src.hypeapi.engine import *


api = API("d882f221-6cc9-4f95-914c-e75750555a21", debug=2)
player = api.getPlayer('quiu')
print(player.skywars.kills)
