class Assassin:
    totalNumber = 0
    def __init__(self,name,rate):
        self.name = name
        self.rate = rate
        Assassin.totalNumber+=1

    def printDetails(self):
        print(f"Name: {self.name}\nSuccess rate: {self.rate}%\nTotal number of Assassin: {Assassin.totalNumber}")

    @classmethod
    def failureRate(cls,name,rate):
        return cls(name,100-rate)

    @classmethod
    def failurePercentage(cls,name,rate):
        return cls(name,100-int(rate[:-1]))

john_wick = Assassin('John Wick', 100)
john_wick.printDetails()
print('============================')
nagisa = Assassin.failureRate("Nagisa", 20)
nagisa.printDetails()
print('============================')
akabane = Assassin.failurePercentage("Akabane", "10%")
akabane.printDetails()
