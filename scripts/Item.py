from Player import Player
from GameState import GameState

class Item:
    def __init__(self,name,description,value,attack,defence,magic, wieldable, itemtype, hp):
        self.name = name
        self.description = description
        self.value = value
        self.attack = attack
        self.defence = defence
        self.magic = magic
        self.wieldable = wieldable
        self.itemtype = itemtype
        self.hp = hp
        
    def __str__(self):
        return f"{self.name}"
