from GameState import GameState
from Room import Room
from Player import Player 
from Item import Item
from Monster import Monster
from Equipment import Equipment

# Define valid directions to move
VALID_MOVES = ["left", "right", "up", "down"]

# Define items 
trainingsword = Item("Training Sword","A wooden sword used by students while training.", 10, 2, 0, 0, True, "melee")
trainingshield = Item("Training Shield","A wooden kite shield used by students while training.", 10, 0, 2, 0, True, "shield")
stick = Item("Wooden stick", "A wooden stick that's about as long as your arm. Not a very useful weapon.",0,1,1,0, True, "melee")

# Define Monsters
trainingdummy = Monster("Training Dummy","A training dummy used by students while learning to fight.",0,0,0,10,0,1,10)
goblin = Monster("Goblin","A three foot grotesque fairy with razor sharp teeth, pointy ears and green skin.\n Will attack if provoked!",15,5,0,15,0,2,25)

# Define Rooms and their relationships
trainingroom = Room("The Training Room","This is the training room where the students practice to fight. There are training dummies to your left as well as a training swords and training shields nearby.")
advtrainingroom = Room("Advanced Training Room","This is the advanced training room. You should not stick around here unless you know how to fight!") 
courtyard = Room("The Courtyard","This is the courtyard.")
lecturehall = Room("Lecture Hall","A small auditorium that is the main lecture hall where non-combat lessons take place.")
dungeon = Room("Dungeon","It's cold and wet here underground. The long corridor leads to a single locked door where a sentient door knock is looking at you.")
crossroads = Room("Crossroads","A literal crossroad with a wooden sign that says: \n Elven Creek LEFT \n Elven Woods RIGHT \n Lucaria Lake UP. \n\n Enter the Woods at your own risk!!!")
lake = Room("Lucaria Lake","Vast lake, Lucaria. You can see the sunlight reflecting off its surface. The view is rather nice! Up ahead you can see the boathouse.")
boathouse = Room("The Boathouse", "This is the Lucaria lake boathouse.")
magiccafe = Room("The Toadstool Cafe", "A small cafe in Elven Creek, that many witches come to. It's famous for it's vast selection of brews.")
meadow = Room("The Meadows", "The meadows where many wildflowers bloom. Continuing travelling RIGHT will take you to Elven Woods.")
elvenwoods = Room("The Elven Woods", "The woods are eerie and dangerous but beautiful. Careful not to venture too far in, you will certainly get lost!")

# Available directions for rooms defined
trainingroomDirections = {"left": advtrainingroom,"right": courtyard}
advtrainingroomDirections = {"right": trainingroom}
courtyardDirections = {"left": trainingroom, "right": lecturehall, "up": crossroads, "down": dungeon}
dungeonDirections = {"up": courtyard}
lecturehallDirections = {"left": courtyard}
crossroadsDirections = {"left": magiccafe, "right": meadow, "up": lake, "down": courtyard}
magiccafeDirections = {"right": crossroads}
meadowDirections = {"left": crossroads, "right": elvenwoods}
elvenwoodsDirections = {"left": meadow}
lakeDirections = {"up": boathouse, "down": crossroads}
boathouseDirections = {"down": lake}

# Link the directions for rooms
trainingroom.directions = trainingroomDirections
advtrainingroom.directions = advtrainingroomDirections
courtyard.directions = courtyardDirections
dungeon.directions = dungeonDirections
lecturehall.directions = lecturehallDirections
crossroads.directions = crossroadsDirections
magiccafe.directions = magiccafeDirections
meadow.directions = meadowDirections
elvenwoods.directions = elvenwoodsDirections
lake.directions = lakeDirections
boathouse.directions = boathouseDirections

# Link the items to rooms
trainingroom.items = {"training sword": trainingsword, "training shield": trainingshield, "wooden stick": stick}


# Link monsters to rooms
trainingroom.monster = {"training dummy": trainingdummy}
advtrainingroom.monster = {"goblin": goblin}


# Define Player
player = Player("ringo", attack=10,defence=10,magic=10, hp=100, mp=100, inventory=[trainingshield], level=1, points=0, preferredhand = "left", otherhand = "right")

# Define Equipment
equipment = Equipment(dominanthand = None, righthand = None)
# Initialise gamestate
gs = GameState()
gs.player = player
gs.equipment = equipment

# Initial location
gs.location = trainingroom 

