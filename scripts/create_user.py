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

    usernameList = []
    for x in usersaves:
        usernameList.append(x.replace('.json',''))
    # print(usernameList)
        
    return usernameList



def makeCharacter(newUser):
    print_slow(f"You're sleeping peacefully in your bed before a noise reaches you.\n...\nSomeone clears their throat with a quick 'Ahem!'\nYou're awake and when you open your eyes you realise...\n... you're not in your bed!\nYou're standing under a lamp overhead, the only source of light...\n\"\033[1;36;40mWelcome, {newUser}!\033[0;37;48m\" a hissy voice greets you. \nA large serpent with golden eyes and shiny scales slowly slithers into view.\n\n")
    
    while True:

        option1 = input(f"Do you run or do you prepare to fight? (run/fight)")

        print_slow(f"\033[1;36;40mFear not, I will not harm you, {newUser}! I'm here to ask you some questions.\033[0;37;48m\n")
        print_slow("\"I beg your pardon?\" you reply.\n\n")
        time.sleep(0.5)
        clear()
        print_slow("\033[1;36;40mWould you rather have a Dragon, Unicorn or a Pixie as a pet?\033[0;37;48m\n")
        select1 = input("\n 1. Dragon \n 2. Unicorn \n 3. Pixie \n \n>")
            
        if select1 == '1' : 
            while True:
                domhand = input("Are you left-handed or right-handed? (left/right)\n")   

                if domhand.lower().strip() == "left":
                    nondomhand = "right"
                    break
                elif domhand.lower().strip() == "right":
                    nondomhand = "left"
                    break
                else: 
                    print("Pick left or right!")

            favfood = input("Last, but not least! What is your favourite food?\n")

            if favfood.lower().strip() == "":
                print_slow("You did not tell me so I'm going to say it is \033[1;33;40mbanana peels\033[0;37;48m! HA!!!")
                time.sleep(0.5)
                clear()
                favfood = "banana peels"
                    

            return Player(newUser,attack=10,defence=5,magic=5,hp=100,mp=100,inventory=[],level=1,points=0,preferredhand= domhand,otherhand=nondomhand,favfood = favfood)

        elif select1 == '2' :
            while True:
                domhand = input("Are you left-handed or right-handed? (left/right)\n")   

                if domhand.lower().strip() == "left":
                    nondomhand = "right"
                    break
                elif domhand.lower().strip() == "right":
                    nondomhand = "left"
                    break
                else: 
                    print("Pick left or right!")

            favfood = input("Last, but not least! What is your favourite food?\n")

            if favfood.lower().strip() == "":
                print_slow("You did not tell me so I'm going to say it is \033[1;33;40mbanana peels\033[0;37;48m! HA!!!")
                time.sleep(0.5)
                clear()
                favfood = "banana peels"

            return Player(newUser,attack=5,defence=5,magic=10,hp=100,mp=100,inventory=[],level=1,points=0,preferredhand= domhand,otherhand=nondomhand,favfood = favfood)
        elif select1 == '3' :
            while True:
                domhand = input("Are you left-handed or right-handed? (left/right)\n")   

                if domhand.lower().strip() == "left":
                    nondomhand = "right"
                    break
                elif domhand.lower().strip() == "right":
                    nondomhand = "left"
                    break
                else: 
                    print("Pick left or right!")

            favfood = input("Last, but not least! What is your favourite food?\n")

            if favfood.lower().strip() == "":
                print_slow("You did not tell me so I'm going to say it is \033[1;33;40mbanana peels\033[0;37;48m! HA!!!")
                time.sleep(0.5)
                clear()
                favfood = "banana peels"

            return Player(newUser,attack=5,defence=10,magic=5,hp=100,mp=100,inventory=[],level=1,points=0,preferredhand= domhand,otherhand=nondomhand,favfood = favfood)
        else: print("Please select by typing in a number!")
    
    
def createNewUser():
    while True:
        clear()
        usernameList = getUserList()

        # Prompt Player to input a new username
        newUser = input("Please type a new username: \n >").strip()
            
        # Check if username contains special characters
        if newUser.isalnum():

            # Check username doesn't already exist
            if len(usernameList) > 0:
                
                lower_current_users = [x.lower() for x in usernameList]
                # print(lower_current_users)
                clear()
                
                if newUser.lower() not in lower_current_users:
                    usernameList.append(newUser)
                    print(f"Your username will be '\033[1;36;40m{newUser}\033[0;37;48m'!")
                    # print(f"Current users: {usernameList}")

                    return makeCharacter(newUser)
                else:
                    print(f"Username '{newUser}' is already taken. Please think of a different username.")
                

            # If usernameList is empty, create a new user.
            else: 
                usernameList.append(newUser)
                print(f"Your username will be '{newUser}'!")
                # print(f"Current users: {usernameList}")

                return makeCharacter(newUser) 
                
        else:
            print("Please only use letters or numbers while creating your username. Try again!")
                


