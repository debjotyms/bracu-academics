class RealNumber:
    def __init__(self, r=0):
        self.__realValue = r
    def getRealValue(self):
        return self.__realValue
    def setRealValue(self, r):
        self.__realValue = r
    def __str__(self):
        return 'RealPart: '+str(self.getRealValue())

class ComplexNumber(RealNumber):
    def __init__(self,r=1.0,i=1.0):
        super().__init__(float(r))
        self.img = float(i)
    def __str__(self):
        print (f"RealPart: {(self.getRealValue())}")
        return f"ImaginaryPart: {self.img}"

cn1 = ComplexNumber()
print(cn1)
print('---------')
cn2 = ComplexNumber(5,7)
print(cn2)