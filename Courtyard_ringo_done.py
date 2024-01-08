import time

class Courtyard:
    def __init__(self):
        self.directions = ["R", "L", "FW", "BW"]
        self.choice = ["Yes", "No"]
        self.weapon = True

    def explore(self):
        print("The expansive courtyard boasts a myriad of sculptures and beautiful architecture")
        time.sleep(2)
        print("You look around curiously at the students and teachers milling around")
        time.sleep(2)
        print("")



courtyard = Courtyard()
courtyard.explore()
