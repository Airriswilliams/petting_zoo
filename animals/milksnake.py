from animals.animals import Animal

class MilkSnake (Animal):
    
    def __init__(self,name,species,shift,food,chip_num):
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        
        
        
    def __str__(self):
        return f"{self.name} is a {self.species}"