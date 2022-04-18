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
        
henry = ShireHorse("Henry", "domestic pig", "midday", "Horse Chow")

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
        
        
        
class Goldfish:

    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = "Goldy"
        self.species = "fish"
        self.swimming = True
        self.date_added =  date.today()
        
class Mallard:

    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = "Mason"
        self.species = "fish"
        self.swimming = True
        self.date_added =  date.today()
        
class RainbowTrout:

    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = "Lucky Charm"
        self.species = "fish"
        self.swimming = True
        self.date_added =  date.today()
        
class Bluegrill:

    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = "Bishop Blue"
        self.species = "fish"
        self.swimming = True
        self.date_added =  date.today()
        
        
class Pumpkinseed:

    def __init__(self):
        # Establish the properties of each animal
        # with a default value
        self.name = "Patrick"
        self.species = "fish"
        self.swimming = True
        self.date_added =  date.today()
        
# golden_beauty = ShireHorse()
# winners_circle = ClydesdaleHorse()
# hampton =TamworthPig()
# steward = HampshirePig()
# miss_fuzz = Llama()
# sneaky_steve = Rattlesnake()
slither_sam = RoughGreenSnake()
cobra_kris = MilkSnake()
mister_slither = GopherSnake()
jackson = GreenSnake()
goldy = Goldfish()
tyson = Mallard()
ricky_rainbow = RainbowTrout()
bary_blue = Bluegrill()
nate_rob = Pumpkinseed()