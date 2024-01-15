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
    healthpotion = Item("Health Potion","A flask of red liquid that heals 50HP.",5,0,0,0,False,"potion",50)
    thornydagger = Item("Thorny Dagger", "A sharp, thorned dagger. A reward from the boatman",5,10,5,0,True,"melee",0)
    healinghoneybread = Item("Healing Honey Bread", "A freshly baked slice of honey bread, Increases hp fully", 5,0,10,10,True,"potion",30)
    strengthsoda = Item("Strength Soda", "A purple, sparkling soda that allows you to block damage",5,0,25,0,True,"potion",0)
    glowberryshortcake = Item("Glowberry Shortcake", "A cake made from the finest glowberries, increases mp",5,0,0,10,True,"potion",0)
    lucarianshield = Item("Lucarian Shield", "A metal shield dropped by the Hydra, it is engraved with an aquarian language",25,0,25,0,True,"shield",0)
    sacredamulet = Item("Sacred Amulet", "A sacred amulet bestowed to you by Gaianthra, it has protective energy",25,0,25,25,True,"shield",0)
    unfairadvantage = Item("Unfair Advantage", "If you like cheating, you will use this!",1000,100,100,0,True,"melee",0)

    # Define Monsters
    trainingdummy = Monster("Training Dummy","A training dummy used by students while learning to fight.",0,0,0,10,0,1,10)
    goblin = Monster("Goblin","A three foot grotesque fairy with razor sharp teeth, pointy ears and green skin.\n Will attack if provoked!",15,5,0,15,0,2,25)
    imp = Monster("Imp","Tiny little devious creature, an imp is a trickster. Make sure to never give them your true name.",15,10,10,20,20,3,30)
    hydra = Monster("Hydra", "A silver serpentine water monster with scaled skin and four heads",20,10,0,30,15,5,50)
    gaianthra = Monster("Gaianthra", "The guardian of the Eleven Woods, a large treelike humanoid", 25,20,0,50,25,5,100)
    spectraloak = Monster("Spectral Oak", "A sentient, haunted oak tree", 10,10,0,15,5,2,20)
    slime = Monster("Slime", "A red slime with beady eyes",5,5,0,10,0,2,30)
    cacklingcrow = Monster("Cackling Crow", "A malevolent crow with obsidian feathers",15,5,0,15,0,3,20)
    swordfish = Monster("Silver Swordfish", "A fish with an actual sword for a nose",20,10,10,50,0,3,40)
    toxicfrog = Monster("Toxic Frog", "A frog that has adapted to the mystical lake environment",10,10,0,10,5,5,15)
    cyclops = Monster("Cyclops","A towering tyrant armed with barbaric weaponry and one eye",10,5,0,25,0,5,30)
    finalboss = Monster("Final Boss","It manifests as your worst fear! Once you defeat it, you win the game!",30,30,0,100,0,1,200,True)

    # Define NPCs
    luna = NPC("Luna","Student of Serpent Academy. She seems chatty!","student")
    caspian = NPC("Caspian", "Student of Serpent Academy. He seems a bit sad", "student")
    orion = NPC("Orion", "Student of Serpent Academy. He seems grumpy!", "student")
    calista = NPC("Calista", "Student of Serpent Academy. She seems to be in a good mood!", "student")
    thorne = NPC("Thorne", "Student of Serpent Academy. He seems chatty!", "student")
    fae = NPC("Fae", "Student of Serpent Academy. She looks calm", "student")
    lyra = NPC("Lyra", "Student of Serpent Academy. She looks grumpy!", "student")
    rune = NPC("Rune", "Student of Serpent Academy. He seems sad about something", "student")

    # Define Rooms and their relationships
    trainingroom = Room("Training Room","This is the training room where the students practice to fight. There are training dummies to your left as well as a training swords and training shields nearby.")
    advtrainingroom = Room("Advanced Training Room","This is the advanced training room. You should not stick around here unless you know how to fight!") 
    courtyard = Room("The Courtyard","The expansive courtyard boasts a myriad of sculptures and beautiful architecture. You can see students and teachers milling around.")
    lecturehall = Room("Lecture Hall","A small auditorium that is the main lecture hall where non-combat lessons take place.")
    dungeon = Room("Dungeon","It's cold and wet here underground. The long corridor leads to a room where the final boss is waiting. There's an item displayed to your left.")
    crossroads = Room("Crossroads","A literal crossroad with a wooden sign that says: \n Elven Creek LEFT \n Elven Woods RIGHT \n Lucaria Lake UP. \n\n Enter the Woods at your own risk!!!")
    lake = Room("Lucaria Lake","Vast lake, Lucaria. You can see the sunlight reflecting off its surface. The view is rather nice! Up ahead you can see the boathouse.")
    boathouse = Room("The Boathouse", "This is the Lucaria lake boathouse.")
    magiccafe = Room("The Toadstool Cafe", "The Toadstool Cafe is a small cafe in Elven Creek. Many witches come for it's vast selection of brews.")
    meadow = Room("The Meadows", "The meadows where many wildflowers bloom. Continuing travelling RIGHT will take you to Elven Woods.")
    elvenwoods = Room("The Elven Woods", "The woods are eerie and dangerous but beautiful. Careful not to venture too far in, you will certainly get lost!")


    rooms = {
       trainingroom.name: trainingroom,
        advtrainingroom.name: advtrainingroom,
        courtyard.name: courtyard,
        lecturehall.name: lecturehall,
        dungeon.name: dungeon,
        crossroads.name: crossroads,
        lake.name:lake, 
        boathouse.name: boathouse,
        magiccafe.name: magiccafe,
        meadow.name: meadow,
        elvenwoods.name: elvenwoods
    }

    # Available directions for rooms defined
    trainingroomDirections = {"left": advtrainingroom.name,"right": courtyard.name}
    advtrainingroomDirections = {"right": trainingroom.name}
    courtyardDirections = {"left": trainingroom.name, "right": lecturehall.name, "up": crossroads.name, "down": dungeon.name}
    dungeonDirections = {"up": courtyard.name}
    lecturehallDirections = {"left": courtyard.name}
    crossroadsDirections = {"left": magiccafe.name, "right": meadow.name, "up": lake.name, "down": courtyard.name}
    magiccafeDirections = {"right": crossroads.name}
    meadowDirections = {"left": crossroads.name, "right": elvenwoods.name}
    elvenwoodsDirections = {"left": meadow.name}
    lakeDirections = {"up": boathouse.name, "down": crossroads.name}
    boathouseDirections = {"down": lake.name}

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
    advtrainingroom.items = {commonpotion.name.lower(): commonpotion}
    trainingroom.items = {trainingsword.name.lower(): trainingsword, trainingshield.name.lower(): trainingshield, stick.name.lower(): stick}
    lake.items = {thornydagger.name.lower(): thornydagger, healthpotion.name.lower() : healthpotion, lucarianshield.name.lower(): lucarianshield}
    elvenwoods.items = {sacredamulet.name.lower(): sacredamulet, healthpotion.name.lower() : healthpotion}
    magiccafe.items = {healinghoneybread.name.lower(): healinghoneybread, strengthsoda.name.lower(): strengthsoda, glowberryshortcake.name.lower(): glowberryshortcake}
    dungeon.items = {unfairadvantage.name.lower(): unfairadvantage}
    # Link monsters to rooms
    trainingroom.monster = {trainingdummy.name.lower(): trainingdummy}
    advtrainingroom.monster = {goblin.name.lower(): goblin, cyclops.name.lower(): cyclops}
    meadow.monster = {imp.name.lower(): imp}
    crossroads.monster = {slime.name.lower(): slime}
    lake.monster = {hydra.name.lower(): hydra, swordfish.name.lower(): swordfish, toxicfrog.name.lower(): toxicfrog}
    elvenwoods.monster = {gaianthra.name.lower(): gaianthra, spectraloak.name.lower(): spectraloak, cacklingcrow.name.lower(): cacklingcrow}
    dungeon.monster = {finalboss.name.lower(): finalboss}

    # Link items to monsters
    goblin.items = {commonpotion.name.lower(): commonpotion}
    swordfish.items = {commonpotion.name.lower() : commonpotion}
    slime.items = {commonpotion.name.lower(): commonpotion}
    gaianthra.items = {sacredamulet.name.lower(): sacredamulet}
    cacklingcrow.items = {commonpotion.name.lower(): commonpotion}
    hydra.items = {lucarianshield.name.lower():lucarianshield}
    

    # Link NPCs to rooms
    courtyard.npc = {luna.name.lower(): luna, caspian.name.lower(): caspian, thorne.name.lower(): thorne, fae.name.lower(): fae}
    trainingroom.npc = {calista.name.lower(): calista}
    lecturehall.npc = {lyra.name.lower(): lyra, orion.name.lower(): orion}
    magiccafe.npc = {rune.name.lower() : rune}


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