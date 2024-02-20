# Class and inheritance homework 

#  1. Create a Vehicle class with attributes (name, color, max_speed)
#  2. Add printAll() method to print all data of Vehicle class

#  3. Create a Car class that inherited from Vehicle class
#  4. Add attribute price in Car class
#  5. Add description() method to print string “this is a car”
#  6. Add printAll() method to print all data of Car class

#  7. Create a Bike class that inherited from Vehicle class
#  8. Add description() method to print string “this is a bike”

#  9. Create an object from Car class, and call description method and printAll method

#  10. Create an object from Bike class, and call description method and printAll method

#  11. Print object of Car class

class Vehicle():
    def __init__(self, name, color, max_speed):
        self.name = name
        self.color = color
        self.max_speed = max_speed

    def __str__(self):
        f"{self.name}, {self.color}, {self.max_speed}"

    def description(self):
        print("This is a vehicle")

    def printAll(self):
        print(f"Name: {self.name}, Color: {self.color}, Max_speed: {self.max_speed}")
        
class Car(Vehicle):
    def __init__(self, name, color, max_speed, price):
        super().__init__(name, color, max_speed)
        Vehicle.__init__(self, name, color, max_speed)
        self.price = price
    
    def __str__(self):
        return f"{self.name}, {self.color}, {self.max_speed}, {self.price}"

    def description(self):
        print("This is a car")

    def printAll(self):
        super().printAll()
        print(f"Price: {self.price}")

class Bike(Vehicle):
    def __init__(self, name, color, max_speed):
        super().__init__(name, color, max_speed)
    
    def description(self):
        print("This is a bike")

car_class = Car("BMW", "black", 250, 139975)
car_class.description()
car_class.printAll()


print()

bike_class = Bike("Cannondale", "red", 45.06)
bike_class.description()
bike_class.printAll()

bike_class2 = Bike("Cannondale2", "red", 45.06)
bike_class2.description()

print()
print(car_class)

# len(string)
# len(tuple)
# len(dictionary)



    




    
