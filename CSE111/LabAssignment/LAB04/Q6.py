class Patient():
  def __init__(self,name,age):    
    self.name=name
    self.age=age
    self.sym=""

  def add_Symptom(self,*args):
    self.sym=",".join(args)


  def printPatientDetail(self):
    print(f"Name: {self.name}")
    print(f"Age: {self.age}")
    print(f"Symptoms: {self.sym}")

p1 = Patient("Thomas", 23)
p1.add_Symptom("Headache")
p2 = Patient("Carol", 20)
p2.add_Symptom("Vomiting", "Coughing")
p3 = Patient("Mike", 25)
p3.add_Symptom("Fever", "Headache", "Coughing")
print("=========================")
p1.printPatientDetail()
print("=========================")
p2.printPatientDetail()
print("=========================")
p3.printPatientDetail()