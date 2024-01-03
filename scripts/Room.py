class Room:
    def __init__(self,name,description, directions = {}, items = {}, npc = {}, monster = {}):
        self.name = name
        self.description = description
        self.directions = directions
        self.items = items
        self.npc = npc
        self.monster = monster

    def __str__(self):
        return f"{self.name}. {self.description}. Available directions: {list(self.directions.keys())}"
    
    def listDirections(self):
        result = ""
        for k, v in self.directions.items():
           result += f"{k} will take you to {v.name}.\n"
        return result  
        
    
    def listItems(self):
        print(f"You can see: {self.items} \n") 



    def whereAmI(self):
        return f"You are in {self.name}. {self.description} \n You may go: {list(self.directions.keys())}. \n"
    
    def doCommand(self, command):
        match command:
            case "list directions":
                return self.listDirections()
            case "list items":
                return self.listItems()
        
    def getCommands(self):
        return [
            "list directions",
            "where am i"
        ]
