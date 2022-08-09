class Calculator:
    def __init__(self,numberA,operator,numberB):
        self.numberA = numberA
        self.numberB = numberB
        print("Let's Calculate!")
    def add(self):
        print(f"Value 1: {numberA}")
        print(f"Operator: {operator}")
        print(f"Value 1: {numberB}")
        self.result = self.numberA + self.numberB
        print(f"Result: {self.result}")
    def subtract(self):
        print(f"Value 1: {numberA}")
        print(f"Operator: {operator}")
        print(f"Value 1: {numberB}")
        self.result = self.numberA - self.numberB
        print(f"Result: {self.result}")
    def multiply(self):
        print(f"Value 1: {numberA}")
        print(f"Operator: {operator}")
        print(f"Value 1: {numberB}")
        self.result = self.numberA * self.numberB
        print(f"Result: {self.result}")
    def divide(self):
        print(f"Value 1: {numberA}")
        print(f"Operator: {operator}")
        print(f"Value 1: {numberB}")
        self.result = self.numberA / self.numberB
        print(f"Result: {self.result}")

numberA = int(input())
operator = input()
numberB = int(input())
tempObject = Calculator(numberA, operator, numberB)

if operator == '+':
    tempObject.add()
elif operator == '-':
    tempObject.subtract()
elif operator == '*':
    tempObject.multiply()
elif operator == '/':
    tempObject.divide()