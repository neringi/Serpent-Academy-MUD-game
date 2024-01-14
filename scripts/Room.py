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
    
    # Lists items, NPCs and monsters in the room, if they're present
    def exploreRoom(self):
        if len(self.items) > 0:
            itemlist = ','.join(self.items)
            print_slow(f"You can see some items laying about: \033[1;33;40m {itemlist}\033[0;37;48m.\n") 
        if len(self.npc) > 0:
            npclist = ','.join(self.npc)
            print_slow(f"There are friendly faces in the room: \033[1;36;40m{npclist}\033[0;37;48m. You could try talking to them. \n")
        if len(self.monster) > 0:
            monsterlist = ','.join(self.monster)
            print_slow(f"There are monsters in the room: \033[1;31;40m{monsterlist}\033[0;37;48m. Prepare your weapon and attack! \n") 
        if len(self.items) == 0 and len(self.npc) == 0 and len(self.monster) == 0:
            print_slow("There's not much left to do in this room!")
    
    # Lists any items in the room
    def listItems(self):
        if len(self.items) > 0:
            itemlist = ','.join(self.items)
            print_slow(f"You can see some items laying about: \033[1;33;40m{itemlist}\033[0;37;48m.\n") 
        else:
            print_slow(f"You cannot see any items in the area.")

    # Lists room you are in and possible directions
    def whereAmI(self):
        return f"You are in \033[1;32;40m{self.name}\033[0;37;48m.\n {self.description} \nYou may go: \033[1;32;40m{list(self.directions.keys())}\033[0;37;48m. \n"
    
    def doCommand(self, command):
        match command.replace(" ", ""):
            case "listitems":
                return self.listItems()
            case "exploreroom":
                return self.exploreRoom()
            case "whereami":
                return self.whereAmI()
