class StudentDatabase:
    def __init__(self,name,sid):
        self.name = name
        self.sid = sid
        self.grades = {}
    
    def calculateGPA(self,courseList,semester):
        tempDict = {}
        courseNameList = []
        gpaList = []
        for courseNames in courseList:
            lst = courseNames.split(":")
            courseNameList.append(lst[0].strip())
            gpaList.append(float(lst[1]))
        CGPA = (sum(gpaList))/len(gpaList)
        courseNameList = tuple(courseNameList)
        tempDict[courseNameList] = round(CGPA,2)
        self.grades[semester] = tempDict
    
    def printDetails(self):
        print(f"Name: {self.name}")
        print(f"ID: {self.sid}")
        for semesters in self.grades.keys():
            print(f"Courses taken in {semesters}:")
            for coureName in self.grades[semesters]:
                for courses in coureName:
                    print(courses)
                print(f"GPA: {self.grades[semesters][coureName]}")

        
s1 = StudentDatabase('Pietro', '10101222')
s1.calculateGPA(['CSE230: 4.0', 'CSE220: 4.0', 'MAT110: 4.0'],'Summer2020')
s1.calculateGPA(['CSE250: 3.7', 'CSE330: 4.0'], 'Summer2021')
print(f'Grades for {s1.name}\n{s1.grades}')
print('-----------------------------------------------')
s1.printDetails()
s2 = StudentDatabase('Wanda', '10103332')
s2.calculateGPA(['CSE111: 3.7', 'CSE260: 3.7', 'ENG101: 4.0'],'Summer2022')
print('-----------------------------------------------')
print(f'Grades for {s2.name}\n{s2.grades}')
print('-----------------------------------------------')
s2.printDetails()