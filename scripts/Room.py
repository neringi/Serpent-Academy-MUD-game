from adhoc import *
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
    
    def listDirections(self):
        result = ""
        for k, v in self.directions.items():
           result += f"{k} will take you to {v.name}.\n"
        return result  
    
    def exploreRoom(self):
        print_slow(self)
        if self.items is not None:
            print_slow(f"You can see items in the room: {self.items}.")
        if self.npc is not None:
            print_slow(f"There are friendly faces in the room. You could try talking to them. \n {self.npc}")
        if self.monster is not None:
            print_slow(f"There are monsters in the room! Prepare your weapon and attack! \n {self.monster}")    
    
    
    def listItems(self):
        if len(self.items) > 0:
            itemlist = ','.join(self.items)
            print_slow(f"You can see some items laying about: {itemlist}.\n") 
        else:
            print_slow(f"You cannot see any items in the area.")

    def whereAmI(self):
        return f"You are in {self.name}. {self.description} \n You may go: {list(self.directions.keys())}. \n"
    
    def doCommand(self, command):
        match command.replace(" ", ""):
            case "listdirections":
                return self.listDirections()
            case "listitems":
                return self.listItems()
            case "exploreroom":
                return self.exploreRoom()
