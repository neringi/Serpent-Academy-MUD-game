import os.path
import json
from Player import Player
# from example import *
from init import gs

dirname = os.path.dirname(os.path.dirname(__file__))
# print(dirname)
savefilepath = dirname + '/resources/savefile.json'
# print(savefilepath)

file_exists = os.path.isfile(savefilepath)
# print(file_exists)

def saveGame():
    # print(player.get_dict())
    if file_exists:
        with open(savefilepath, 'w', encoding='utf-8') as f: 
            # players_json = f.read()

            # players = json.loads(players_json)
            # players.append(player.get_dict())

        # with open(savefilepath, 'w', encoding='utf-8') as f:
            f.write(gs.toJSON())
    else:
        with open(savefilepath, 'w', encoding='utf-8') as f: 
            json.dump({}, f, ensure_ascii=False, indent=4)


saveGame()

    
