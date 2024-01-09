

class Equipment:
    def __init__(self, dominanthand = None, nondominanthand = None):
        self.dominanthand = dominanthand
        self.nondominanthand = nondominanthand
    
    def __str__(self):
        return f"Your EQUIPMENT: \n Dominant Hand: {self.dominanthand}. \n Non Dominant Hand: {self.nondominanthand}.\n"
    
   