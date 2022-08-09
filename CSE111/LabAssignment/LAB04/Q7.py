class Match:
  def __init__(self,n):
    self.name=n
    print("5..4..3..2..1.. Play !!!")
    team=n.split("-")
    self.first=team[0]
    self.second=team[1]
    self.runs=0
    self.overs=0
    self.wicket=0

  def add_run(self,r):
    self.runs+=r

  def add_over(self,over):
    
    if (self.overs+over)>5:
      print("Warning! Cannot add 5 over/s (5 over match)") 
    else:
      self.overs+=over

  def add_wicket(self,w):
    self.wicket+=w

  def print_scoreboard(self):
    return(f"""Batting Team: {self.first}
Bowling Team: {self.second}
Total Runs: {self.runs} Wickets: {self.wicket} Overs: {self.overs} """)



match1 = Match("Rangpur Riders-Cumilla Victorians")
print("=========================")
match1.add_run(4)
match1.add_run(6)
match1.add_over(1)
print(match1.print_scoreboard())
print("=========================")
match1.add_over(5)
print("=========================")
match1.add_wicket(1)
print(match1.print_scoreboard())