class Pokemon:
    def __init__(self,poke1Name,poke2Name,poke1Power,poke2Power,dameRate):
        self.pokemon1_name = poke1Name
        self.pokemon2_name = poke2Name
        self.pokemon1_power = poke1Power
        self.pokemon2_power = poke2Power
        self.damage_rate = dameRate
#Write your code for class here
team_pika = Pokemon('pikachu', 'charmander', 90, 60, 10)
print('=======Team 1=======')
print('Pokemon 1:',team_pika.pokemon1_name,team_pika.pokemon1_power)
print('Pokemon 2:',team_pika.pokemon2_name,team_pika.pokemon2_power)
pika_combined_power = (team_pika.pokemon1_power +team_pika.pokemon2_power) * team_pika.damage_rate
print('Combined Power:', pika_combined_power)
#Write your code for subtask 2,3,4 here
team_bulb = Pokemon('bulbasaur', 'squirtle', 80, 70,9)
print('=======Team 2=======')
print('Pokemon 1:',team_bulb.pokemon1_name,team_bulb.pokemon1_power)
print('Pokemon 2:',team_bulb.pokemon2_name,team_bulb.pokemon2_power)
pika_combined_power = (team_bulb.pokemon1_power +team_bulb.pokemon2_power) * team_bulb.damage_rate
print('Combined Power:', pika_combined_power)