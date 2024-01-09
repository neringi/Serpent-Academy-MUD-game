from create_user import * 
# from resources.ascii.castle import *
import time
from init import *
from adhoc import *

# def display(story, time):
#     for s in story:
#         print(s)
#         time.sleep(time)



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
            if "inventory" in tokens[1]:
                display(gs.player.listInventory())
            if "equipment" in tokens[1]:
                display(gs.listEquipment())
            if "items" in tokens[1]:
                display(gs.location.doCommand(action))
            if "directions" in tokens[1]:
                display(gs.location.doCommand(action))
        case "attack":
            display(gs.attack(tokens[1]))
        case "help":
            display(gs.helpOption())
        case "equip":
            display(gs.equipItem(tokens[1]))
        case "unequip":
            if len(tokens) == 1:
                print_slow("What are you trying to unequip?\n Type 'UNEQUIP X' to unequip X item \n Type 'UNEQUIP ALL' to unequip everything.")
            elif "all" == tokens[1]:
                display(gs.unequipAll())
            elif tokens[1] is not None:
                display(gs.unequipItem(tokens[1]))
        case "explore":
            if "room" in tokens[1]:
                display(gs.location.doCommand(action))
        case "save":
            display(gs.saveGame())


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
            updateState(userInput)





        
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


# """

# Welcome message when starting the game
print_slow("V1.0 Jan 2024\n")
print_slow("Created by Mesha and Neringa\n")
# print(castle)
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
            createNewUser()

            
        elif str(option.strip()) == '2':
            print("Let's load your game from save file.")


        elif str(option).strip() == '3':
            print("Leaderboard!")
        elif str(option).strip() == 'q':
            print("Bye!")
            break
        else: print("Invalid choice! \nPlease type '1' for New Game, \n'2' to load a game or \n'3' for the leaderboard.")

else: 
    print("That's too bad! Maybe next time.")
