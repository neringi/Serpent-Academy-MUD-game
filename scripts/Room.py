from adhoc import *
import json
class Room:

    def __init__(self,name,description, directions = {}, items = {}, npc = {}, monster = {}):
        self.name = name
        self.description = description
        self.directions = directions
        self.items = items
        self.npc = npc
        self.monster = monster

    def __str__(self):
        return f"{self.name}.\n {self.description}. Available directions: {list(self.directions.keys())}"
    
    # def listDirections(self):
    #     result = ""
    #     for k, v in self.directions.items():
    #     # v.name is no longer available as self.directions is <String, String>
    #     # Move listDirections to GameState 
    #        result += f"{k} will take you to {v.name}.\n"
    #     return result  
    
    def exploreRoom(self):
        if len(self.items) > 0:
            itemlist = ','.join(self.items)
            print_slow(f"You can see some items laying about: {itemlist}.\n") 
        if len(self.npc) > 0:
            npclist = ','.join(self.npc)
            print_slow(f"There are friendly faces in the room: {npclist}. You could try talking to them. \n")
        if len(self.monster) > 0:
            monsterlist = ','.join(self.monster)
            print_slow(f"There are monsters in the room: {monsterlist}. Prepare your weapon and attack! \n")    
    
    
    def listItems(self):
        if len(self.items) > 0:
            itemlist = ','.join(self.items)
            print_slow(f"You can see some items laying about: {itemlist}.\n") 
        else:
            print_slow(f"You cannot see any items in the area.")

    def whereAmI(self):
        return f"You are in {self.name}.\n {self.description} \nYou may go: {list(self.directions.keys())}. \n"
    
    def doCommand(self, command):
        match command.replace(" ", ""):
            case "listitems":
                return self.listItems()
            case "exploreroom":
                return self.exploreRoom()
            case "whereami":
                return self.whereAmI()
