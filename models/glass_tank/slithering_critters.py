

# python datetime module to help us create a timestamp
from datetime import date

class Rattlesnake:
    
    def __init__(self,name, species, shift, food, chip_num):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.__chip_number = chip_num
        self.slithering = True
        self.date_added =  date.today()
        
    @property
    def chip_number(self):
        return self.__chip_number
    
    @chip_number.setter
    def chip_number(self,num):
        pass
 
ricky_ratler = Rattlesnake("Ricky Ratler", "snake", "midday", "Mice", 12345) 
print(ricky_ratler.chip_number)      

        

        
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