class Team:

    def __init__(self,__country=None):
        self.__name = __country
        self.__list = []
    
    def setName(self,name):
        self.__name = name
    
    def addPlayer(self,player):
        self.__list.append(player.name)

    def printDetail(self):
        print("=====================")
        print(f"Team: {self.__name}")
        print("List of Players:")
        print(self.__list)
        print("=====================")

class Player:
    def __init__(self,name):
        self.name = name

b = Team()
b.setName('Bangladesh')
mashrafi = Player("Mashrafi")
b.addPlayer(mashrafi)
tamim = Player("Tamim")
b.addPlayer(tamim)
b.printDetail()
a = Team("Australia")
ponting = Player("Ponting")
a.addPlayer(ponting)
lee = Player("Lee")
a.addPlayer(lee)
a.printDetail()