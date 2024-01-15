import unittest 
import sys
sys.path.append("scripts")
from Room import Room
from Item import Item
from Monster import Monster
from NPC import NPC

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.trainingroom = Room("Training Room",
                         "This is the training room where the students practice to fight. There are training dummies to your left as well as a training swords and training shields nearby.")
        
        self.advtrainingroom = Room("Advanced Training Room",
                               "This is the advanced training room. You should not stick around here unless you know how to fight!") 
        
        courtyard = Room("The Courtyard",
                         "The expansive courtyard boasts a myriad of sculptures and beautiful architecture. You can see students and teachers milling around.")
   
        # rooms = {
        #             trainingroom.name: trainingroom,
        #             advtrainingroom.name: advtrainingroom,
        #             courtyard.name: courtyard
        #         }
   
        trainingroomDirections = {"left": self.advtrainingroom.name,"right": courtyard.name}
        advtrainingroomDirections = {"right": self.trainingroom.name}
        courtyardDirections = {"left": self.trainingroom.name}

        self.trainingroom.directions = trainingroomDirections
        self.advtrainingroom.directions = advtrainingroomDirections
        courtyard.directions = courtyardDirections

        trainingsword = Item("Training Sword","A wooden sword used by students while training.", 10, 2, 0, 0, True, "melee",0)
        trainingdummy = Monster("Training Dummy","A training dummy used by students while learning to fight.",0,0,0,10,0,1,10)
        luna = NPC("Luna","Student of Serpent Academy. She seems chatty!","student")

        self.trainingroom.items = {trainingsword.name.lower(): trainingsword}
        self.trainingroom.monster = {trainingdummy.name.lower(): trainingdummy}
        self.trainingroom.npc = {luna.name.lower(): luna}
                           
    def test_str_returns_name(self):
        self.assertTrue(self.trainingroom.name in self.trainingroom.__str__())   

    def test_list_items(self):
        self.assertTrue(len(self.trainingroom.items) > 0)
        itemlist = ','.join(self.trainingroom.items)
        self.assertTrue("training sword" in itemlist)

    def test_explore_room(self):
        self.assertTrue(len(self.trainingroom.items) > 0)
        itemlist = ','.join(self.trainingroom.items)
        self.assertTrue("training sword" in itemlist)

        self.assertTrue(len(self.trainingroom.monster) > 0)
        monsterlist = ','.join(self.trainingroom.monster)
        self.assertTrue("training dummy" in monsterlist)

        self.assertTrue(len(self.trainingroom.npc) > 0)
        npclist = ','.join(self.trainingroom.npc)
        self.assertTrue("luna" in npclist)

    def test_where_am_i(self):
        self.assertTrue(self.trainingroom.name in self.trainingroom.whereAmI())  
        self.assertTrue(self.trainingroom.description in self.trainingroom.whereAmI())
        self.assertTrue("left" in self.trainingroom.whereAmI()) 
        self.assertTrue("Training Room" in self.trainingroom.whereAmI()) 
        self.assertTrue("right" in self.trainingroom.whereAmI()) 
        
if __name__ == '__main__':
    unittest.main()