# Creating factory method using classmethod
# Factory Method: A method that preprocesses before creating an object
# classname === cls === type(self) 
# Design pattern - SWE Course - GoF Book

# class Student:
#     uni_name = "BRACU"
#     def __init__(self,name,ID):
#         self.name = name
#         self.ID = ID
    
#     def details(self):
#         print(f"Student Name : {self.name}")
#         print(f"Student ID : {self.ID}")
#         print(f"University Name : {Student.uni_name}")
#         print("========================")

#     @classmethod
#     def update_uni_name(cls,new_uni_name):
#         Student.uni_name = new_uni_name

#     @classmethod
#     def from_string(cls,student_info):
#         s_name, s_ID = student_info.split("-")
#         return cls(s_name,s_ID)

# s1 = Student("John",123)
# s1.details()

# s2 = Student("Mary",456)
# s2.details()

# s3 = Student.from_string("Susan-910")
# s3.details()

# ------ Inheritance ------
# Types of inheritance
    # Single inheritance (Parent class / Base class / Super class - Child class / Sub class)
    # Multi-level inheritance (Grand Parent - Father - Child)
    # Multiple inheritance (Father + Mother = Child)
    # Hybrid (Multi-level + Multiple)

# class A:
# class B(A): # Class B inheritse from class A

class Parent:
    title = "Khan"
    def func1(self):
        print("Inside Parent Class")
    def func4(self):
        print("Inside Parent Class")

class Child(Parent): # Child class Inherites from Parent class
    __title = "Ullah"
    def func2(self):
        print("Inside Child Class")

class GrandChild(Child): # GrandChild class Inherites from Child class
    def func2(self):
        print("GrandChild")

p1 = Parent()
p1.func1()
c1 = Child()
c1.func1()
gc1 = GrandChild()
gc1.func2()
print(gc1.title)