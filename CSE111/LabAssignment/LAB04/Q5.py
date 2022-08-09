class Student():
  def __init__(self,name,id,dep="CSE"):
    self.name=name
    self.id=id
    self.dep=dep
    self.hr=0

  def dailyEffort(self,hr):
    self.hr=hr
    
  def printDetails(self):
    print(f"Name: {self.name}")
    print(f"ID: {self.id}")
    print(f"Department: {self.dep}")
    print(f"Daily Effort: {self.hr} hour(s)")
    if self.hr<=2:
        print("Suggestion: Should give more effort!")
    elif self.hr<=4:
        print("Suggestion: Keep up the good work!")
    else:
        print("Suggestion: Excellent! Now motivate others.")
   





harry = Student('Harry Potter', 123)
harry.dailyEffort(3)
harry.printDetails()
print('========================')
john = Student("John Wick", 456, "BBA")
john.dailyEffort(2)
john.printDetails()
print('========================')
naruto = Student("Naruto Uzumaki", 777, "Ninja")
naruto.dailyEffort(6)
naruto.printDetails()