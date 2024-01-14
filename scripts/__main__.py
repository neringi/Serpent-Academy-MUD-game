from create_user import * 
import time
from init import initialGame
from adhoc import *
from save_game import loadGame
from figures import *

from GameState import GameState
from Room import Room
from Player import Player 
from Item import Item
from Monster import Monster
from Equipment import Equipment
from NPC import NPC
from Leaderboard import Leaderboard
import traceback

gs = initialGame()
lb = Leaderboard("resources/leaderboard.json")

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
            # moves location
            if len(tokens) == 1:
                print_slow("You jump around in one spot. Try typing \033[1;32;40m'MOVE LEFT'\033[0;37;48m")
            else:
                display(move(tokens[1]))

        case "who":
            # lists user stats
            display(gs.player.doCommand(action))

        case "where":
            # lists current location
            display(gs.location.whereAmI())

        case "take":
            # picks up a specified item in the room
            if len(tokens) == 1:
                print_slow("What are you trying to take? Type  \033[1;32;40m'TAKE'\033[0;37;48m followed by name of the item")
            else:
                display(gs.takeItem(tokens[1]))

        case "list":
            # Lists items/weapons/directions
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
            # deals damage to a monster HP (and player HP)
            if len(tokens) == 1:
                print_slow("Who are you trying to attack? \n Type \033[1;32;40m'ATTACK'\033[0;37;48m followed by the name of the monster.")
            else:
                attack = gs.attack(tokens[1])
                if attack == "endgame":
                    clear()
                    print("Congratulations! You beat the game!")
                    input("Press ENTER to go back to the main menu!")
                    return True
                if attack == "dead":
                    clear()
                    print("You died! The game beat you!")
                    input("Press ENTER to go back to the main menu!")
                    return True
                else: 
                    display(attack)


            

        case "help":
            # HELP option
            display(gs.helpOption())
        
        case "hint":
            # HINT option - same as EXPLORE ROOM
            display(gs.location.doCommand("exploreroom"))
                    
        case "equip":
            # Equips specified item
            if len(tokens) == 1:
                print_slow("What are you trying to equip?\n Type \033[1;32;40m'EQUIP'\033[0;37;48m followed by name of the item.")
            else:
                display(gs.equipItem(tokens[1]))

        case "unequip":
            # Unequips specified item
            if len(tokens) == 1:
                print_slow("What are you trying to unequip?\n Type \033[1;32;40m'UNEQUIP X'\033[0;37;48m to unequip X item \n Type \033[1;32;40m'UNEQUIP ALL'\033[0;37;48m to unequip everything.")
            elif "all" == tokens[1]:
                display(gs.unequipAll())
            elif tokens[1] is not None:
                display(gs.unequipItem(tokens[1]))

        case "explore":
            # Lists any items, NPCs or monsters in the room
            if len(tokens) == 1:
                print_slow("Type \033[1;32;40m'EXPLORE ROOM'\033[0;37;48m to explore the area.")
            elif "room":
                display(gs.location.doCommand(action))

        case "save":
            # Saves game to resources folder as a JSON
            display(gs.saveGame())

        case "quit":
            # If User wants to quit, takes them back to menu
            quit = input("Are you sure you want to quit? (y/n)")
            if quit.lower().strip() == "y":
                clear()
                return True
            
        case "use":
            # Can use potions
            if len(tokens) == 1:
                print_slow("What are you trying to use? Type \033[1;32;40m''USE'\033[0;37;48m followed by the name of the item.\n")
            elif len(tokens) > 1:
                display(gs.useItem(tokens[1]))

        case "talk":
            # Talk to NPCs
            if len(tokens) == 1:
                print_slow("Who are you trying to talk to? Type 'TALK' followed by the name of who you are trying to talk to!")
            elif len(tokens) > 1:
                display(gs.talkNPC(tokens[1]))

        case "favouritefood":
            # Prints user input for favourite food
            display(gs.player.favFood())
                




def userMoves():
    while True:
        
        userInput = input("\nYour Move:")
        clear()
        print(f"\nYour Move: '{userInput}'")
        userInput = userInput.lower()
        if userInput.strip() == "":
            print_slow("You have to do something! \nType '\033[1;32;40mHELP\033[0;37;48m' to see a list of actions you can take!")
        else:
            if userInput in ("left", "right","up", "down"):
                print_slow("If you want to travel, use keyword '\033[1;32;40mMOVE\033[0;37;48m' before choosing a direction")
                # validate input 
                # is a valid command, is an actionable verb, is composed of verb + noun
            shouldexit = updateState(userInput)
            if shouldexit:
                gs.saveGame()
                lb.save_score(gs.player)
                display("Saved score to leaderboard\n")
                print(lb)
                return


# Welcome message when starting the game
clear()
print_slow("V1.0 Jan 2024\n")
print_slow("Created by Mesha and Neringa\n")
school()
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
            
            print_slow("Type actions to play the game! Try typing '\033[1;32;40mHELP\033[0;37;48m' if you're stuck!")
            userMoves()
            
        elif str(option.strip()) == '2':
            clear()
            print("Let's load your game from save file.")
            try:
                gs = loadGame()
            except Exception as e:
                # print(repr(e))
                traceback.print_exc()
                continue
            
            clear()
            print_slow("Type actions to play the game! Try typing '\033[1;32;40mHELP\033[0;37;48m' if you're stuck!")

            userMoves()

        elif str(option).strip() == '3':

            clear()
            print(lb)
            input("Type ENTER to return to the Main Menu.")
            clear()


        elif str(option).strip() == 'q':
            print("Bye!")
            break

        else: print("Invalid choice! \nPlease type '1' for New Game, \n'2' to load a game or \n'3' for the leaderboard.")

else: 
    print("That's too bad! Maybe next time.")
