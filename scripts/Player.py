# class Player:
#     def __init__(self, username):
#         self.username = username
#         self.score = 0
    
    # def set_score()

    # def add_points()

    # def save(self):
    #     users = load_list_dict_from_csv("../data/users.csv")
    #         for row in row["name".strip().lower() == username.strip().lower():
    #             row["score"] = self.score
    #             if

# if __name__ = "__main__":
#     logging.basicConfig(filename="my_log.log")

from Room import *

class Player:
    def __init__(self, username,attack,defence,magic,hp,mp, inventory, level,points, armor):
        self.username = username
        self.attack = attack
        self.defence = defence
        self.magic = magic
        self.hp = hp
        self.mp = mp
        self.inventory = inventory
        self.level = level
        self.points = points
        self.armor = armor

    def __str__(self):
        return f"You are {self.username}."

    def listInventory(self):
        return self.inventory
    
    def whoAmI(self):
        return f"You are {self.username}. \n STATS: \n Attack ({self.attack})\n Defence ({self.defence}) \n Magic ({self.magic})\n\n You are currently Level {self.level} and have {self.points} points.\n"
    
    
    def doCommand(self, command):
        match command:
            case "list inventory":
                return self.listInventory()
            case "who am i":
                return self.whoAmI()
            # case "where am i":
            #     return self.whereAmI()
            case "list directions":
                return 
        
    def getCommands(self):
        return [
            "list inventory",
            "list directions"
            "who am i",
            "where am i"
        ]
    


