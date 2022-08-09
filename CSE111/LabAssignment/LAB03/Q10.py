class UberEats:
    def __init__(self,name,number,location):
        self.name = name
        self.number = number
        self.location = location
        print(f"{self.name}, welcome to UberEats!")
        self.ord1 = ""
        self.ord2 = ""
        self.price1 = 0
        self.price2 = 0
    def add_items(self,ord1,ord2,price1,price2):
        self.ord1 = ord1
        self.ord2 = ord2
        self.price1 = price1
        self.price2 = price2
    def print_order_detail(self):
        print(f"User details: Name: {self.name}, Phone: {self.number}, Address: {self.location}")
        ordDict = {self.ord1:self.price1,self.ord2:self.price2}
        totalPrice = self.price1+self.price2
        return f"""Orders: {ordDict}
Total Paid Amount: {totalPrice}"""

order1 = UberEats("Shakib", "01719658xxx", "Mohakhali")
print("=========================")
order1.add_items("Burger", "Coca Cola", 220, 50)
print("=========================")
print(order1.print_order_detail())
print("=========================")
order2 = UberEats ("Siam", "01719659xxx", "Uttara")
print("=========================")
order2.add_items("Pineapple", "Dairy Milk", 80, 70)
print("=========================")
print(order2.print_order_detail())