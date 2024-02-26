class animal():
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Color: {self.color}, Age: {self.age}"

class cat(animal):
    def __init__(self, name, color, age, price):
        super().__init__(name, color, age)
        self.price = price
        self.weight = "5kg"
        print("Cat")
    
    def __str__(self):
        return f"Name: {self.name}, Color: {self.color}, Age: {self.age}, Price: {self.price}, Weight: {self.weight}"
    

    def make_sound(self):
        return f"Cat purred"
    
    def cute(self):
        print("Cats are cute")
    
class dog(animal):
    def __init__(self, name, color, age, price):
        super().__init__(name, color, age)
        self.price = price
        self.num = 3
        print("Dog")

    def __str__(self):
        return f"Name: {self.name}, Color: {self.color}, Age: {self.age}, Price: {self.price}, Numbers: {self.num}"

    def make_sound(self):
        return f"Dog barked"
    
    def cute(self):
        print("Dogs are the cutest animal of all time")

class bird(animal):
    def __init__(self, name, color, age, price):
        super().__init__(name, color, age)
        self.price = price
        print("Bird")

    def all(self, num):
        return f"Name: {self.name}, Color: {self.color}, Age: {self.age}, Price: {self.price}, Numbers: {num}"
    
    def make_sound(self):
        return f"Bird chirped"
    
    def cute(self):
        print("Bird are small and cute")

animal_cat = cat("Dar Dar", "white with black spots", "8", "250000 kyats")
print(animal_cat)
print(animal_cat.make_sound())
animal_cat.cute()

print()
print("💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛💛")
print()

animal_dog = dog("Bar Bar", "brown", "5", "800000 kyats")
print(animal_dog)
print(animal_dog.make_sound())
animal_dog.cute()

print()
print("🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍")
print()


animal_bird = bird("Har Har", "yellowish", "3", "500000 kyats")
print(animal_bird.all(5))
print(animal_bird.make_sound())
animal_bird.cute()




