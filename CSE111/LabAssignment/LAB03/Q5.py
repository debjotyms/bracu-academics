class Shape:
    def __init__(self,shapeName,length,breath):
        self.shape = shapeName
        self.length = length
        self.breath = breath
    
    def area(self):
        if self.shape == "Triangle":
            area = (.5)*self.length*self.breath
            print("Area:",area)
        elif self.shape == "Square":
            area = self.length*self.breath
            print("Area:",area)
        elif self.shape == "Rhombus":
            area = (.5)*self.length*self.breath
            print("Area:",area)
        elif self.shape == "Rectangle":
            area = self.length*self.breath
            print("Area:",area)
        else:
            print("Area: Shape unknown")

triangle = Shape("Triangle",10,25)
triangle.area()
print("==========================")
square = Shape("Square",10,10)
square.area()
print("==========================")
rhombus = Shape("Rhombus",18,25)
rhombus.area()
print("==========================")
rectangle = Shape("Rectangle",15,30)
rectangle.area()
print("==========================")
trapezium = Shape("Trapezium",15,30)
trapezium.area()