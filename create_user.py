import time

usernameList = []


# Consider using maskpass + hashing and salting of the password? 
# import maskpass
# pwd = maskpass.advpass()  # masking the password
# print('Password : ', pwd)

def checkSpecialChar(input):
    # Define special characters which are not allowed
    special_characters = " !\"#$%&'()*+,-./:;<=>?@[\]_^`{|}~"

     # Check if contains special characters
    if any(c in special_characters for c in input):
        if len(input) > 0:
            return True
    
def createPassword():
    try:
        while True:
        # Prompt Player to input a new password
            newPass = input("Please type a password. Only use letters or numbers: \n >")
        
            # Check for special characters
            if checkSpecialChar(newPass):
                print("Please only use letters or numbers while creating your password. Try again!")
            else: 
                # Prompt Player to input the password again
                matchPass = input("Please repeat your password!\n>")

                if newPass == matchPass:
                    print("Password created! Woohoo!")
                    break
                else: 
                    print("The passwords you have entered did not match. Try again!")
    except Exception as e:
        print(e)

def makeCharacter(newUser):
    try:
        print("You're sleeping peacefully in your bed before a noise reaches you.")
        time.sleep(2)
        print("...")
        time.sleep(2)
        print("Someone clears their throat with a quick 'Ahem!'")
        time.sleep(1)
        print("You're awake and when you open your eyes you realise...")
        time.sleep(1)
        print("... you're not in your bed!")
        time.sleep(1)
        print("...")
        time.sleep(3)
        print("You're standing under a lamp overhead, the only source of light...")
        time.sleep(2)
        print(f"\"Welcome, {newUser}!\" a hissy voice greets you.")
        time.sleep(2)
        print("A large serpent with golden eyes and shiny scales slowly slithers into view.")
        time.sleep(1)
        while True:

            option1 = input(f"Do you run or do you prepare to fight? (run/fight)")

            if option1.lower().strip() == "run":
                time.sleep(3)
                char1 = "careful"
                print(char1)

                print(f"Fear not, I will not harm you, {newUser}! I'm here to ask you if you're ready.")
                print("\"I bed your pardon?\" you reply.")

                print("The serpent asks you.")
                while True: 
                        
                    print("What are you looking forward to most at the Serpent Academy?")
                    select1 = input("\n 1. Learning to fight \n 2. Learning magic \n 3. What are you talking about?\n 'q' to Start Over \n>")
                        
                    if select1 == '1' : 
                        char_str = 10
                        char_mgc = 5
                        char_int = 5
                        break
                    elif select1 == '2' :
                        char_str = 5
                        char_mgc = 10
                        char_int = 5
                        break
                    elif select1 == '3' :
                        char_str = 5
                        char_mgc = 5
                        char_int = 10
                        break
                    elif select1 == 'q':
                        print('Starting over...')
                        break
                    else: print("Please select by typing in a number, or type 'q' to Quit")

            elif option1.lower().strip() == "fight":
                time.sleep(3)
                char1 = "bold"
                print(char1)

                print(f"Fear not, I will not harm you, {newUser}! I'm here to ask you if you're ready.")
                print("\"I bed your pardon?\" you reply.")

                print("To be continued...")
            else: 
                print("You're so shocked, you couldn't decide on how to act!")
                time.sleep(3)
                char1 = "careful"
                print(char1)

                print(f"Fear not, I will not harm you, {newUser}! I'm here to ask you if you're ready.")
                print("\"I bed your pardon?\" you reply.")

                print("To be continued...")

            



    except Exception as e:
        print(e)
    
    
def createNewUser():
    try:
        while True:

            # Prompt Player to input a new username
            newUser = input("Please type a new username: \n >").strip()
                
            # Check if username contains special characters
            if checkSpecialChar(newUser):
                print("Please only use letters or numbers while creating your username. Try again!")    
            else:   
                try: 
                        # Check usernameList is not empty
                        if len(usernameList) > 0:
                            
                            lower_current_users = [x.lower() for x in usernameList]
                            print(lower_current_users)

                            if newUser.lower() not in lower_current_users:
                                usernameList.append(newUser)
                                print(f"Username '{newUser}' created!")
                                print(f"Current users: {usernameList}")

                                createPassword()

                                makeCharacter(newUser)

                            elif newUser.lower() in lower_current_users:
                                print(f"Username '{newUser}' is already taken. Please think of a different username.")
                            else:
                                print("Something went wrong there! Sorry about that!")
                                break

                        # If usernameList is empty, create a new user.
                        else: 
                            usernameList.append(newUser)
                            print(f"Username '{newUser}' created! Yay!")
                            print(f"Current users: {usernameList}")

                            createPassword()
                            makeCharacter(newUser)

                except Exception as e:
                    print(e)   

    except Exception as e:
        print(e)


