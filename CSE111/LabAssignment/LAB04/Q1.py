class Customer:
    def __init__(self,name):
        self.name = name
    
    def greet(self,person=""):
        if len(person) == 0:
            print("Hello!")
        else:
            print(f"Hello {person}!")

    def purchase(self,*items):
        print(f"{self.name}, you purchased {len(items)} item(s):")
        for item in items:
            print(item)

customer_1 = Customer("Sam")
customer_1.greet()
customer_1.purchase("chips", "chocolate", "orange juice")
print("-----------------------------")
customer_2 = Customer("David")
customer_2.greet("David")
customer_2.purchase("orange juice")