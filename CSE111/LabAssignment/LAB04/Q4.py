class Student():
  def __init__(self,name="default student"):
    self.name=name
    self.average=0

  def quizcalc(self,*args):
    sum=0
    for x in args:
      sum+=x
    self.average=sum/3

  def printdetail(self):
    print(f"Hello {self.name}")
    print(f"Your average quiz score is {self.average}")




s1 = Student()
s1.quizcalc(10)
print('--------------------------------')
s1.printdetail()
s2 = Student('Harry')
s2.quizcalc(10,8)
print('--------------------------------')
s2.printdetail()
s3 = Student('Hermione')
s3.quizcalc(10,9,10)
print('--------------------------------')
s3.printdetail()