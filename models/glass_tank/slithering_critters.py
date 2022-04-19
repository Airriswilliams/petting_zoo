

# python datetime module to help us create a timestamp
from datetime import date

class Rattlesnake:
    
    def __init__(self,name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.slithering = True
        self.date_added =  date.today()
        self.food = food
 
ricky_ratler = Rattlesnake("Ricky Ratler", "snake", "midday", "Mice")       
        

        
class RoughGreenSnake:
    
    def __init__(self):
        self.name = "Jake"
        self.species = "snake"
        self.slithering = True
        self.date_added =  date.today()
        
class MilkSnake:
    
    def __init__(self):
        self.name = "Milky"
        self.species = "snake"
        self.slithering = True
        self.date_added =  date.today()
        
class GopherSnake:
    
    def __init__(self):
        self.name = "Gerald Gopher"
        self.species = "snake"
        self.slithering = True
        self.date_added =  date.today()
        
class GreenSnake:
    
    def __init__(self):
        self.name = "Mister Green"
        self.species = "snake"
        self.slithering = True
        self.date_added =  date.today()