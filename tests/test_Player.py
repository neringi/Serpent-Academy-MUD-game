import unittest 
import sys
sys.path.append("scripts")
from Player import Player
from Item import Item

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player(
            "test",
            attack=5,
            defence=10,
            magic=5,
            hp=100,
            mp=100,
            inventory=[],
            level=1,
            points=0,
            preferredhand="left",
            otherhand="right",
            favfood = "example"
        )
        self.item = Item("Training Sword",
                         "A wooden sword used by students while training.", 
                         10, 2, 0, 0, True, "melee",0)

    def test_str_returns_name(self):
        self.assertTrue(self.player.username in self.player.__str__())
    
    def test_add_inventory_and_list(self):
        self.assertTrue(self.player.inventory == [])
        self.player.inventory.append(self.item)
        self.assertTrue(self.item in self.player.listInventory())
    
    def test_list_empty_inventory(self):
        self.assertTrue("empty" in self.player.listInventory())

    def test_who_am_i(self):
        whoAmI = self.player.whoAmI()
        self.assertTrue(self.player.username in whoAmI)
        self.assertTrue(str(self.player.attack) in whoAmI)
        self.assertTrue(str(self.player.defence) in whoAmI)
    
    def test_levelling_up(self):
        self.assertTrue(self.player.points == 0)
        self.player.earnPoints(5)
        self.assertTrue(self.player.level == 1)
        self.player.earnPoints(5)
        self.assertTrue(self.player.points == 10)
        self.assertTrue(self.player.level == 2)

    def test_favourite_food(self):
        self.assertTrue(self.player.favfood in self.player.favFood())
    


if __name__ == '__main__':
    unittest.main()
