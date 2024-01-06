from Player import Player
from GameState import GameState

class Item:
    def __init__(self,name,description,value,attack,defence,magic, wieldable, itemtype):
        self.name = name
        self.description = description
        self.value = value
        self.attack = attack
        self.defence = defence
        self.magic = magic
        self.wieldable = wieldable
        self.itemtype = itemtype
    def __str__(self):
        return f"{self.name}"
