from enum import Enum

ItemType = Enum('ItemType', ['Melee', 'Shield', 'Potion', 'Magic'])
Wieldable = [ItemType.Magic, ItemType.Shield, ItemType.Melee]