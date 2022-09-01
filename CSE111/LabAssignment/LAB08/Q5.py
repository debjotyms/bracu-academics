class Exam:
    def __init__(self,marks):
        self.marks = marks
        self.time = 60
    def examSyllabus(self):
        return "Maths , English"
    def examParts(self):
        return "Part 1 - Maths\nPart 2 - English\n"

class ScienceExam(Exam):
  def __init__(self, marks, time, *args):
    super().__init__(marks)
    self.time = time
    self.args = args
    self.part = len(args) + 2
  def __str__(self):
    return f'Marks {self.marks} Time: {self.time} minutes Number of Parts: {self.part}'
  def examSyllabus(self):
    subs = super().examSyllabus() + ', '
    for a in self.args:
      subs += a+', '
    return subs[:-2]
  def examParts(self):
    lst = super().examParts()
    for b in range(len(self.args)):
      lst += 'Part '+str(b+3)+' - '+str(self.args[b])+'\n'
    return lst

engineering = ScienceExam(100,90,"Physics","HigherMaths")
print(engineering)
print('----------------------------------')
print(engineering.examSyllabus())
print(engineering.examParts())
print('==================================')
architecture = ScienceExam(100,120,"Physics","HigherMaths","Drawing")
print(architecture)
print('----------------------------------')
print(architecture.examSyllabus())
print(architecture.examParts())