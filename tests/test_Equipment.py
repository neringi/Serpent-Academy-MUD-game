import unittest 
import sys
sys.path.append("scripts")
from Equipment import Equipment

class TestEquipment(unittest.TestCase):

    def setUp(self):
        self.Equipment = Equipment("sword", "shield")

    def test_str_returns_name(self):
        self.assertTrue(self.Equipment.dominanthand in self.Equipment.__str__())   
        self.assertTrue(self.Equipment.nondominanthand in self.Equipment.__str__()) 


if __name__ == '__main__':
    unittest.main()
