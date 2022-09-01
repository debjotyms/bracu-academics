class RealNumber:
    def __init__(self, number=0):
        self.number = number
    def __add__(self, anotherRealNumber):
        return self.number + anotherRealNumber.number
    def __sub__(self, anotherRealNumber):
        return self.number - anotherRealNumber.number
    def __str__(self):
        return str(self.number)

class ComplexNumber(RealNumber):
  def __init__(self, r, i):
    if type(r)==type(1):
      super().__init__(r)
      self.i = i
    else:
      super().__init__(r.number)
      self.i = i
  def __add__(self, aNumber):
    if self.i + aNumber.i >= 0:
      return f'{super().__add__(aNumber)} + {self.i + aNumber.i}i'
    else:
      return f'{super().__add__(aNumber)} - {abs(self.i + aNumber.i)}i'
  def __sub__(self, aNumber):
    if self.i> aNumber.i:  
      return f'{super().__sub__(aNumber)} + {self.i - aNumber.i}i'
    else:
      return f'{super().__sub__(aNumber)} - {abs(self.i - aNumber.i)}i'
  def __str__(self):
    return f'{self.number} + {self.i}i'

r1 = RealNumber(3)
r2 = RealNumber(5)
print(r1+r2)
cn1 = ComplexNumber(2, 1)
print(cn1)
cn2 = ComplexNumber(r1, 5)
print(cn2)
cn3 = cn1 + cn2
print(cn3)
cn4 = cn1 - cn2
print(cn4)