from GameState import GameState
from Room import Room
from Player import Player 
from Item import Item
from Monster import Monster
from Equipment import Equipment

# Define valid directions to move
VALID_MOVES = ["left", "right", "up", "down"]

# Define items 
trainingsword = Item("Training Sword","A wooden sword used by students while training.", 10, 2, 0, 0, True)
trainingshield = Item("Training Shield","A wooden kite shield used by students while training.", 10, 0, 2, 0, True)

# Define Monsters
trainingdummy = Monster("Training Dummy","A training dummy used by students while learning to fight.",0,0,0,10,0,1,10)
goblin = Monster("Goblin","A three foot grotesque fairy with razor sharp teeth, pointy ears and green skin.\n Will attack if provoked!",15,5,0,15,0,2,25)

# Define Rooms and their relationships
trainingroom = Room("The Training Room","This is the training room where the students practice to fight. You can see a Training Dummy to your left as well as a Training Sword and Training Shield next to it.")
roomB = Room("Room B","This is the second room") 
roomC = Room("Room C","This is the third room")

# Available directions for rooms defined
trainingroomDirections = {"left": roomB,"right": roomC}
roomBDirections = {"right": trainingroom}
roomCDirections = {"left": trainingroom}

# Link the directions for rooms
trainingroom.directions = trainingroomDirections
roomB.directions = roomBDirections
roomC.directions = roomCDirections

# Link the items to rooms
trainingroom.items = {"training sword": trainingsword, "training shield": trainingshield}

# Link monsters to rooms
trainingroom.monster = {"training dummy": trainingdummy}
roomB.monster = {"goblin": goblin}


# Define Player
player = Player("ringo", attack=10,defence=10,magic=10, hp=100, mp=100, inventory=[trainingshield], level=1, points=0,armor={})

# Define Equipment
equipment = Equipment(lefthand = None, righthand = None)
# Initialise gamestate
gs = GameState()
gs.player = player
gs.equipment = equipment

# Initial location
gs.location = trainingroom 

