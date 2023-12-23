import time

class lucarialake: #will fix this with self etc - ive just been testing how it runs
    directions = ["R", "L", "FW", "BW"]
    choice = ["Yes", "No"]
    #weapon = false or true depending on if they have one - spells can be used if mage
    print("You walk on the path towards the grand lake in the courtyard of the academy")
    time.sleep(1)
    print("You come to a crossroads. Which way would you like to go?")
    userinput = ""
    while userinput not in directions:
        print("Please choose: right(R),left(L),forwards(FW) or backwards(BW)")
        userinput = input("Choose a direction: ")
        if userinput == "R":
            print("As you are walking a thick mist begins covering the path...")
            time.sleep(1)
            print("Continuing through the fog your visibility drops to mere feet ahead")
            time.sleep(1)
            print("After a few minutes you come to a clearing and you see a figure up ahead on the dock")
            time.sleep(1)
            print("Would you like to advance towards the figure?")
        choiceinput = ""
        while choiceinput not in choice:
            print("Please choose: Yes or No")
            choiceinput = input()
            if choiceinput == "Yes":
                print("You cautiously walk towards the figure")
                time.sleep(1)
                print("As you get closer to the figure, the figure looks in your direction")
                time.sleep(1)
                print("")
            elif choiceinput == "No":
                print("You decide to head away from where the figure is and continue walking")
                time.sleep(1)
                print("You reach a dead end, and walk back towards the crossroads")
                time.sleep(1)
                print("Which way would you like to head?")
                userinput = input("Choose a direction: ")
            else:
                print("Please choose a valid option")

            print()
        #elif userinput == "L":
            #print("")
        #elif userinput == "FW":
            #print("")
        #elif userinput == "BW":
            #print("")
        #else:
            #print("Please enter a valid option.")
