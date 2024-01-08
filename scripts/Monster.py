
class Monster:
    def __init__(self,name,description, attack, defence, magic, hp, mp,level, points, items = {}):
        self.name = name
        self.description = description
        self.attack = attack
        self.defence = defence
        self.magic = magic
        self.hp = hp
        self.mp = mp
        self.level = level
        self.points = points
        self.items = items

    def __str__(self):
        return f"\033[1;31;40m{self.name}\033[0;37;40m. {self.description}.\n STATS: STR {self.attack} \n INT {self.defence} MGC {self.magic}.\n"
