from hypeapi import API # import HypeAPI

api = API('your_api_key') # create an API object, used to send requests to the API
player = api.getPlayer(name="Neruxov") # get a Player object
print(player.displayname) # print the player's displayname