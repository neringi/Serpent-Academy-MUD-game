import json
import os.path
class GameState:
    def __str__(self):
        return f""
    
    def getRoom(self, name):
        return self.rooms[name]
    
    def updateLocation(self, location):
        if location not in self.location.directions.keys():
            self.location.listDirections()
            return "Not a valid direction"
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
            return f"You have added '{itemname}' to your inventory."
        else:
            return f"{itemname} not found."

    def listEquipment(self):
        domhand = self.player.preferredhand
        nondomhand = self.player.otherhand
        return f"You're currently equipped with: \n {domhand.upper()} HAND: '{self.equipment.dominanthand}' \n {nondomhand.upper()} HAND: '{self.equipment.nondominanthand}' \n "
        
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
            print(f"You've unequipped {equippedWeapon} and added it to your inventory.")

        if equippedShield is not None:
            # add equipped item back to inventory
            self.player.inventory.append(equippedShield)

            # remove from equipment
            self.equipment.nondominanthand = None

            # update player stats based on items stats
            self.player.attack -= equippedShield.attack
            self.player.defence -= equippedShield.defence
            self.player.magic -= equippedShield.magic
            print(f"You've unequipped {equippedShield} and added it to your inventory.")

    def unequipItem(self,itemname):
        key = itemname.lower()
        
        # check if item is equipped
        equippedWeapon = self.equipment.dominanthand
        equippedShield = self.equipment.nondominanthand

        if equippedWeapon.name.lower() != key and equippedShield.name.lower() != key:
            return f"You do not have item {itemname} equipped\n"
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
                
        return(f"You've unequipped '{itemname}' and added it to your inventory.")
 
    def equipItem(self, itemname):
        key = itemname.lower()
        preferredhand = self.player.preferredhand
        otherhand = self.player.otherhand

        # Check if the item is in the inventory
        item = next(item for item in self.player.inventory if item.name.lower() == key)
        if item is None:
            return f"You do not have item {itemname}\n"
        else:
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

                        return f"You have successfully wielded {item.name} in your {preferredhand} hand!"
                
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
                        return f"You previously wielded '{equippeditem}' which you put in your inventory. \n You have successfully wielded {item.name} in your {preferredhand} hand!"
                    
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

                        return f"You have successfully wielded {item.name} in your {otherhand} hand!"
                    
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
                        return f"You previously wielded '{equippeditem}' which you put in your inventory. \n You have successfully wielded {item.name} in your {preferredhand} hand!"
                    
            else:
                return f"Cannot equip {item.name}!\n"

    def helpOption(self):
        return "\nIf you want to travel between areas, use keyword \033[1;32;40m'MOVE'\033[0;37;48m followed by direction \033[1;32;40mLEFT, RIGHT, UP or DOWN.\033[0;37;48m \n\n \033[1;32;40m'WHERE AM I'\033[0;37;48m will show which area you are in. \n \033[1;32;40m'WHO AM I'\033[0;37;48m will show your stats. \n \033[1;32;40m'EXPLORE ROOM'\033[0;37;48m will tell you more about the area you are in. \n \033[1;32;40m'TAKE X'\033[0;37;48m will let you pick up an item. \n \033[1;32;40m'ATTACK X'\033[0;37;48m will attack an enemy. \n \033[1;32;40m'EQUIP X'\033[0;37;48m will equip an item. \n \033[1;32;40m'UNEQUIP X'\033[0;37;48m will unequip an item. \033[1;32;40m'UNEQUIP ALL'\033[0;37;48m will unequip everything. \n \033[1;32;40m'LIST ITEMS'\033[0;37;48m will list items in area. \n \033[1;32;40m'LIST INVENTORY'\033[0;37;48m will list items you have.\n \033[1;32;40m'LIST EQUIPMENT'\033[0;37;48m will list what you have equipped. \n"
    
    def attack(self,monster):
        key = monster.lower()
        monster = self.location.monster.get(key)
        if monster is not None:
            playerattack = self.player.attack - monster.defence
            monster.hp -= playerattack

            if monster.hp <= 0:
                self.location.monster.pop(key,None)
                self.player.earnPoints(monster.points)
                return f" You have killed '{monster.name}'!\n You've earned {monster.points} points!\n"
            else:
                monsterattack = monster.attack - self.player.defence
                self.player.hp -= monsterattack
                if self.player.hp <= 0:
                    return f"You are dead! Game over!\n"
                else:
                    return f"You attacked {monster.name} for {playerattack} HP. \nThe {monster.name} attacked you for {monsterattack} HP. \n You have {self.player.hp} HP left.\n"
        else:
            return f"{key} is not in this room."
        
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    
    def saveGame(self):
        dirname = os.path.dirname(os.path.dirname(__file__))
        # print(dirname)
        savefilepath = dirname + '/resources/' + self.player.username +'.json'
        print(savefilepath)

        # file_exists = os.path.isfile(savefilepath)
        # if file_exists:
        with open(savefilepath, 'w', encoding='utf-8') as f: 
            f.write(self.toJSON())
            
        return f"Your game has been saved, {self.player.username}!"
        # else:
        #     print("Something went wrong. Could not save game, try again")
