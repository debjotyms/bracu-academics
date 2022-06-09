# -- Mutability --
# Mutable Objects: list, dict, set
# Immutable Objects: String, tuple

tpl = (1,2,[1,2,3])
tpl[2].append(4) # The list inside the tuple is mutable

# Ordered: list, tuple
# Unordered: set, dictionary
# That's why we can't use indexing in set and dictionary
set1 = {2,'3',1}
# print(set1)
dict = {1:2,4:5,0:3} # After python3.7, the dictionary is now ordered
# print(dict)

# Add items to set
set1 = {1,2,3}
set1.add(4)
set1.update([5,6]) # Argument must be a list
# print(set1)

# -- Introduction to OOP --
# Todays Lecture
    # Concept of OOP
    # Pillars of OOP
    # Class (Blueprint of Template)
    # Object (Real thing of that Blueprint)
# SPL and OOP (Follows an template)
# Book: The Python Crash Course (2nd Editon)

# -- Concept of OOP --
# We are inheritanting our genetic behavior
# Reusable code

# -- Pillars of OOP --
    # Object/Instance
    # Class
    # Polymorphism
    # Abstraction
    # Inheritance
    # Encapsulation

# -- Class --
# It's a blueprint of the object we will create
# Class components
    # Data (The arrtributes about it)
        # driver_name
        # num_passenger
    # Behavior (The methods())
        # pick_up_passanger()

# -- Method --
# It's like a Python function.
# Must be called on a object.
# It must put it inside a class.
# A method has a name, ans may take parameters ans have a return statement.
set1 = set()
set2 = set()
set2.union(set1) # Called the method using it's object.

# -- Encapsulation --
# Not disturbing other objects Atributes ans Behviors.
# Like the capsule.

# -- How to create a class --
# First letter of the name of a class should be a capital letter.
class Car:
    def __init__(self):
        pass
    name = "A new car" # Default name
    color = None # Default color
    
    def display(self):
        print(self.name)

car1 = Car() # None parameterized constructor # Default Constructor?
car2 = Car()
car1.color = "Blue"
print(car1.color)
print(car2.color) # Encapsulatoin in action
car1.display()