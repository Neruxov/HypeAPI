from hypeapi import API  # import HypeAPI

api = API('your_api_key')  # create an API object, used to send requests to the API

player_uuid = input("Please enter a player UUID: ")  # get a player UUID from the user
player = api.getPlayer(uuid=player_uuid)  # get a player object from the API

print('Options:\n - 1. Level \n - 2. Display Name \n - 3. Skywars Kills \n - 4. Bedwars Wins')  # print the options
option = int(input("Please enter an option: "))  # get an option from the user

# !!! IMPORTANT !!! This example was written using Python 3.10, so you have a thing called "match" and "case". If you
# use any version lower than 3.10, you will have to use "if", "else", "elif" with every option.
# !!! IMPORTANT !!!

match option:
    case 1:
        print(f'Level: {player.level}')  # print the player's level
    case 2:
        print(f'Display Name: {player.displayName}')  # print the player's display name
    case 3:
        print(f'Skywars Kills: {player.skywars.kills}')  # print the player's skywars kills
    case 4:
        print(f'Bedwars Wins: {player.bedwars.wins}')  # print the player's bedwars wins
