class Football:

  def __init__(self, team_name, name, role):
    self.__team = team_name
    self.__name = name
    self.role = role
    self.earning_per_match = 0

  def get_name_team(self):
    return 'Name: '+self.__name+', Team Name: ' +self.__team

class Player(Football):
  def __init__(self, team_name, name, role, tGoal, tPlayed):
    super().__init__(team_name, name, role)
    self.tGoal = tGoal
    self.tPlayed = tPlayed
    self.earning_per_match = (self.tGoal*1000)+(self.tPlayed*10)
  def calculate_ratio(self):
    self.ratio = self.tGoal/self.tPlayed
  def print_details(self):
    print(f'{self.get_name_team()}')
    print(f'Team Role: {self.role}')
    print(f'Total Goal: {self.tGoal}, Total Played: {self.tPlayed}')
    print(f'Goal Ratio: {self.ratio}')
    print(f'Match Earning: {self.earning_per_match}K')
class Manager(Football):
  def __init__(self, team_name, name, role, win):
    super().__init__(team_name, name, role)
    self.win = win
    self.earning_per_match = self.win*1000
  def print_details(self):
    print(f'{self.get_name_team()}')
    print(f'Team Role: {self.role}')
    print(f'Total Win: {self.win}')
    print(f'Match Earning: {self.earning_per_match}K')

player_one = Player('Juventus', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()