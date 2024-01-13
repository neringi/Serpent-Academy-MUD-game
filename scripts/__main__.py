from create_user import * 
import time
from init import initialGame
from adhoc import *
from save_game import loadGame

from GameState import GameState
from Room import Room
from Player import Player 
from Item import Item
from Monster import Monster
from Equipment import Equipment
from NPC import NPC


gs = initialGame()

VALID_MOVES = ["left", "right", "up", "down"]

def display(info):
    if type(info) is not str:
        # print(info)
        if type(info) is list:
            for i in info:
                print(i)
    else:
        print_slow(info)

def move(location):
    if location not in VALID_MOVES:
        print_slow("Not a valid direction \n")
        display(gs.location.whereAmI())
        return
    return gs.updateLocation(location)

def updateState(action):
    tokens = action.split(None,1)
    verb = tokens[0]
    match verb:
        case "move":
            display(move(tokens[1]))
        case "who":
            display(gs.player.doCommand(action))
        case "where":
            display(gs.location.whereAmI())
        case "take":
            display(gs.takeItem(tokens[1]))
        case "list":
            if len(tokens) == 1:
                print_slow("What are you trying to list?\n Type \033[1;32;40m'LIST'\033[0;37;48m followed by \033[1;32;40mINVENTORY / EQUIPMENT / ITEMS / DIRECTIONS\033[0;37;48m.")
            elif "inventory" in tokens[1]:
                display(gs.player.listInventory())
            elif "equipment" in tokens[1]:
                display(gs.listEquipment())
            elif "items" in tokens[1]:
                display(gs.location.doCommand(action))
            elif "directions" in tokens[1]:
                display(gs.listDirections())
        case "attack":
            display(gs.attack(tokens[1]))
        case "help":
            display(gs.helpOption())
        case "equip":
            display(gs.equipItem(tokens[1]))
        case "unequip":
            if len(tokens) == 1:
                print_slow("What are you trying to unequip?\n Type \033[1;32;40m'UNEQUIP X'\033[0;37;48m to unequip X item \n Type \033[1;32;40m'UNEQUIP ALL'\033[0;37;48m to unequip everything.")
            elif "all" == tokens[1]:
                display(gs.unequipAll())
            elif tokens[1] is not None:
                display(gs.unequipItem(tokens[1]))
        case "explore":
            if len(tokens) == 1:
                print_slow("Type \033[1;32;40m'EXPLORE ROOM'\033[0;37;48m to explore the area.")
            elif "room":
                display(gs.location.doCommand(action))
        case "save":
            # Saves game to resources folder as a JSON
            display(gs.saveGame())
        case "quit":
            # If User wants to quit, takes them back to menu
            quit = input("Are you sure you want to quit? Any progress that was not saved will be lost. (y/n)")
            if quit.lower().strip() == "y":
                clear()
                return True
        case "use":
            if len(tokens) == 1:
                print_slow("What are you trying to use? Type \033[1;32;40m''USE'\033[0;37;48m followed by the name of the item.\n")
            elif len(tokens) > 1:
                display(gs.useItem(tokens[1]))
        case "talk":
            if len(tokens) == 1:
                print_slow("Who are you trying to talk to? Type 'TALK' followed by the name of who you are trying to talk to!")
            elif len(tokens) > 1:
                display(gs.talkNPC(tokens[1]))
                




def userMoves():
    while True:
        # print_slow(f"You are in {gs.location.name}")
        userInput = input("\nYour Move:")
        userInput = userInput.lower()
        if userInput.strip() == "":
            print_slow("You have to do something! \nType 'HELP' to see a list of actions you can take!")
        else:
            if userInput in ("left", "right","up", "down"):
                print_slow("If you want to travel, use keyword 'MOVE' before choosing a direction")
                # validate input 
                # is a valid command, is an actionable verb, is composed of verb + noun
            shouldexit = updateState(userInput)
            if shouldexit:
                return




        
# castle ref
# https://www.asciiart.eu/buildings-and-places/castles

# castle = """
#                            o                    
#                        _---|         _ _ _ _ _ 
#                     o   ---|     o   ]-I-I-I-[ 
#    _ _ _ _ _ _  _---|      | _---|    \ ` ' / 
#    ]-I-I-I-I-[   ---|      |  ---|    |.   | 
#     \ `   '_/       |     / \    |    | /^\| 
#      [*]  __|       ^    / ^ \   ^    | |*|| 
#      |__   ,|      / \  /    `\ / \   | ===| 
#   ___| ___ ,|__   /    /=_=_=_=\   \  |,  _|
#   I_I__I_I__I_I  (====(_________)___|_|____|____
#   \-\--|-|--/-/  |     I  [ ]__I I_I__|____I_I_| 
#    |[]      '|   | []  |`__  . [  \-\--|-|--/-/  
#    |.   | |' |___|_____I___|___I___|---------| 
#   / \| []   .|_|-|_|-|-|_|-|_|-|_|-| []   [] | 
#  <===>  |   .|-=-=-=-=-=-=-=-=-=-=-|   |    / \  
#  ] []|`   [] ||.|.|.|.|.|.|.|.|.|.||-      <===> 
#  ] []| ` |   |/////////\\\\\\\\\\.||__.  | |[] [ 
#  <===>     ' ||||| |   |   | ||||.||  []   <===>
#   \T/  | |-- ||||| | O | O | ||||.|| . |'   \T/ 
#    |      . _||||| |   |   | ||||.|| |     | |
# ../|' v . | .|||||/____|____\|||| /|. . | . ./
# .|//\............/...........\........../../\\\

            
school = print('''     
      
    |>>>                                                      |>>>
    |                    |>>>          |>>>                   |
    *                     |             |                     *
   / \                    *             *                    / \.
  /___\                 _/ \           / \_                 /___\.
  [   ]                |/   \_________/   \|                [   ]
  [ I ]                /     \       /     \                [ I ]
  [   ]_ _ _          /       \     /       \          _ _ _[   ]
  [   ] U U |        {#########}   {#########}        | U U [   ]
  [   ]====/          \=======/     \=======/          \====[   ]
  [   ]    |           |   I |_ _ _ _| I   |           |    [   ]
  [___]    |_ _ _ _ _ _|     | U U U |     |_ _ _ _ _ _|    [___]
  \===/  I | U U U U U |     |=======|     | U U U U U | I  \===/
   \=/     |===========| I   | + W + |   I |===========|     \=/
    |  I   |           |     |_______|     |           |   I  |
    |      |           |     |||||||||     |           |      |
    |      |           |   I ||vvvvv|| I   |           |      |
_-_-|______|-----------|_____||     ||_____|-----------|______|-_-_
   /________\         /______||     ||______\         /________\.
   
    ''')


# Welcome message when starting the game
print_slow("V1.0 Jan 2024\n")
print_slow("Created by Mesha and Neringa\n")
print(school)
print_slow("Welcome to the Serpent Academy!\n\n")
time.sleep(1)

reply = input("Would you like to see the game menu? (y/n) \n>").lower().strip()

if reply == "y":
    time.sleep(.5)

    clear()
    print_slow("Good, let's begin!")
    time.sleep(1)
    clear()

    while True:
        print_slow("Please select from the following options:")
        print("\n 1. Create New Game \n 2. Load Game \n 3. Leaderboard \n 'q' to Quit")
        option = input("\n>")
        if str(option.strip()) == '1':
            player = createNewUser()
            gs = initialGame()
            gs.player = player
            
            userMoves()
            
        elif str(option.strip()) == '2':
            clear()
            print("Let's load your game from save file.")
            try:
                gs = loadGame()
            except:
                continue

            userMoves()

        elif str(option).strip() == '3':
            print("Leaderboard!")
        elif str(option).strip() == 'q':
            print("Bye!")
            break
        else: print("Invalid choice! \nPlease type '1' for New Game, \n'2' to load a game or \n'3' for the leaderboard.")

else: 
    print("That's too bad! Maybe next time.")
