import unittest 
import sys
sys.path.append("scripts")
from NPC import NPC

class TestNPC(unittest.TestCase):

    def setUp(self):
        self.NPC = NPC("Luna","Student of Serpent Academy. She seems chatty!","student")

    def test_str_returns_name(self):
        self.assertTrue(self.NPC.name in self.NPC.__str__())   
        self.assertTrue(self.NPC.description in self.NPC.__str__()) 


if __name__ == '__main__':
    unittest.main()
