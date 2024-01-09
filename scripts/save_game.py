import os.path
import json
from Player import Player
from Equipment import Equipment
from Room import Room
from Item import Item
from Monster import Monster
# from example import *
from init import gs

# dirname = os.path.dirname(os.path.dirname(__file__))
# # print(dirname)
# savefilepath = dirname + '/resources/savefile.json'
# # print(savefilepath)

# file_exists = os.path.isfile(savefilepath)
# # print(file_exists)

# def saveGame():
#     # print(player.get_dict())
#     if file_exists:
#         with open(savefilepath, 'w', encoding='utf-8') as f: 
#             f.write(gs.toJSON())
#     else:
#         print("Something went wrong. Could not save game, try again")


# saveGame()



def loadGame():
    user = input("What is your username?").lower().strip()
    dirname = os.path.dirname(os.path.dirname(__file__))
    # print(dirname)
    usersavepath = dirname + '/resources/' + user +'.json'
    print(usersavepath)

    file_exists = os.path.isfile(usersavepath)
    if file_exists:
        print("File loading...")

        # Opening JSON file
        f = open(usersavepath)

        # returns JSON object as 
        # a dictionary
        loaded_game = json.load(f)


        # Load Equipment
        gs.equipment = Equipment()

        # Load equipped items
        for key, value in loaded_game["equipment"].items():
            if value != None:
                setattr(gs.equipment, key, Item(**value))
        # print(gs.equipment.dominanthand)
        # print(loaded_game)

        # Load Current Location
        gs.location = Room(**loaded_game["location"])
        # print(gs.location)

        # Load Player
        gs.player = Player(**loaded_game["player"])
        # print(gs.player.username)
        # print(gs.player.inventory
        items = []
        # Load items in player's inventory
        for item in gs.player.inventory:
            items.append(Item(**item))
            # print(f" Item is {item}")
            
        gs.player.items = items

        # Load Rooms
        rooms = {}
        for key, room in loaded_game["rooms"].items():

            # Load items, monsters and npcs in rooms
            items = {}
            monsters = {}
            # npcs = {}

            for itemkey, item in room["items"].items():
                items[itemkey] = Item(**item)
                # print(f" Itemkey is {itemkey}")
                # print(items)

            for monsterkey, monster in room["monster"].items():
                monsters[monsterkey] = Monster(**monster)

            
            # for npckey, npc in room["npc"].items():
            #     npcs[npckey] = NPC(**npc)
        
            rooms[key] = Room(**room)

            rooms[key].items = items
            rooms[key].monster = monsters
            # rooms[key].npc = npcs


            print(rooms[key])
            print(f"room is {key}")
            print(f"Room items are {rooms[key].items}")
            print(f"Room monsters are {rooms[key].monster}")

            
        # Closing file
        f.close()       
    else:
        print("Sorry, there are no save files for that username. \n Check the username is correct or create a new game!")

loadGame()