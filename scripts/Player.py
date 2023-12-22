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

class Player:
    def __init__(self, username):
        self.username = username
        self.str = 0
        self.int = 0
        self.mgc = 0
        self.hp = 100
        self.mp = 100
        self.inventory = []
        self.level = 0
        self.points = 0
        self.armor = []

    def listInventory(self):
        return self.inventory
    
    def whoAmI(self):
        return self.username
    
    def doCommand(self, command):
        match command:
            case "list inventory":
                return self.listInventory()
            case "who am i":
                return self.whoAmI()
        
    def getCommands(self):
        return [
            "list inventory",
            "who am i"
        ]
