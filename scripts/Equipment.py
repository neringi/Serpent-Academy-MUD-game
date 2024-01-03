
class Equipment:
    def __init__(self, lefthand = None, righthand = None):
        self.lefthand = lefthand
        self.righthand = righthand
    
    # def getLeftHand(): 
    #     return self.equipment.get("lefthand")
    # def setLeftHand(self, item):
    #     self.equipment["lefthand"] = item
    def __str__(self):
        return f"Your EQUIPMENT: \n Left Hand: {self.lefthand}. \n Right Hand: {self.righthand}.\n"