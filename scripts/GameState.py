import json
import os.path
import random
from figures import sword
class GameState:
    def __str__(self):
        return f""
    
    def getRoom(self, name):
        return self.rooms[name]
    
    def updateLocation(self, location):
        if location not in self.location.directions.keys():
            print(self.listDirections())
            return "Not a valid direction!"
        self.location = self.getRoom(self.location.directions[location])
        return self.location.description
    
    def currentLocation(self):
        return f"You are in {self.location}. {self.description} \n You may go: {list(self.directions.keys())}. \n"
        
    def takeItem(self,itemname):
        key = itemname.lower()
        item = self.location.items.get(key)
        if item is not None:
            self.player.inventory.append(item)
            self.location.items.pop(key, None) 
            return f"You have added '\033[1;33;40m{itemname}\033[0;37;48m' to your inventory."
        else:
            return f"\033[1;33;40m{itemname}\033[0;37;48m not found."

    def listEquipment(self):
        domhand = self.player.preferredhand
        nondomhand = self.player.otherhand
        return f"You're currently equipped with: \n {domhand.upper()} HAND: '\033[1;33;40m{self.equipment.dominanthand}\033[0;37;48m' \n {nondomhand.upper()} HAND: '\033[1;33;40m{self.equipment.nondominanthand}\033[0;37;48m' \n "
        
    def unequipAll(self):
        equippedWeapon = self.equipment.dominanthand
        equippedShield = self.equipment.nondominanthand

        if equippedWeapon is not None:
            # add equipped item back to inventory
            self.player.inventory.append(equippedWeapon)

            # remove from equipment
            self.equipment.dominanthand = None

            # update player stats based on items stats
            self.player.attack -= equippedWeapon.attack
            self.player.defence -= equippedWeapon.defence
            self.player.magic -= equippedWeapon.magic
            print(f"You've unequipped \033[1;33;40m{equippedWeapon}\033[0;37;48m and added it to your inventory.")

        if equippedShield is not None:
            # add equipped item back to inventory
            self.player.inventory.append(equippedShield)

            # remove from equipment
            self.equipment.nondominanthand = None

            # update player stats based on items stats
            self.player.attack -= equippedShield.attack
            self.player.defence -= equippedShield.defence
            self.player.magic -= equippedShield.magic
            print(f"You've unequipped \033[1;33;40m{equippedShield}\033[0;37;48m and added it to your inventory.")

    def unequipItem(self,itemname):
        key = itemname.lower()
        
        # check if item is equipped
        equippedWeapon = self.equipment.dominanthand
        equippedShield = self.equipment.nondominanthand

        if equippedWeapon.name.lower() != key and equippedShield.name.lower() != key:
            return f"You do not have item \033[1;33;40m{itemname}\033[0;37;48m equipped\n"
        elif equippedWeapon.name.lower() == key:
            # add equipped item back to inventory
            self.player.inventory.append(equippedWeapon)

            # remove from equipment
            self.equipment.dominanthand = None

            # update player stats based on items stats
            self.player.attack -= equippedWeapon.attack
            self.player.defence -= equippedWeapon.defence
            self.player.magic -= equippedWeapon.magic
        
        elif equippedShield.name.lower() == key:
            # add equipped item back to inventory
            self.player.inventory.append(equippedShield)

            # remove from equipment
            self.equipment.nondominanthand = None

            # update player stats based on items stats
            self.player.attack -= equippedShield.attack
            self.player.defence -= equippedShield.defence
            self.player.magic -= equippedShield.magic
                
        return(f"You've unequipped '\033[1;33;40m{itemname}\033[0;37;48m' and added it to your inventory.")
 
    def equipItem(self, itemname):
        key = itemname.lower()
        # print(key)
        preferredhand = self.player.preferredhand
        otherhand = self.player.otherhand

        # Check if the item is in the inventory
        if len(self.player.inventory) == 0:
            return "Your inventory is empty."
        
        item = next((item for item in self.player.inventory if item.name.lower() == key), None)

        # print(item)
        if item is None:
            return f"You do not have item \033[1;33;40m{itemname}\033[0;37;48m\n"

        if item.wieldable: # Check if item can be wielded
            if item.itemtype == "melee": 
                # check if player is holding anything in dominant hand
                if self.equipment.dominanthand is None:
                    # equip weapon to dominant hand
                    self.equipment.dominanthand = item

                    # remove from inventory
                    self.player.inventory.remove(item) 

                    # update player stats based on item stats
                    self.player.attack += item.attack
                    self.player.defence += item.defence
                    self.player.magic += item.magic

                    sword()
                    return f"You have successfully wielded \033[1;33;40m{item.name}\033[0;37;48m in your {preferredhand} hand!"
            
                else: # if weapon already equipped in dominant hand
                    equippeditem = self.equipment.dominanthand

                    # add equipped item back to inventory
                    self.player.inventory.append(equippeditem)

                    # update player stats based on items stats
                    self.player.attack -= equippeditem.attack
                    self.player.defence -= equippeditem.defence
                    self.player.magic -= equippeditem.magic

                    # equip weapon to dominant hand
                    self.equipment.dominanthand = item

                    # remove from inventory
                    self.player.inventory.remove(item) 

                    # update player stats based on item stats
                    self.player.attack += item.attack
                    self.player.defence += item.defence
                    self.player.magic += item.magic
                    return f"You previously wielded '\033[1;33;40m{equippeditem}\033[0;37;48m' which you put in your inventory. \n You have successfully wielded \033[1;33;40m{item.name}\033[0;37;48m in your {preferredhand} hand!"
                
            elif item.itemtype == "shield":
                # check if player is holding anything in nondominant hand
                if self.equipment.nondominanthand is None:
                    # Equip shield to nondominant hand
                    self.equipment.nondominanthand = item

                    # remove from inventory
                    self.player.inventory.remove(item)

                    # update player stats based on items stats
                    self.player.attack += item.attack
                    self.player.defence += item.defence
                    self.player.magic += item.magic

                    return f"You have successfully wielded \033[1;33;40m{item.name}\033[0;37;48m in your {otherhand} hand!"
                
                else: # if shield already equipped in nondominant hand
                    equippeditem = self.equipment.nondominanthand

                    # add equipped item back to inventory
                    self.player.inventory.append(equippeditem)

                    # update player stats based on items stats
                    self.player.attack -= equippeditem.attack
                    self.player.defence -= equippeditem.defence
                    self.player.magic -= equippeditem.magic

                    # equip shield to nondominant hand
                    self.equipment.nondominanthand = item

                    # remove from inventory
                    self.player.inventory.remove(item) 

                    # update player stats based on item stats
                    self.player.attack += item.attack
                    self.player.defence += item.defence
                    self.player.magic += item.magic
                    return f"You previously wielded '\033[1;33;40m{equippeditem}\033[0;37;48m' which you put in your inventory. \n You have successfully wielded \033[1;33;40m{item.name}\033[0;37;48m in your {otherhand} hand!"
                
        else:
            return f"Cannot equip \033[1;33;40m{item.name}\033[0;37;48m!\n"

    def useItem(self, itemname):
        key = itemname.lower()

        # Check if the item is in the inventory
        item = next((item for item in self.player.inventory if item.name.lower() == key), None)
        # print(item)
        if item is None:
            return f"You do not have item \033[1;33;40m{itemname}\033[0;37;48m\n"
        else:
            if item.itemtype == "potion":
                if item.hp > 0:
                    self.player.hp += item.hp
                    # print(item.hp)
                    # print(self.player.inventory)
                    self.player.inventory.remove(item)
                    return f"You consume it. It tastes like... \033[1;33;40m{self.player.favfood}\033[0;37;48m!?!\n HP increased by {item.hp}!\n"
                else:
                    return "It did nothing but it tasted pretty good."
            else:
                return f"Cannot use \033[1;33;40m{itemname}\033[0;37;48m."    


    def helpOption(self):
        print("\nIf you want to travel between areas, use keyword \033[1;32;40m'MOVE'\033[0;37;48m followed by direction \033[1;32;40mLEFT, RIGHT, UP or DOWN.\033[0;37;48m \n\n \033[1;32;40m'WHERE AM I'\033[0;37;48m will show which area you are in. \n \033[1;32;40m'WHO AM I'\033[0;37;48m will show your stats. \n \033[1;32;40m'EXPLORE ROOM'\033[0;37;48m will tell you more about the area you are in. \n \033[1;32;40m'TAKE X'\033[0;37;48m will let you pick up an item. \n \033[1;32;40m'ATTACK X'\033[0;37;48m will attack an enemy. \n \033[1;32;40m'EQUIP X'\033[0;37;48m will equip an item. \n \033[1;32;40m'UNEQUIP X'\033[0;37;48m will unequip an item. \033[1;32;40m'UNEQUIP ALL'\033[0;37;48m will unequip everything. \n \033[1;32;40m'LIST ITEMS'\033[0;37;48m will list items in area. \n \033[1;32;40m'LIST INVENTORY'\033[0;37;48m will list items you have.\n \033[1;32;40m'LIST EQUIPMENT'\033[0;37;48m will list what you have equipped.\n \033[1;32;40m'LIST DIRECTIONS'\033[0;37;48m will list directions you can move. \n \033[1;32;40m'USE X'\033[0;37;48m will use a specified item.\n\n \033[1;32;40m'QUIT'\033[0;37;48m will quit the game.\n")
    
    def talkNPC(self,npc):
        key = npc.lower()
        npc = self.location.npc.get(key)

        if npc is not None:
            if npc.social == 0:
                npc.social += 1
                self.player.earnPoints(5)
                print(f"Your are now acquainted with \033[1;36;40m{npc.name}\033[0;37;48m!")
                return random.choice([
                    f"\033[1;36;40mHi. I'm {npc.name}!\033[0;37;48m",
                    f"\033[1;36;40mHello, you must be {self.player.username}! I'm {npc.name}.\033[0;37;48m",
                    "\033[1;36;40mWho are you again?\033[0;37;48m",
                    "\033[1;36;40mHey... Can I help you?\033[0;37;48m",
                    "\033[1;36;40mHey! Nice to meet you!\033[0;37;48m",
                    "\033[1;36;40mHmm? What's up?\033[0;37;48m",
                    f"\033[1;36;40mYou're {self.player.username}, right? I'm {npc.name}, let me know if you need anything!\033[0;37;48m"
                    ])
            elif 0 < npc.social <= 15:
                if npc.type == "student":
                    npc.social += random.randint(1, 3)
                    self.player.earnPoints(1)

                    return random.choice([
                        f"\033[1;36;40mHey, {self.player.username}! I have been studying hard for the test, I'm so nervous!\033[0;37;48m",
                        f"\033[1;36;40mHey, {self.player.username}! I've learnt a new spell! Wanna see?\033[0;37;48m \n{npc.name} attempts to cast a fireball, nearly burning their eyebrows.",
                        "\033[1;36;40mHey, how's it going?\033[0;37;48m",
                        "\033[1;36;40mHey... I'm a bit busy right now, I have an exam today!!!\033[0;37;48m",
                        "\033[1;36;40mHave you been to the meadow yet? It's so pretty there!\033[0;37;48m",
                        "\033[1;36;40mI'm never going to be able to finish this homework!!! THERE'S SO MUCH TO DO!!!\033[0;37;48m",
                        "\033[1;36;40mDo you know much about goblins?\033[0;37;48m",
                        "\033[1;36;40mDo you know much about combat moves?\033[0;37;48m",
                        "\033[1;36;40mThat lecture was sooooo long. I need a nap!\033[0;37;48m"
                        ])
            elif 15 < npc.social < 30:
                if npc.type == "student":
                    npc.social += 1
                    self.player.earnPoints(1)
                    return random.choice([
                        f"\033[1;36;40m{self.player.username}, a few of us are thinking of going to the Toadstool Cafe for a brew. Wanna come?\033[0;37;48m",
                        f"\033[1;36;40m{self.player.username}! Can you help me with combat tomorrow? You make it look so easy!\033[0;37;48m"
                        "\033[1;36;40mI really wanna go checkout the boat house at the lake!\033[0;37;48m",
                        "\033[1;36;40mI nearly got so lost in the mist last week by the lake!\033[0;37;48m",
                        "\033[1;36;40mHave you heard about the legend of the monster at the Elven Woods?\033[0;37;48m",
                        "\033[1;36;40mHi! I have combat class later! Have you seen the goblin there? I hope we don't have to fight it!\033[0;37;48m",
                        f"\033[1;36;40m{self.player.username}!!! Did you just see that gargoyle move? Creepy!\033[0;37;48m",
                        f"\033[1;36;40m{self.player.username}! Do you know much about fighting slime?\033[0;37;48m",
                        f"\033[1;36;40m What's up, {self.player.username}?\033[0;37;48m",
                        f"\033[1;36;40m What's up, {self.player.username}? Have you ever been to the Toadstool Cafe? Their honey bread is so yummy!\033[0;37;48m",
                        f"\033[1;36;40mHi, {self.player.username}!\033[0;37;48m",
                        f"\033[1;36;40mHI, {self.player.username.upper()}!!! IHADTOOMUCHCOFFEEANDNOWIMBUZZING!!!!\033[0;37;48m",
                        f"\033[1;36;40mIs it nap time yet?\033[0;37;48m"
                        ])
            else:
                if npc.type == "student":
                    return random.choice([
                        f"{npc.name} nods at you. They're busy revising for an exam.",
                        f"\033[1;36;40mHey, {self.player.username}! So sorry, can we chat later I've almost finished this homework!\033[0;37;48m",
                        f"\033[1;36;40mHey, {self.player.username}! How's it going?\033[0;37;48m",
                        f"\033[1;36;40mHi, {self.player.username}! That exam was so hard, glad it's over!\033[0;37;48m",
                        f"\033[1;36;40m{self.player.username}! Brew at the Toadstool Cafe later?\033[0;37;48m",
                        f"\033[1;36;40mAll good?\033[0;37;48m"
                    ])

        else:
            return f"\033[1;36;40m{key}\033[0;37;48m is not in this room."

    def attack(self,monster):
        key = monster.lower()
        monster = self.location.monster.get(key)

        if monster is None: 
            return f"\033[1;31;40m{key}\033[0;37;48m is not in this room."
        # print(type(monster))
        # print(monster)

        playerattack = 0 if monster.defence >= self.player.attack else self.player.attack - monster.defence
        monsterattack = 0 if self.player.defence >= monster.attack else monster.attack - self.player.defence

        monster.hp -= playerattack

        if monster.hp <= 0:

            
            # Check if monster is holding items and move to inventory if yes
            loot = monster.items.values()
            # print(loot)

            self.player.inventory += loot
            
            self.location.monster.pop(key,None)
            self.player.earnPoints(monster.points)

            if monster.finalboss:
                print(f"You have killed '\033[1;31;40m{monster.name}\033[0;37;48m'!\n You've earned {monster.points} points!\n")
                return "endgame"
            return f"You have killed '\033[1;31;40m{monster.name}\033[0;37;48m'!\n You've earned {monster.points} points!\n"
        
        
        self.player.hp -= monsterattack

        if self.player.hp <= 0:
            return "dead"

        result = ""
        if playerattack == 0:
            result += f"Be careful! This monster may be too strong for you!!!\n"
        if monsterattack == 0:
            result += f"This monster is no match for you! Its attack is too weak to hurt you.\n"
        
        return f"{result}You attacked \033[1;31;40m{monster.name} \033[0;37;48m for {playerattack} HP. \nThe \033[1;31;40m{monster.name}\033[0;37;48m attacked you for {monsterattack} HP. \n You have {self.player.hp} HP left.\n"

        
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    
    def saveGame(self):
        dirname = os.path.dirname(os.path.dirname(__file__))
        # print(dirname)
        savefilepath = dirname + '/resources/' + self.player.username +'.json'
        # print(savefilepath)

        # file_exists = os.path.isfile(savefilepath)
        # if file_exists:
        with open(savefilepath, 'w', encoding='utf-8') as f: 
            f.write(self.toJSON())
        return f"Your game has been saved, {self.player.username}!"
        # else:
        #     print("Something went wrong. Could not save game, try again")
    
    def listDirections(self):
        result = ""
        # print(self.location.directions.items())
        for k, v in self.location.directions.items():
            result += f"\033[1;32;40m{k}\033[0;37;48m will take you to \033[1;32;40m{self.rooms[v].name}\033[0;37;48m.\n"
            # print(self.rooms[v])
        return result