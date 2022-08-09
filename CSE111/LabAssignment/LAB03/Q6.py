class Calculator:
    def __init__(self):
        print("Calculator is ready!")
        self.first = 0
        self.second = 0
        self.operator = ""
    def calculate(self,first,second,operator):
        self.first = first
        self.second = second
        self.operator = operator
        if self.operator == "+":
            return self.first+self.second
        elif self.operator == "-":
            return self.first-self.second
        elif self.operator == "*":
            return self.first*self.second
        elif self.operator == "/":
            return self.first/self.second
    def showCalculation(self):
        if self.operator == "+":
            print(f"{self.first} + {self.second} = {self.first + self.second}")
        elif self.operator == "-":
            print(f"{self.first} - {self.second} = {self.first - self.second}")
        elif self.operator == "*":
            print(f"{self.first} * {self.second} = {self.first * self.second}")
        elif self.operator == "/":
            print(f"{self.first} / {self.second} = {self.first / self.second}")


c1 = Calculator()
print("==================")
val = c1.calculate(10, 20, '+')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 10, '-')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 5, '*')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 16, '/')
print("Returned value:", val)
c1.showCalculation()