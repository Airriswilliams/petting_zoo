
class Attraction:
    
    def __init__(self, name, desctiption):
        self.attraction_name = name
        self.description = desctiption
        self.animals = list()
        
    def add_animal(self,animal):
        self.animals.append(animal)
        
    def remove_animal(self, animal):
        self.animals.remove(animal)
        
    def __str__(self):
        return f'{self.attraction_name} ({len(self)} animals)'
    
    def __len__(self):
        return len(self.animals)