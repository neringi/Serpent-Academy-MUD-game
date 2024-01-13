from GameState import GameState
from Room import Room
from Player import Player 
from Item import Item
from Monster import Monster
from Equipment import Equipment
from NPC import NPC

def initialGame():

    # Define valid directions to move
    VALID_MOVES = ["left", "right", "up", "down"]

    # Define items 
    trainingsword = Item("Training Sword","A wooden sword used by students while training.", 10, 2, 0, 0, True, "melee",0)
    trainingshield = Item("Training Shield","A wooden kite shield used by students while training.", 10, 0, 2, 0, True, "shield",0)
    stick = Item("Wooden Stick", "A wooden stick that's about as long as your arm. Not a very useful weapon.",0,1,1,0, True, "melee",0)
    commonpotion = Item("Common Potion","A flask of red liquid that heals 10HP.",5,0,0,0,False,"potion",10)
    thornydagger = Item("Thorny Dagger", "A sharp, thorned dagger. A reward from the boatman",5,10,5,0,True,"melee",0)
    healinghoneybread = Item("Manuka Honey Bread", "A freshly baked slice of honey bread, Increases hp fully", 5,0,10,10,True,"potion",30)
    strengthsoda = Item("Extra Strength Potion", "A purple, sparkling soda that allows you to block damage",5,0,25,0,True,"potion",0)
    glowberryshortcake = Item("Glowberry Shortcake", "A cake made from the finest glowberries, increases mp",5,0,0,10,True,"potion",0)
    lucarianshield = Item("Lucarian Shield", "A metal shield dropped by the Hydra, it is engraved with an aquarian language",25,0,25,0,True,"shield",0)
    sacredamulet = Item("Sacred Amulet", "A sacred amulet bestowed to you by Gaianthra, it has protective energy",25,0,25,25,True,"magic",0)

    # Define Monsters
    trainingdummy = Monster("Training Dummy","A training dummy used by students while learning to fight.",0,0,0,10,0,1,10)
    goblin = Monster("Goblin","A three foot grotesque fairy with razor sharp teeth, pointy ears and green skin.\n Will attack if provoked!",15,5,0,15,0,2,25)
    imp = Monster("Imp","Tiny little devious creature, an imp is a trickster. Make sure to never give them your true name.",15,10,10,20,20,3,20)
    hydra = Monster("Hydra", "A silver serpentine water monster with scaled skin and four heads",20,10,0,30,15,5,50)
    gaianthra = Monster("Gaianthra", "The guardian of the Eleven Woods, a large treelike humanoid", 25,20,0,50,25,5,100)
    spectraloak = Monster("Spectral Oak", "A sentient, haunted oak tree", 10,10,0,15,5,2,15)
    slime = Monster("Slime", "A red slime with beady eyes",5,5,0,10,0,2,5,commonpotion)
    cacklingcrow = Monster("Cackling Crow", "A malevolent crow with obsidian feathers",3,5,0,15,0,3,5,None)
    swordfish = Monster("A silver swordfish", "A fish with an actual sword for a nose",6,10,10,0,0,10,commonpotion)
    toxicfrog = Monster("A toxic frog", "A frog that has adapted to the mystical lake environment",5,5,0,10,5,5,10,None)
    cyclops = Monster("A towering tyrant armed with barbaric weaponry and one eye",10,5,0,25,0,5,25,None)

    # Define NPCs
    luna = NPC("Luna","Student of Serpent Academy. She seems chatty!","student")
    caspian = NPC("Caspian", "Student of Serpent Academy. He seems a bit sad", "student")
    orion = NPC("Orion", "Student of Serpent Academy. He seems grumpy!", "student")
    calista = NPC("Calista", "Student of Serpent Academy. She seems to be in a good mood!", "student")
    thorne = NPC("Thorne", "Student of Serpent Academy. He seems chatty!", "student")
    fae = NPC("Fae", "Student of Serpent Academy. She looks calm", "student")
    lyra = NPC("Lyra", "Student of Serpent Academy. She looks grumpy!", "student")
    rune = NPC("Rune", "Student of Serpent Academy. He seems sad about something", "student")


    #Felicity = NPC("Felicity", "The Toadstool Cafe Shopkeeper", "other")
   # Pedro = NPC("Pedro", "The Dungeon Master", "other")
    #EdenEldritch = NPC("Eden Eldritch", "Serpent Academy Combat Teacher", "teacher")
    #SeraphinaSpellweaver = NPC("Seraphina Spellweaver", "Serpent Academy Magic Teacher", "teacher")


    # Define Rooms and their relationships
    trainingroom = Room("The Training Room","This is the training room where the students practice to fight. There are training dummies to your left as well as a training swords and training shields nearby.")
    advtrainingroom = Room("Advanced Training Room","This is the advanced training room. You should not stick around here unless you know how to fight!") 
    courtyard = Room("The Courtyard","The expansive courtyard boasts a myriad of sculptures and beautiful architecture. You can see students and teachers milling around.")
    lecturehall = Room("Lecture Hall","A small auditorium that is the main lecture hall where non-combat lessons take place.")
    dungeon = Room("Dungeon","It's cold and wet here underground. The long corridor leads to a single locked door where a sentient door knock is looking at you.")
    crossroads = Room("Crossroads","A literal crossroad with a wooden sign that says: \n Elven Creek LEFT \n Elven Woods RIGHT \n Lucaria Lake UP. \n\n Enter the Woods at your own risk!!!")
    lake = Room("Lucaria Lake","Vast lake, Lucaria. You can see the sunlight reflecting off its surface. The view is rather nice! Up ahead you can see the boathouse.")
    boathouse = Room("The Boathouse", "This is the Lucaria lake boathouse.")
    magiccafe = Room("The Toadstool Cafe", "A small cafe in Elven Creek, that many witches come to. It's famous for it's vast selection of brews.")
    meadow = Room("The Meadows", "The meadows where many wildflowers bloom. Continuing travelling RIGHT will take you to Elven Woods.")
    elvenwoods = Room("The Elven Woods", "The woods are eerie and dangerous but beautiful. Careful not to venture too far in, you will certainly get lost!")

    rooms = {
        "trainingroom": trainingroom,
        "advtrainingroom": advtrainingroom,
        "courtyard": courtyard,
        "lecturehall": lecturehall,
        "dungeon": dungeon,
        "crossroads": crossroads,
        "lake":lake, 
        "boathouse": boathouse,
        "magiccafe": magiccafe,
        "meadow": magiccafe,
        "elvenwoods": elvenwoods
    }

    # Available directions for rooms defined
    trainingroomDirections = {"left": "advtrainingroom","right": "courtyard"}
    advtrainingroomDirections = {"right": "trainingroom"}
    courtyardDirections = {"left": "trainingroom", "right": "lecturehall", "up": "crossroads", "down": "dungeon"}
    dungeonDirections = {"up": "courtyard"}
    lecturehallDirections = {"left": "courtyard"}
    crossroadsDirections = {"left": "magiccafe", "right": "meadow", "up": "lake", "down": "courtyard"}
    magiccafeDirections = {"right": "crossroads"}
    meadowDirections = {"left": "crossroads", "right": "elvenwoods"}
    elvenwoodsDirections = {"left": "meadow"}
    lakeDirections = {"up": "boathouse", "down": "crossroads"}
    boathouseDirections = {"down": "lake"}

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
    advtrainingroom.items = {"common potion": commonpotion}
    trainingroom.items = {"training sword": trainingsword, "training shield": trainingshield, "wooden stick": stick}
    lake.items = {"Thorny Dagger": thornydagger, "Health Potion" : commonpotion, "Lucarian Shield":lucarianshield}
    elvenwoods.items = {"Sacred Amulet": sacredamulet, "Health Potion" : commonpotion}
    magiccafe.items = {"Healing Honey Bread": healinghoneybread, "Strength Soda": strengthsoda, "Glowberry Shortcake": glowberryshortcake}

    # Link monsters to rooms
    trainingroom.monster = {"training dummy": trainingdummy}
    advtrainingroom.monster = {"goblin": goblin, "cyclops": cyclops}
    meadow.monster = {"imp": imp}
    lake.monster = {"hydra": hydra, "swordfish": swordfish, "toxic frog": toxicfrog}
    elvenwoods.monster = {"gaianthra": gaianthra, "spectraloak": spectraloak, "cackling crow":cacklingcrow}
    dungeon.monster = {"slime": slime}

    # Link items to monsters
    goblin.items = {"Common Potion": commonpotion}
    swordfish.items = {"Common Potion" : commonpotion}
    slime.items = {"Common Potion": commonpotion}
    gaianthra.items = {"Sacred Amulet": sacredamulet}
    cacklingcrow.items = { "Common Potion":commonpotion}
    hydra.items = {"Lucarian Shield":lucarianshield}

    # Link NPCs to rooms
    courtyard.npc = {"Luna": luna}
    courtyard.npc = {"Caspian" : caspian}
    courtyard.npc = {"Orion" : orion}
    courtyard.npc = {"Calista" : calista}
    courtyard.npc = {"Thorne":thorne}
    courtyard.npc = {"Fae" : fae}
    courtyard.npc = {"Lyra" : lyra}
    courtyard.npc = {"Rune" : rune}


    # Define Player
    # player gets defined when character is created

    # Define Equipment
    equipment = Equipment(dominanthand = None, nondominanthand = None)

    # Initialise gamestate
    gs = GameState()
    gs.equipment = equipment
    gs.rooms = rooms

    # Initial location
    gs.location = trainingroom 

    return gs