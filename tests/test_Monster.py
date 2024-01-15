import unittest 
import sys
sys.path.append("scripts")
from Monster import Monster

class TestMonster(unittest.TestCase):

    def setUp(self):
        self.monster = Monster("Training Dummy","A training dummy used by students while learning to fight.",0,0,0,10,0,1,10)

    def test_str_returns_name(self):
        self.assertTrue(self.monster.name in self.monster.__str__())   


if __name__ == '__main__':
    unittest.main()
