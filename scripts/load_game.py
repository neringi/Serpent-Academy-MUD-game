import os.path
import json
from Player import Player
from Equipment import Equipment
from Room import Room
from Item import Item
from Monster import Monster
from NPC import NPC
# from example import *
from GameState import GameState
from adhoc import *


def loadGame():
    user = input("What is your username?").lower().strip()
    dirname = os.path.dirname(os.path.dirname(__file__))
    # print(dirname)
    usersavepath = dirname + '/resources/' + user +'.json'
    # print(usersavepath)

    file_exists = os.path.isfile(usersavepath)
    # invert if statement
    if not file_exists:
        print("Sorry, there are no save files for that username. \n Check the username is correct or create a new game!")
        raise Exception("No saved file")
    print_slow("File loading...")

    # Opening JSON file
    # f = open(usersavepath)
    with open(usersavepath) as f:
      loaded_game = json.load(f)

    # returns JSON object as 
    # a dictionary
    # loaded_game = json.load(f)

    gs = GameState()

    # Load Equipment
    gs.equipment = Equipment()
    # Load equipped items
    dh = loaded_game["equipment"]["dominanthand"]
    nh = loaded_game["equipment"]["nondominanthand"]
    gs.equipment.dominanthand = Item(**dh) if dh is not None else None
    gs.equipment.nondominanthand = Item(**nh) if nh is not None else None
    # print(gs.equipment.dominanthand)
    # print(loaded_game)

    # Set current location room name
    startinglocation = loaded_game["location"]["name"]

    # Load Player
    gs.player = Player(**loaded_game["player"])
    # print(gs.player.username)
    # print(gs.player.inventory)
    playeritems = []

    # Load items in player's inventory
    for playeritem in gs.player.inventory:
        playeritems.append(Item(**playeritem))
        # print(f" Item is {item}")
        
    gs.player.inventory = playeritems

    # Load Rooms
    rooms = {}
    for key, room in loaded_game["rooms"].items():

        # Load items, monsters and npcs in rooms
        items = {}
        monsters = {}
        npcs = {}

        # Load Items in Rooms
        for itemkey, item in room["items"].items():
            items[itemkey] = Item(**item)
            # print(f" Itemkey is {itemkey}")
            # print(items)

        # Load Monsters in Rooms
        for monsterkey, monster in room["monster"].items():
            monsters[monsterkey] = Monster(**monster)
            # print(type(monsters[monsterkey]))
            # print(monsters[monsterkey])
            loot = {}

        # Load Items in Monsters
            for lootkey, l in monster["items"].items():
                loot[lootkey] = Item(**l)
        
            monsters[monsterkey].items = loot


        # Load NPCs in Rooms
        for npckey, npc in room["npc"].items():
            npcs[npckey] = NPC(**npc)

            loot = {}
            for lootkey, l in npc["items"].items():
                loot[lootkey] = Item(**l)
        
            npcs[npckey].items = loot
    
        rooms[key] = Room(**room)

        rooms[key].items = items
        rooms[key].monster = monsters
        rooms[key].npc = npcs
        # for m in rooms[key].monster:
        #     print(type(m))
        #     print((m))
        # rooms[key].npc = npcs

        
        # print(rooms[key])
        # print(f"room is {key}")
        # print(f"Room items are {rooms[key].items}")
        # print(f"Room monsters are {rooms[key].monster}")
    # print(rooms.keys())

    gs.location = rooms[startinglocation]
    gs.rooms = rooms
    time.sleep(2)
    clear()
    print_slow(f"Welcome back, {gs.player.username}! \nUse \033[1;32;40m'HELP'\033[0;37;48m option to remind you how to play. \n")
    return gs 
     
