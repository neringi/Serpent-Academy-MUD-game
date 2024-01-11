import time
import os.path
from adhoc import *
from Player import *


# Check save files in resources folder and save all usernames in a list
def getUserList():
    savesfolder = os.path.dirname(os.path.dirname(__file__)) + '/resources'
    # print(savesfolder)
    
    usersaves = os.listdir(savesfolder) 

    usersaves.remove("ascii")
    usersaves.remove("serpent_academy_leaderboard.csv")

    usernameList = []
    for x in usersaves:
        usernameList.append(x.replace('.json',''))
    # print(usernameList)
        
    return usernameList



def makeCharacter(newUser):
    print_slow(f"You're sleeping peacefully in your bed before a noise reaches you.\n...\nSomeone clears their throat with a quick 'Ahem!'\nYou're awake and when you open your eyes you realise...\n... you're not in your bed!\nYou're standing under a lamp overhead, the only source of light...\n\"Welcome, {newUser}!\" a hissy voice greets you. \nA large serpent with golden eyes and shiny scales slowly slithers into view.\n\n")
    
    while True:

        option1 = input(f"Do you run or do you prepare to fight? (run/fight)")

        print_slow(f"Fear not, I will not harm you, {newUser}! I'm here to ask you some questions.\n")
        print_slow("\"I beg your pardon?\" you reply.\n\n")

        print_slow("What are you looking forward to most at the Serpent Academy?")
        select1 = input("\n 1. Learning to fight \n 2. Learning magic \n 3. What are you talking about?\n 'q' to Start Over \n>")
            
        if select1 == '1' : 
            while True:
                domhand = input("Are you left-handed or right-handed? (left/right)")   

                if domhand.lower().strip() == "left":
                    nondomhand = "right"
                    break
                elif domhand.lower().strip() == "right":
                    nondomhand = "left"
                    break
                else: 
                    print("Pick left or right!")

            return Player(newUser,attack=10,defence=5,magic=5,hp=100,mp=100,inventory=[],level=1,points=0,preferredhand= domhand,otherhand=nondomhand)

        elif select1 == '2' :
            while True:
                domhand = input("Are you left-handed or right-handed? (left/right)")   

                if domhand.lower().strip() == "left":
                    nondomhand = "right"
                    break
                elif domhand.lower().strip() == "right":
                    nondomhand = "left"
                    break
                else: 
                    print("Pick left or right!")

            return Player(newUser,attack=5,defence=5,magic=10,hp=100,mp=100,inventory=[],level=1,points=0,preferredhand= domhand,otherhand=nondomhand)
        elif select1 == '3' :
            while True:
                domhand = input("Are you left-handed or right-handed? (left/right)")   

                if domhand.lower().strip() == "left":
                    nondomhand = "right"
                    break
                elif domhand.lower().strip() == "right":
                    nondomhand = "left"
                    break
                else: 
                    print("Pick left or right!")

            return Player(newUser,attack=5,defence=10,magic=5,hp=100,mp=100,inventory=[],level=1,points=0,preferredhand= domhand,otherhand=nondomhand)
        elif select1 == 'q':
            print('Quitting...')
            break
        else: print("Please select by typing in a number, or type 'q' to Quit")
    
    
def createNewUser():
    while True:
        clear()
        usernameList = getUserList()

        # Prompt Player to input a new username
        newUser = input("Please type a new username: \n >").strip()
            
        # Check if username contains special characters
        if newUser.isalnum():
            # Check usernameList is not empty
            if len(usernameList) > 0:
                
                lower_current_users = [x.lower() for x in usernameList]
                print(lower_current_users)

                if newUser.lower() not in lower_current_users:
                    usernameList.append(newUser)
                    print(f"Your username will be '{newUser}'!")
                    # print(f"Current users: {usernameList}")

                    return makeCharacter(newUser)
                else:
                    print(f"Username '{newUser}' is already taken. Please think of a different username.")
                

            # If usernameList is empty, create a new user.
            else: 
                usernameList.append(newUser)
                print(f"Your username will be '{newUser}'!")
                # print(f"Current users: {usernameList}")

                # createPassword()
                return makeCharacter(newUser) 
                
        else:
            print("Please only use letters or numbers while creating your username. Try again!")
                


