class Cat:
    Number_of_cats = 0
    def __init__(self,color="White",action="sitting"):
        self.color = color
        self.action = action
        Cat.Number_of_cats+=1
    def changeColor(self,color):
        self.color = color
    @classmethod
    def no_parameter(cls):
        return cls("White","sitting")
    @classmethod
    def first_parameter(cls,color):
        return cls(color)
    @classmethod
    def second_parameter(cls,action):
        return cls("Grey",action)
    def printCat(self):
        print(f"{self.color} cat is {self.action}")

print("Total number of cats:", Cat.Number_of_cats)
c1 = Cat.no_parameter()
c2 = Cat.first_parameter("Black")
c3 = Cat("Brown", "jumping")
c4 = Cat("Red", "purring")
c5 = Cat.second_parameter("playing")
print("=======================")
c1.printCat()
c2.printCat()
c3.printCat()
c4.printCat()
c5.printCat()
c1.changeColor("Blue")
c3.changeColor("Purple")
c1.printCat()
c3.printCat()
print("=======================")
print("Total number of cats:", Cat.Number_of_cats)