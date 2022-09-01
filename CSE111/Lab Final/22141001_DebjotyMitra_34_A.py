class Candidates:
    candidates={}
    candidateNo = 0
    def __init__(self,name,add,phoneNo,exp,dob):
        self.name = name
        self.address = add
        self.phoneNo = phoneNo
        self.experience = exp
        self.dateOfBirth = dob
      
    def addCandidate(self,info):
        Candidates.candidates[self.ID]= info
    def __str__(self):
        return "Name: {}\nAddress: {}\nPhone No: {}\nExperience: {}\nDate of Birth: {}".format(self.name,self.address,self.phoneNo,self.experience,self.dateOfBirth)

class Candidates_2022(Candidates):
    def __init__(self,name,add,phoneNo,exp,dob,*langs):
        super().__init__(name,add,phoneNo,exp,dob)
        self.langs = langs
        Candidates.candidateNo+=1
        lst = [name,add,phoneNo,exp,dob]
        for l in langs:
            lst.append(l)
            
        self.ID = str("2022C-"+str(Candidates.candidateNo))
        super().addCandidate(lst)
    
    def createCandidate(self,name,add,phoneNo,exp,dob,*langs):
        return Candidates_2022(self,name,add,phoneNo,exp,dob,*langs)
    
    def __str__(self):
        tempLangs = ""
        for lang in self.langs:
            tempLangs = tempLangs+lang+','
        return "Name: {}\nAddress: {}\nPhone No: {}\nExperience: {}\nDate of Birth: {}\nProgramming Languages: {}".format(self.name,self.address,self.phoneNo,self.experience,self.dateOfBirth,tempLangs[:-1])

print("Number of candidates:",Candidates.candidates)
print("Candidates Database:",Candidates.candidateNo)
print("#################################")
c1 = Candidates_2022("Mia Divia Yang","9303 Buttonwood Ave. Hope Mills, NC 28348","(440) 988-4567",30,"2/1/1960","Python","Java")
print("---Details of the candidate---")
print(c1)
print("#################################")
c2 = Candidates_2022.createCandidate("Calvin F. Alvarez","799 Lake Floyd Circle Newark, DE 19714","(1) 302-246-4718",31,"June 23, 1962","Python")
print("---Details of the candidate---")
print(c2)
print("#################################")
c3 = Candidates_2022("Theresa J. Barone","500 Ben Street North Greenbush, NY 12144","(1) 518-225-3077", 23,"13/4/1976","Python","Java","C++")
print("---Details of the candidate---")
print(c3)
print("#################################")
print("Number of candidates:",Candidates.candidateNo)
print("Candidates Database:",Candidates.candidates)