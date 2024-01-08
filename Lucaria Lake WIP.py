import time
import unittest
from npc import boatman
import random
from monsters import Hydra
from monsters import Imp


class LucariaLake:
    def __init__(self):
        self.directions = ["R", "L", "FW", "BW"]
        self.choice = ["Yes", "No"]
        self.weapon = True

    def explore(self):
        print("You walk on the path towards the grand lake in the courtyard of the academy")
        time.sleep(1)

    """
    The crossroads function allows the user to travel
    around the lake section within the game
    """

    def crossroads(self):
        print("You come to a crossroads. Which way would you like to go?")
        userinput = ""
        while userinput not in self.directions:
            userinput = input("Please choose: right(R),left(L),forwards(FW) or backwards(BW)")
        if userinput == "R" or "r":
            self.mist()
        elif userinput == "L" or "l":
            self.boathouse()
        elif userinput == "FW" or "fw":
            self.loch()
        elif userinput == "BW" or "bw":
            self.courtyard()
        else:
            return "please enter a valid direction"
        """ 
        The mist function starts if R is chosen in directions
        There are options to choose whether the player
        wants to play the boatman side-section of the game
        """

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
            boatman()

        elif choiceinput == "No":
            print("You decide to head away from where the figure is and continue walking")
            time.sleep(2)
            print("You reach a dead end, and walk back towards the courtyard")
            time.sleep(2)
            print("You reach the courtyard")

        """
        The boathouse function below starts the interaction with
        the boathouse section of the story when L is chosen in directions
        """

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
            print("There is a box on the left and you pick it up")
            time.sleep(2)
            print("You carefully pry open the box")
            time.sleep(2)
            # get item

        elif choiceinput == "No":
            print("Deciding not to go inside the boathouse, you back away slowly")
            time.sleep(2)
            print("Heading back down the path you encounter an Imp!")
            time.sleep(2)
            print("Prepare for battle!")
            Imp()

    """
    The Loch function allows the user to interact with
    the loch storyline if FW was chosen within directions
    """

    def loch(self):
        print("You choose to walk down the long, cobbled path towards the lake")
        time.sleep(2)
        print("A faint hissing can be heard in the distance...")
        time.sleep(2)
        print("What is that? you think to yourself, still advancing towards the center of the lake")
        time.sleep(2)
        print("The misty path clears and you gaze upon the emerald coloured lake")
        time.sleep(2)
        print("Stepping towards the edge of the lake, you peer into the water")
        time.sleep(2)
        print("After a few seconds a pair of eyes stare back at you...and then a few more")
        time.sleep(2)
        print("Prepare for battle!")
        Hydra()

    def courtyard(self):
        print("You decide to turn around and head back to the courtyard")
        time.sleep(2)
        print("Whilst walking back towards the courtyard you take in the scenery")
        time.sleep(2)
        print("You come across a student")


def main():
    lake = LucariaLake()
    lake.explore()
    lake.crossroads()
    boatman()


if __name__ == "__main__":
    main()

# class TestDirections(unittest.TestCase):

# def test_upper(self):
#  self.assertEqual('r'.upper(), 'R')

#  def test_isupper(self):
#  self.assertTrue('R' .isupper())
#  self.assertFalse('r'.isupper())


#  if __name__ == '__main__':
#  unittest.main()

# class InputDirection(unittest.TestCase):
# def __init__(self,move):
# super(InputDirection, self).__init__()
# self.directions = ['R', 'L', 'FW', 'BW']
#  self.move = move

# def test_travel(self):
# if self.move == 'R':
#   self.assertTrue(True,'Travelled right')
# elif self.move == 'L':
#     self.assertTrue(True,'Travelled left')
# elif self.move == 'FW':
#    self.assertTrue(True,'Travelled forwards')
# elif self.move == 'BW':
#  self.assertTrue(True,'Travelled backwards')
# elif not isinstance(self.move, str):
#   raise TypeError('Input must be type string')

# if __name__ == '__main__':
#  unittest.main()

