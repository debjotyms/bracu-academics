# Task_1
# class Cookies:
#     def __init__(self):
#         self.Shape = 'Round'
#         self.Taste = 'Sweet'

# SweetNRound = Cookies()
# SpiceNSquare = Cookies()
# SpiceNSquare.Shape = 'Square'
# SpiceNSquare.Taste = 'Spicy'
# print(SweetNRound.Shape + " and " + SweetNRound.Taste)
# print(SpiceNSquare.Shape + " and " + SpiceNSquare.Taste)

# Task_2
# class Cookies:
#     def __init__(self,shape,taste):
#         self.Shape = shape
#         self.Taste = taste

# TriNSour = Cookies("Triangle","Sour")
# print(TriNSour.Shape + " and " + TriNSour.Taste)


# -- Function Overloading -- Polymorphism --

# Positional Aproach
def add(num1,num2=2): # Arguments # Positional Arguments
    sum = num1+num2
    return sum
sum_res = add(1) # Parameters

def add(*cat):
    return cat
# print(add(1,2,4))

# Keyword Aproach
def add(num1,num2,num3=30): # Positional non-posional mixture
    return num1+num2+num3

print(add(10,20,0)) # Must be in key-value pair

# (non-default, default)
########################**kwargs#########################