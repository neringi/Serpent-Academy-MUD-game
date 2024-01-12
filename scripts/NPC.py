import random
class NPC:
    def __init__(self,name,description, type, items = {},social = 0):
        self.name = name
        self.description = description
        self.type = type
        self.items = items
        self.social = social

    def __str__(self):
        return f"\033[1;36;40m{self.name}. {self.description}.\033[0;37;40m. \n"
