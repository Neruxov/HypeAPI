from src.hypeapi.engine import *
from datetime import datetime
from colorama import Fore

api = API("d882f221-6cc9-4f95-914c-e75750555a21", debug=True)

skyblock = api.skyblock()
skyblock_auctions = skyblock.getAuctions(page=1)

def beautiful_amount(amount):
    amount = str(int(amount))
    amount_list = []
    return_value = []
    for i in range(len(amount)):
        x = amount[-1 * (i + 1)]
        amount_list.append(x)
        if (i+1) % 3 == 0 and (i+1) != len(amount):
            amount_list.append("'")
    for i in range(len(amount_list)):
        x = amount_list[-1 * (i + 1)]
        return_value.append(x)
    return ''.join(return_value)

REFORGES = ["Stiff ", "Lucky ", "Jerry's ", "Dirty ", "Fabled ", "Suspicious ", "Gilded ", "Warped ", "Withered ", "Bulky ", "Stellar ", "Heated ", "Ambered ", "Fruitful ", "Magnetic ", "Fleet ", "Mithraic ", "Auspicious ", "Refined ", "Headstrong ", "Precise ", "Spiritual ", "Moil ", "Blessed ", "Toil ", "Bountiful ", "Candied ", "Submerged ", "Reinforced ", "Cubic ", "Warped ", "Undead ", "Ridiculous ", "Necrotic ", "Spiked ", "Jaded ", "Loving ", "Perfect ", "Renowned ", "Giant ", "Empowered ", "Ancient ", "Sweet ", "Silky ", "Bloody ", "Shaded ", "Gentle ", "Odd ", "Fast ", "Fair ", "Epic ", "Sharp ", "Heroic ", "Spicy ", "Legendary ", "Deadly ", "Fine ", "Grand ", "Hasty ", "Neat ", "Rapid ", "Unreal ", "Awkward ", "Rich ", "Clean ", "Fierce ", "Heavy ", "Light ", "Mythic ", "Pure ", "Smart ", "Titanic ", "Wise ", "Bizarre ", "Itchy ", "Ominous ", "Pleasant ", "Pretty ", "Shiny ", "Simple ", "Strange ", "Vivid ", "Godly ", "Demonic ", "Forceful ", "Hurtful ", "Keen ", "Strong ", "Superior ", "Unpleasant ", "Zealous "]

for i in skyblock_auctions:
    if i['bin']:
        name = i['item_name']

        stars = name.count('✪')
        name = name.replace('✪', '')

        start = datetime.utcfromtimestamp(int(i['start']) / 1000)
        end = datetime.utcfromtimestamp(int(i['end']) / 1000)

        reforge = None
        for x in REFORGES:
            if x in name:
                reforge = name.split(' ')[0]

        rarity = i['tier']
        if rarity == "COMMON":
            color = Fore.WHITE
        elif rarity == "UNCOMMON":
            color = Fore.GREEN
        elif rarity == "RARE":
            color = Fore.LIGHTBLUE_EX
        elif rarity == "EPIC":
            color = Fore.MAGENTA
        elif rarity == "LEGENDARY":
            color = Fore.YELLOW
        elif rarity == "MYTHIC":
            color = Fore.MAGENTA
        elif rarity == "SPECIAL":
            color = Fore.RED

        item_type = i['item_lore'].split('\n')[-1][4:]

        if 'rune' in item_type.lower() or 'furniture' in item_type.lower():
            continue

        print(f"{i['uuid']} - {color}{rarity}[{stars}✪] {name} ({item_type}){Fore.RESET} - {beautiful_amount(price)} coins - Lowest BIN: {lowestbin} - Reforge: {reforge}")