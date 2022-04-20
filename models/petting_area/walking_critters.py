
# python datetime module to help us create a timestamp
from datetime import date

class ShireHorse:

    def __init__(self, name, species, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()
        self.food = food
        
henry = ShireHorse("Henry", "horse", "midday", "Horse Chow")

def feed(self):
    print(f'{self.name} was fed {self.food} on {self.today().strftime("%m/%d/%Y")}')
    
def __str__(self):
    return f"{self.name} is a {self.species}"


        
class ClydesdaleHorse:

    def __init__(self, name, species, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()
        self.food = food
        
clyde_drexler = ClydesdaleHorse("Clyde Drexler", "horse", "midday", "Horse Chow")

class TamworthPig:

    def __init__(self,name, species, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added =  date.today()
        self.food = food
        
tammy = TamworthPig("Tammy", "pig", "morning", "Pig Slaw")
        
class HampshirePig:

    def __init__(self,name, species, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added = date.today()
        self.food = food
        
hammy = HampshirePig("Hammy", "pig", "lateday", "Pig Slaw")
        
class Llama:

    def __init__(self,name, species, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.shift = shift
        self.walking = True
        self.date_added =  date.today()
        self.food = food
        
miss_fuzz = Llama("Miss Fuzz","domestic llama", "lateday", "Llama Chow")
        