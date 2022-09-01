class Shape3D:
  pi = 3.14159
  def __init__(self, name = 'Default', radius = 0):
    self._area = 0
    self._name = name
    self._height = 'No need'
    self._radius = radius   
  def calc_surface_area(self):
    return 2 * Shape3D.pi * self._radius
  def __str__(self):
      return "Radius: "+str(self._radius)

class Sphere(Shape3D):
  def __init__(self, name, rad):
    super().__init__(name, rad)
    print(f'Shape name: {self._name}, Area Formula: 4 * pi * r * r')
  def calc_surface_area(self):
     self.area = super().calc_surface_area() * 2 * self._radius
  def __str__(self):
    s1 = super().__str__() + ' Height: ' + str(self._height)
    return s1+'\n'+'Area: '+ str(self.area)

class Cylinder(Shape3D):
  def __init__(self, name, rad, height):
    super().__init__(name, rad)
    self._height = height
    print(f'Shape name: {self._name}, Area Formula: 2 * pi * r * (r + h)')
  def calc_surface_area(self):
    self.area = super().calc_surface_area() * (self._radius+self._height)
  def __str__(self):
    s1 = super().__str__() + ' Height: ' + str(self._height)
    return s1+'\n'+'Area: '+ str(self.area)

sph = Sphere('Sphere', 5)
print('----------------------------------')
sph.calc_surface_area()
print(sph)
print('==================================')
cyl = Cylinder('Cylinder', 5, 10)
print('----------------------------------')
cyl.calc_surface_area()
print(cyl)