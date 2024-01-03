from init import *
from adhoc import *



def display(info):
    if type(info) is not str:
        # print(info)
        if type(info) is list:
            for i in info:
                print(i)
    else:
        print_slow(info)

def move(location):
    if location not in VALID_MOVES:
        print_slow("Not a valid direction \n")
        display(gs.location.whereAmI())
        return
    return gs.updateLocation(location)

def updateState(action):
    tokens = action.split(None,1)
    verb = tokens[0]
    match verb:
        case "move":
            display(move(tokens[1]))
        case "who":
            display(gs.player.doCommand(action))
        case "where":
            display(gs.location.whereAmI())
        case "take":
            display(gs.takeItem(tokens[1]))
        case "list":
            if "inventory" in tokens[1]:
                display(gs.player.listInventory())
        case "attack":
            display(gs.attack(tokens[1]))
        case "help":
            display(gs.helpOption())
        case "equip":
            display(gs.equipItem(tokens[1]))


while True:
    # print_slow(f"You are in {gs.location.name}")
    userInput = input("\nYour Move:")
    userInput = userInput.lower()
    if userInput in ("left", "right","up", "down"):
        print_slow("If you want to travel, use keyword 'MOVE' before choosing a direction")
        # validate input 
        # is a valid command, is an actionable verb, is composed of verb + noun
    updateState(userInput)