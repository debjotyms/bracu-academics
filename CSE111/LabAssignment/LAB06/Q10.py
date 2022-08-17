class SultansDine:
  branches=0
  total=0
  branchInfo=[]
  def __init__(self, name):
    self.name=name
    self.sell = 0
  def sellQuantity(self, quantity):
    if quantity<10:
      self.sell=quantity*300
    elif quantity<20:
      self.sell=quantity*350
    else:
      self.sell=quantity*400
    SultansDine.total +=  self.sell
    SultansDine.branches += 1
    self.branchInfo.append([self.name,self.sell])
  def branchInformation(self):
    print("Branch Name: ",self.name)
    print("Branch Sell: ",self.sell,"Taka")
  @classmethod
  def details(cls):
    print("Total number of branch(s):",SultansDine.branches)
    print("Total Sell:",SultansDine.total,"Taka")
    for info in SultansDine.branchInfo:
      print("Branch Name:",info[0],", Branch Sell:",info[1],"Taka")
      print("Branch consists of total sell's:",round(((info[1]/SultansDine.total)*100),2),"%")

SultansDine.details()
print('########################')
dhanmodi = SultansDine('Dhanmondi')
dhanmodi.sellQuantity(25)
dhanmodi.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()