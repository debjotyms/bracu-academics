# The use of super()
# Super points directly to the immediate parent
# Mostly used to call parent class method;
# specially calling parents's __init__()

# class Father:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     def print_details(self):
#         print("Inside Father class")
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")

# f1 = Father("John",45)
# f1.print_details()
# print("========================")

# class Son(Father):
#     def __init__(self, name, age, tech):
#         super().__init__(name, age)
#         self.tech = tech
    
#     def print_details(self):
#         print("Inside Son class")
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Technology: {self.tech}")

# s1 = Son("Jasson", 30, "Python")
# s1.print_details()

# class Grandson(Son):
#     def __init__(self,name,age,tech,pet):
#         Father.__init__(self, name,age)
#         self.tech = tech
#         self.pet = pet
    
#     def print_details(self):
#         print("Inside Grandson class")
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Technology: {self.tech}")
#         print(f"Pet {self.pet}")

# print("========================")

# g1 = Grandson("Jonnas", 6, "Java", "Nanobot")
# g1.print_details()



# ====== Abstraction ======
# A class becomes a abstract class if it has atleast one abstract method
# Abstract method = Has name and arguments but no body(Definition)(Pass)
# An abstact class (normally) can not initialize an object
# Python is an exception

from abc import ABC, abstractmethod

class Shape:
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def calculateArea(self, *dimension):
        pass
    # def printDetails(self):
    #     print(f"{self.name} has area of {self.calculateArea()}")

class Rectangle(Shape):
    def calculateArea(self, *dimension):
        length, weight = dimension[0], dimension[1]
        return length * weight

class Triangle(Shape):
    def calculateArea(self, *dimension):
        base, height = dimension[0], dimension[1]
        return base * height * .5

rec1 = Rectangle("square")
rec1Area = rec1.calculateArea(5,4)
print(rec1Area)

print(isinstance(rec1,Shape))
print(issubclass(Shape,Rectangle))