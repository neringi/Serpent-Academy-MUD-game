import random

class Enemy:
    def __init__(self,name):
        self.name = name
        self.hp = random.randint(5,10)
        self.attack = random.randint(2,5)
        self.xp = 50
        self.item = ""
    def damage(self, value):
        self.hp -= value
        print(f"Your health has reduced by ({value}: {self.hp}")

    def die(self):
        if self.hp == 0:
            print(f"You have defeated {Enemy}")

# goblin inherits from the enemy class
#Lake
class Imp(Enemy):
    def __init__(self):
        super().__init__(Imp)
        self.name = "Imp"
        if self.attack:
            print(f"The {self.name} attacks for {self.attack} damage")
imp = Imp()
print(imp.name, imp.attack)


class Hydra(Enemy):
    def __init__(self):
        super().__init__(Hydra)
        self.hp = 50
        self.name = "Grand Hydra"
        self.xp = 100
        self.attack = random.randint(5,10)
        self.item = "Golden Snake Eye"
        if self.hp == 0:
            print(f"You have collected the {self.item}")

# Woods

class Goblin(Enemy):
    def __init__(self):
        super().__init__(Goblin)
        self.hp = random.randint(10,20)
        self.name = "Goblin"
        self.item = "Green Jelly"
        if self.attack:
            print(f"The {self.name} attacks for {self.attack} damage!")
        if self.hp == 0:
            print(f"You have collected the {self.item}")

#testing randint
goblin = Goblin()
print(goblin.item)
print(goblin.attack)
print(goblin.hp)

class SpectralOak(Enemy):
    def __init__(self):
        super().__init__(SpectralOak)
        self.hp = 10
        self.name = "Spectral Oak"
        self.attack = random.randint(2,5)
        if self.attack:
            print(f"The {self.name} attacks for {self.attack} damage!")

SpectralOakOak = SpectralOak()
print(SpectralOakOak.attack)

class Gaianthra(Enemy):
    def __init__(self):
        super().__init__(Gaianthra)
        self.hp = 50
        self.item = "Healing Sap"
        self.attack = random.randint(5,10)
        self.name = "Gaianthra"
        if self.attack:
            print(f"{self.name} attacks you for {self.attack} damage!")
        if self.hp == 0:
            print(f"You have collected the {self.item}")


Gaianthra = Gaianthra()
print(Gaianthra.attack)


  # School/Courtyard
#def playerAttack():
    #fightChoice = opt("What do you want to do?"), ["Fight", "Item", "Flee"])

   # if (fightChoice == 0):
        #attackChoice = opt("Choose an attack"),["Punch","Magic", "Dodge"])
    #elif (fightChoice == 0):

#def enemyAttack():
       # if playerAttack() == True:
            #return enemyAttack()



