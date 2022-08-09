class Joker:
    def __init__(self,name,power,is_he_psycho):
        self.name = name
        self.power = power
        self.is_he_psycho = is_he_psycho
#=================================================================
j1 = Joker('Heath Ledger', 'Mind Game', False)
print(j1.name)
print(j1.power)
print(j1.is_he_psycho)
print('====================')
j2 = Joker('Joaquin Phoenix', 'Laughing out Loud', True)
print(j2.name)
print(j2.power)
print(j2.is_he_psycho)
print('====================')
if j1 == j2:
    print('same')
else:
    print('different')
j2.name = 'Heath Ledger'
print(j1,j2)
if j1.name == j2.name:
    print('same')
else:
    print('different')
#=================================================================
explainA = """In the first if/else block, we are actually comparing object j1's memory location 
with object j2's memory location and oviously they are not same. That's why we are getting the output 'different'."""
explainB = """In the second if/else block, we are comparing the values of j1.name and j2.name and they are same. 
That's why we are getting output 'same'"""
print(explainA,explainB)