# Method Resoluton Order (MRO)
# Overloading vs Overridding
class Father:
    gender = "Male"
    hair_color = "Black"

class Mother:
    gender = "Female"
    # hair_color = "Red"

class Child(Mother, Father): # Evaluated from left to right
    hair_color = "Brown"
    def print_details(self):
        print(f"Gender : {self.gender}")
        print(f"Hair Color : {self.hair_color}")

c = Child()
c.print_details()