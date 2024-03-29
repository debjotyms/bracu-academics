class Student:
    def __init__(self,name,id,department,gpa):
        self.name = name
        self.id = id
        self.department = department
        self.gpa = gpa
    def calculate_CGPA(self):
        self.numberOfCourses = len(self.gpa)
        self.totalCgpa = 0
        for eachGpa in self.gpa:
            self.totalCgpa+=(eachGpa*3)
        self.totalCgpa = self.totalCgpa/(3*self.numberOfCourses)
    def print_details(self):
        print(f"Name: {self.name}, ID: {self.id}")
        print(f"Department: {self.department}")
        print(f"CGPA: {self.totalCgpa}")

        if self.totalCgpa>3.80:
            print(f"Your academic standing is 'Highest Distinction'")
        elif self.totalCgpa>3.65:
            print(f"Your academic standing is 'High Distinction'")
        elif self.totalCgpa>3.50:
            print(f"Your academic standing is 'Distinction'")
        elif self.totalCgpa>2.00:
            print(f"Your academic standing is 'Satisfactory'")
        else:
            print(f'Sorry, you cannot graduate')


s1 = Student('Dora', '15995599','CSE', [4,3.7,3.7,4])
s1.calculate_CGPA()
print("==========================")
s1.print_details()
print("==========================")
s2 = Student('Pingu', '12312322', 'EEE', [1.7,1.3,1.3,1.3,1])
s2.calculate_CGPA()
print("==========================")
s2.print_details()
print("==========================")
s3 = Student('Bob', '13311331', 'CSE', [2,3,3,3.7,2.7,2.7])
s3.calculate_CGPA()
print("==========================")
s3.print_details()