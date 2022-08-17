class Student:
  totalStudents = 0
  bracuStudents = 0
  otherStudents = 0
  def __init__(self, name, dept, institute = 'Brac University'):
    self.name = name
    self.dept = dept
    self.institute = institute
    Student.totalStudents += 1
    if self.institute == 'Brac University':
      Student.bracuStudents += 1
    else:
      Student.otherStudents += 1
  @classmethod
  def printDetails(cls):
    print(f'Total Student(s): {Student.totalStudents}\nBRAC University Student(s): {Student.bracuStudents}\nOther Institution Student(s): {Student.otherStudents}')
  @classmethod
  def createStudent(cls, name, dept, institute = 'Brac University'):
    return Student (name, dept, institute)
  def  individualDetail(self):
    print(f'Name: {self.name}\nDepartment: {self.dept}\nInstitution: {self.institute}')

Student.printDetails()
print('#########################')

mikasa = Student('Mikasa Ackerman', "CSE")
mikasa.individualDetail()
print('------------------------------------------')
Student.printDetails()

print('========================')

harry = Student.createStudent('Harry Potter', "Defence Against Dark Arts", "Hogwarts School")
harry.individualDetail()
print('-------------------------------------------')
Student.printDetails()

print('=========================')

levi = Student.createStudent("Levi Ackerman", "CSE")
levi.individualDetail()
print('--------------------------------------------')
Student.printDetails()