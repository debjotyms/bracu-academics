class Dolls:
    def __init__(self,name,price):
        self.name = name
        self.price = price
        self.compound = False
    def detail(self):
        if self.compound:
            return f"Dolls: {self.name}\nTotal Price: {self.price} taka"
        else:
            return f"Doll: {self.name}\nTotal Price: {self.price} taka"
    def __gt__(self,other):
        return self.price>other.price
    def __add__(self,other):
        obj = Dolls(f"{self.name} {other.name}",(self.price+other.price))
        obj.compound = True
        return obj

obj_1 = Dolls("Tweety", 2500)
print(obj_1.detail())
if obj_1 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_2 = Dolls("Daffy Duck", 1800)
print(obj_2.detail())
if obj_2 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_3 = Dolls("Bugs Bunny", 3000)
print(obj_3.detail())
if obj_3 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_4 = Dolls("Porky Pig", 1500)
print(obj_4.detail())
if obj_4 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")
print("=========================")
obj_5 = obj_2 + obj_3
print(obj_5.detail())
if obj_5 > obj_1:
    print("Congratulations! You get the Tweety as a gift!")
else:
    print("Thank you!")