class Shinobi:
    def __init__(self,name,rank):
        self.mission = 0
        self.salary = 0
        self.name = name
        self.rank = rank
    
    def calSalary(self,mission):
        self.mission = mission
        if self.rank == "Genin":
            self.salary = mission*50
        elif self.rank == "Chunin":
            self.salary = mission*100
        else:
            self.salary = mission*500
    
    def changeRank(self,newRank):
        self.rank = newRank
    def printInfo(self):
        print(f"Name: {self.name}")
        print(f"Rank: {self.rank}")
        print(f"Number of mission: {self.mission}")
        print(f"Salary: {self.salary}")


naruto = Shinobi("Naruto", "Genin")
naruto.calSalary(5)
naruto.printInfo()
print('====================')
shikamaru = Shinobi('Shikamaru', "Genin")
shikamaru.printInfo()
shikamaru.changeRank("Chunin")
shikamaru.calSalary(10)
shikamaru.printInfo()
print('====================')
neiji = Shinobi("Neiji", "Jonin")
neiji.calSalary(5)
neiji.printInfo()