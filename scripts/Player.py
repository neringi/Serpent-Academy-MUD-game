from figures import books

from Room import *
import random
import math

class Player:
    def __init__(self, username,attack,defence,magic,hp,mp, inventory, level,points,preferredhand, otherhand,favfood):
        self.username = username
        self.attack = attack
        self.defence = defence
        self.magic = magic
        self.hp = hp
        self.mp = mp
        self.inventory = inventory
        self.level = level
        self.points = points
        self.preferredhand = preferredhand
        self.otherhand = otherhand
        self.favfood = favfood

    def __str__(self):
        return f"You are {self.username}."
    
    def favFood(self):
        return f"Favourite food: {self.favfood}."

    def listInventory(self):
        if len(self.inventory) == 0:
            return "Your inventory is empty."
        else:
            return self.inventory
    
    def whoAmI(self):
        return f"You are \033[1;36;40m{self.username}\033[0;37;48m.\n \n STATS: \n \033[1;36;40mHP\033[0;37;48m: {self.hp} \n \033[1;36;40mAttack\033[0;37;48m ({self.attack})\n \033[1;36;40mDefence\033[0;37;48m ({self.defence}) \n \033[1;36;40mMagic\033[0;37;48m ({self.magic})\n\n You are currently \033[1;36;40mLevel {self.level}\033[0;37;48m and have \033[1;36;40m{self.points} points\033[0;37;48m.\n"
    
    def earnPoints(self, points):
        self.points += points
        self.levelUp()

    def levelUp(self):
        newlvl = math.floor(self.points / 10) + 1
        # print(newlvl)
        diff = newlvl - self.level + 1
        # print(diff)
        if diff > 0:
            for i in range(1,diff):
                # print(i)
                pickrand = random.randint(1,3)
                # print(f"random number is {pickrand}")
                if pickrand == 1:
                    self.attack += 1
                    # print("Your Attack has increased!")
                if pickrand == 2:
                    self.defence += 1
                    # print("Your Defence has increased!")
                if pickrand == 3:
                    self.magic += 1
                    # print("Your Magic has increased!")
        
        if diff > 1:
            self.level = newlvl
            books()
            print(f"Congratulations! You have leveled up. \n Your Level is {self.level}!")
            

    def doCommand(self, command):
        match command.replace(" ", ""):
            case "listinventory":
                return self.listInventory()
            case "whoami":
                return self.whoAmI()
        


