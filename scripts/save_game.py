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
            f.write(gs.toJSON())
    else:
        print("Something went wrong. Could not save game, try again")


# saveGame()

    
