

class Equipment:
    def __init__(self, dominanthand = None, righthand = None):
        self.dominanthand = dominanthand
        self.nondominanthand = righthand
    
    def __str__(self):
        return f"Your EQUIPMENT: \n Left Hand: {self.dominanthand}. \n Right Hand: {self.nondominanthand}.\n"
    
   