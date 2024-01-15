import unittest 
import sys
sys.path.append("scripts")
from Room import Room
from Item import Item
from Monster import Monster
from NPC import NPC
from Player import Player
from GameState import GameState
from Equipment import Equipment

class TestGameState(unittest.TestCase):

    def setUp(self):
        self.gs = GameState()

        self.gs.player = Player(
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

        self.gs.equipment = Equipment()

        advtrainingroom = Room("Advanced Training Room",
                               "This is the advanced training room. You should not stick around here unless you know how to fight!") 
        trainingroom = Room("Training Room",
                         "This is the training room where the students practice to fight. There are training dummies to your left as well as a training swords and training shields nearby.")
        
        courtyard = Room("The Courtyard",
                         "The expansive courtyard boasts a myriad of sculptures and beautiful architecture. You can see students and teachers milling around.")
   
        self.gs.location = trainingroom


        self.gs.rooms = {
                    trainingroom.name: trainingroom,
                    advtrainingroom.name: advtrainingroom,
                    courtyard.name: courtyard
                }
   
        trainingroomDirections = {"left": advtrainingroom.name,"right": courtyard.name}
        advtrainingroomDirections = {"right": trainingroom.name}
        courtyardDirections = {"left": trainingroom.name}

        trainingroom.directions = trainingroomDirections
        advtrainingroom.directions = advtrainingroomDirections
        courtyard.directions = courtyardDirections

        trainingsword = Item("Training Sword","A wooden sword used by students while training.", 10, 2, 0, 0, True, "melee",0)
        trainingdummy = Monster("Training Dummy","A training dummy used by students while learning to fight.",0,0,0,10,0,1,10)
        luna = NPC("Luna","Student of Serpent Academy. She seems chatty!","student")

        trainingroom.items = {trainingsword.name.lower(): trainingsword}
        trainingroom.monster = {trainingdummy.name.lower(): trainingdummy}
        trainingroom.npc = {luna.name.lower(): luna}
                           
    def test_str_returns_name(self):
        self.assertTrue("" in self.__str__())   
    
    def test_update_location(self):
        self.assertTrue("Not a valid" in self.gs.updateLocation("up"))
        self.assertTrue("advanced training" in self.gs.updateLocation("left"))

    def test_take_item(self):
        self.assertTrue("training sword" in self.gs.takeItem("training sword"))
        self.assertTrue(self.gs.player.inventory != [])

    def test_list_equipment(self):
        self.assertTrue("currently equipped with" in self.gs.listEquipment())
        self.assertTrue(str(self.gs.equipment.dominanthand) in self.gs.listEquipment())
        self.assertTrue(str(self.gs.equipment.nondominanthand) in self.gs.listEquipment())
        self.gs.equipment.dominanthand = "training sword"

        self.assertTrue(str(self.gs.equipment.dominanthand) in self.gs.listEquipment())

    def test_unequip_all(self):
        self.assertTrue(str(self.gs.equipment.dominanthand) in self.gs.listEquipment())
        self.gs.unequipAll()
        self.assertTrue(self.gs.equipment.dominanthand == None)

        
if __name__ == '__main__':
    unittest.main()