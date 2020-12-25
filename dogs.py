class Dog():
    attr1 = 'mamal'
    attr2 = 'dog'
    
    def func(self):
        print(f"I'm a {self.attr1}")
        print(f"I'm a {self.attr2}")

    
class Person:
    def __init__(self, name):
        self.name = name
    
    def say_hi(self):
        print(f'Hello my name is {self.name}')
        
        
class SuperDog:
    
    animal = 'dog'
    
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color
       