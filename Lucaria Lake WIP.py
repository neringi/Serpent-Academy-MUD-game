import time
import courtyard


class LucariaLake:
    def __init__(self):
        self.directions = ["R", "L", "FW", "BW"]
        self.choice = ["Yes", "No"]
        self.weapon = True
    def explore(self):
        print("You walk on the path towards the grand lake in the courtyard of the academy")
        time.sleep(1)

    def crossroads(self):
        print("You come to a crossroads. Which way would you like to go?")
        userinput = ""
        while userinput not in self.directions:
            userinput = input("Please choose: right(R),left(L),forwards(FW) or backwards(BW)")
        if userinput == "R":
            self.mist()
        elif userinput == "L":
            self.boathouse()
        elif userinput == "FW":
            self.loch()
        elif userinput == "BW":
            self.courtyard()
        else:
            return "please enter a valid direction"
    def mist(self):
            print("As you are walking a thick mist begins covering the path...")
            time.sleep(2)
            print("Continuing through the fog your visibility drops to mere feet ahead")
            time.sleep(2)
            print("After a few minutes you come to a clearing and you see a figure up ahead on the dock")
            time.sleep(2)
            print("Would you like to advance towards the figure?")

            choiceinput = ""
            while choiceinput not in self.choice:
                    print("Please choose: Yes or No")
                    choiceinput = input()

            if choiceinput == "Yes":
                print("You cautiously walk towards the figure")
                time.sleep(2)
                print("As you get closer to the figure, the figure looks in your direction")
                time.sleep(2)
                print("")

            elif choiceinput == "No":
                print("You decide to head away from where the figure is and continue walking")
                time.sleep(2)
                print("You reach a dead end, and walk back towards the courtyard")
                time.sleep(2)
                print("You reach the courtyard") #placeholder statement

    def boathouse(self):
                print("You walk along the muddy path around the lake")
                time.sleep(2)
                print("The fog makes it hard to see ahead, you squint your eyes")
                time.sleep(2)
                print("You continue to walk and come to a clearing, you have reached the boat house")
                time.sleep(2)
                print("Would you like to go inside?")

                choiceinput = ""
                while choiceinput not in self.choice:
                    print("Please choose: Yes or No")
                    choiceinput = input()

                if choiceinput == "Yes":
                    print("You have chosen to go inside the old boathouse")
                    time.sleep(2)
                    print("The old, rickety door creaks open, leading the way into a small shack")
                    time.sleep(2)
                    print("A damp, earthy smell sweeps over you")
                    time.sleep(2)

                elif choiceinput == "No":
                    print("Deciding not to go inside the boathouse, you back away slowly")
                    time.sleep(2)
                    print("")
    def loch(self):
        print("You choose to walk down the long, cobbled path towards the lake")
        time.sleep(2)
        print("A faint humming can be heard in the distance...")
        time.sleep(2)
        print("What is that? you think to yourself, still advancing towards the center of the lake")
        time.sleep(2)
        print("The misty path clears and you gaze upon the emerald coloured lake")
        time.sleep(2)
        print("")

    def courtyard(self):
        print("You decide to turn around and head back to the courtyard")
        time.sleep(2)
        print("Whilst walking back towards the courtyard you take in the scenery")
        time.sleep(2)
        print("You come across a student")


lake = LucariaLake()
lake.explore()
lake.crossroads()
