from Player import Player
from GameState import GameState

class Item:
    def __init__(self,name,description,value,attack,defence,magic, wieldable):
        self.name = name
        self.description = description
        self.value = value
        self.attack = attack
        self.defence = defence
        self.magic = magic
        self.wieldable = wieldable

    def __str__(self):
        return f"{self.name}. {self.description}.\n Value: {self.value} \n"
