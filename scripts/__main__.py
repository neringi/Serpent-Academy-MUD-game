from create_user import * 
# from resources.ascii.castle import *
import time

from adhoc import *





# def display(story, time):
#     for s in story:
#         print(s)
#         time.sleep(time)
        
# castle ref
# https://www.asciiart.eu/buildings-and-places/castles

castle = """
                           o                    
                       _---|         _ _ _ _ _ 
                    o   ---|     o   ]-I-I-I-[ 
   _ _ _ _ _ _  _---|      | _---|    \ ` ' / 
   ]-I-I-I-I-[   ---|      |  ---|    |.   | 
    \ `   '_/       |     / \    |    | /^\| 
     [*]  __|       ^    / ^ \   ^    | |*|| 
     |__   ,|      / \  /    `\ / \   | ===| 
  ___| ___ ,|__   /    /=_=_=_=\   \  |,  _|
  I_I__I_I__I_I  (====(_________)___|_|____|____
  \-\--|-|--/-/  |     I  [ ]__I I_I__|____I_I_| 
   |[]      '|   | []  |`__  . [  \-\--|-|--/-/  
   |.   | |' |___|_____I___|___I___|---------| 
  / \| []   .|_|-|_|-|-|_|-|_|-|_|-| []   [] | 
 <===>  |   .|-=-=-=-=-=-=-=-=-=-=-|   |    / \  
 ] []|`   [] ||.|.|.|.|.|.|.|.|.|.||-      <===> 
 ] []| ` |   |/////////\\\\\\\\\\.||__.  | |[] [ 
 <===>     ' ||||| |   |   | ||||.||  []   <===>
  \T/  | |-- ||||| | O | O | ||||.|| . |'   \T/ 
   |      . _||||| |   |   | ||||.|| |     | |
../|' v . | .|||||/____|____\|||| /|. . | . ./
.|//\............/...........\........../../\\\


"""

# Welcome message when starting the game
print("V1.0 Dec 2023")
print("Created by Mesha and Neringa")
# print(castle)
# print("Welcome to the Serpent Academy!")
# time.sleep(2)

reply = input("Would you like to see the game menu? (y/n) \n>").lower().strip()

if reply == "y":
    time.sleep(.5)

    clear()
    print("Good, let's begin!")

    while True:
        time.sleep(1)
        print("Please select from the following options:")
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
