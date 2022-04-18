from models import ShireHorse, Rattlesnake

class PettingZoo:

    def __init__(self, attraction_name, description):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = list()
        
henry = ShireHorse("Henry", "domestic pig", "midday", "Horse Chow")


varmint_village = PettingZoo("Varmint Village", "cute and fuzzy critters to cuddle") 
varmint_village.animals.append(henry)   
for animal in varmint_village.animals:
    print(animal.name)

        

class SnakePit:

    def __init__(self, attraction_name, description):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = list()
        
ricky_ratler = Rattlesnake("Ricky Ratler", "snake", "midday", "Mice")       
        
slither_inn = SnakePit("Slither Inn", "home of the friendly snakes")
slither_inn.animals.append(ricky_ratler)
for animal in slither_inn.animals:
    print(animal.name)


        

class Wetlands:

    def __init__(self, attraction_name, description, animals):
        self.attraction_name = attraction_name
        self.description = description
        self.animals = list(animals)