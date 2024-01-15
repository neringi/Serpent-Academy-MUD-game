import unittest 
import sys
sys.path.append("scripts")
from Item import Item

class TestItem(unittest.TestCase):

    def setUp(self):
        self.item = Item("Training Sword",
                         "A wooden sword used by students while training.", 
                         10, 2, 0, 0, True, "melee",0)

    def test_str_returns_name(self):
        self.assertTrue(self.item.name in self.item.__str__())   


if __name__ == '__main__':
    unittest.main()
