import json

class GameState:
    def __str__(self):
        return f""

    def updateLocation(self, location):
        if location not in self.location.directions.keys():
            self.location.listDirections()
            return "Not a valid direction"
        self.location = self.location.directions[location]
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

    def equipItem(self, itemname):
        key = itemname.lower()
        item = next(item for item in self.player.inventory if item.name.lower() == key)
        if item is None:
            return f"You do not have item {itemname}\n"
        else:
            if item.wieldable:
                if self.equipment.lefthand is None:
                    self.equipment.lefthand = item
                    self.player.inventory.remove(item)
                    self.player.attack += item.attack
                    self.player.defence += item.defence
                    self.player.magic += item.magic
                    return f"You have successfully wielded {item.name} in your left hand!"
                elif self.equipment.righthand is None:
                    self.equipment.righthand = item
                    self.player.inventory.remove(item)
                    self.player.attack += item.attack
                    self.player.defence += item.defence
                    self.player.magic += item.magic
                    return f"You have successfully wielded {item.name} in your right hand!"

                # update stats
                # update equipped list
                return ""
            else:
                return f"Cannot equip {item.name}!\n"
    
    def earnPoints(self, points):
        self.player.points += points
        return ""

    
    def helpOption(self):
        return "\nIf you want to travel between areas, use keyword 'MOVE' followed by direction LEFT, RIGHT, UP or DOWN. \n\n 'WHERE AM I' will show which area you are in. \n 'WHO AM I' will show your stats. \n 'TAKE X' will let you pick up an item. \n 'ATTACK X' will attack an enemy. \n"
    def attack(self,monster):
        key = monster.lower()
        monster = self.location.monster.get(key)
        if monster is not None:
            # get attack and defence from player
            # get attack and defence from monster
            # playerhits = monster.hp - (player.attack - monster.defence)
            # monsterhits = player.hp - (monster.attach - player.defence)
            # check they havent died yet)
            playerattack = self.player.attack - monster.defence
            monster.hp -= playerattack

            if monster.hp <= 0:
                self.location.monster.pop(key,None)
                self.earnPoints(monster.points)
                return f"You have killed '{monster.name}'!\n You've earned {monster.points} points!\n"
            else:
                monsterattack = monster.attack - self.player.defence
                self.player.hp -= monsterattack
                if self.player.hp <= 0:
                    return f"You are dead! Game over!\n"
                else:
                    return f"You attacked {monster.name} for {playerattack} HP. \nThe {monster.name} attacked you for {monsterattack} HP. \n You have {self.player.hp} HP left.\n"
        else:
            return f"{key} is not in this room."

            
        
    def doCommand(self, command):
        match command:
            case "list directions":
                return self.listDirections()
            case "where am i":
                return self.whereAmI()
        
    def getCommands(self):
        return [
            "list directions",
            "where am i"
        ]
    
    # def save():

    #     player_save = {
    #         "username": "ringo"

    #     }
        # create json with player properties
        # cerate json with room properties