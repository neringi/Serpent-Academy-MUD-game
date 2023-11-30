from create_user import * 
import time



# Welcome message when starting the game
print("Welcome to the Serpent Academy!")
print("Created by Mesha and Neringa")

while True:
    reply = input("Would you like to see the game menu? (y/n) \n>").lower().strip()

    if reply == "y":
        time.sleep(.5)
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
        break