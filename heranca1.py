import animal

class Gato(animal.Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
        
class Cachorro(animal.Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
       
class Coelho(animal.Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)