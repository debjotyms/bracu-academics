class Shape:
  def __init__(self, name='Default', height=0, base=0):
    self.area = 0
    self.name = name
    self.height = height
    self.base = base

  def get_height_base(self):
    return "Height: "+str(self.height)+",Base: "+str(self.base)

class triangle(Shape):
    def __init__(self,name = "Default",height=0,base=0):
        super().__init__(name,height,base)
    def calcArea(self):
        self.area = 0.5 * self.height * self.base
        return self.area
    def printDetail(self):
        firstpart = super().get_height_base()
        secondpart = "Shape Name: " + str(self.name) + "\n" + firstpart + "\n" + "Area: " + str(self.area)
        return secondpart

class trapezoid(Shape):
    def __init__(self,name,height,base,side):
        super().__init__(name,height,base)
        self.side = side
    def calcArea(self):
        self.area = ((self.side + self.base)/2) * self.height
        return self.area
    def printDetail(self):
        firstpart = super().get_height_base()
        secondpart = "Shape Name: " + str(self.name) + "\n" + firstpart + " Side_A: " + str(self.side) + "\n" + "Area: " + str(self.area)
        return secondpart

tri_default = triangle()
tri_default.calcArea()
print(tri_default.printDetail())
print('--------------------------')
tri = triangle('Triangle', 10, 5)
tri.calcArea()
print(tri.printDetail())
print('---------------------------')
trap = trapezoid('Trapezoid', 10, 6, 4)
trap.calcArea()
print(trap.printDetail())