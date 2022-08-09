# -- Polymorphism -- 
# Greek God Morphism (Could change his look)
# add(1,2) or add(1,2,3) or add(1,2,[1,2,3])
# Different behaviors of the same function

# -- Self --
# The object being refered to
# Object reference

class Car:
    name = "A new class" # Instance (Synonym of object) variable, Atributes, Data
    color = None
    numberPlate = "DDDDYYMM"
    def display(self): # Instance method
        print(f"This car is {self.name} and the color is {self.color} and the numberplate contains {self.numberPlate}")

car1 = Car()
car1.name = "Tesla"
# car1.display()

# -- Cinstructor --
# classname() is a constructor
# Default contructor
# Non paramitarized constructor
# A constructor is a special method that inisializase an object (Creation + Putting the default variable/method)
class Car:
    def __init__(self): # Default constructor # Everything inside this function is an instance varible or default variable
        self.name = "A new car"
        self.color = "white"
        self.numberPlate = "DDDDYYMM"
        print('Hello')
    
    # Paramitarized constructor
    def __init__(self,carName, carColor, carNumberPlate):
        self.name = carName
        self.color = carColor
        self.numberPlate = carNumberPlate
        self.doors = 4
        self.windows = 5

    def display(self): # Instance method
        print(f"This car is {self.name} and the color is {self.color} and the numberplate contains {self.numberPlate}.\nIt has {self.doors} doors and {self.windows} windows.")

# car1 = Car()
# car2 = Car()
# car3 = Car()
# car4 = Car()
# car3.display()
# car1.name = "Tesla"
# car4.numberPlate = "fa;skdf"
# car4.name = "Tesla"
# car4.color = "Silver"
# car4.display()
car5 = Car("Ford","Red","BBBSSSS")
car5.windows = 6
car5.display()
car6 = Car("Ferrari","Blue","asfdasf")
# car6.display()