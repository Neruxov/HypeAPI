from src.hypeapi.engine import *
from datetime import datetime
from colorama import Fore

api = API("d882f221-6cc9-4f95-914c-e75750555a21", debug=True)
player = api.player('quiu')
print(player.getPlayerName())



