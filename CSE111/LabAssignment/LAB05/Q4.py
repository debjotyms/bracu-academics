class Color:
    def __init__(self,color):
        self.color = color
        self.clr = None
    def __add__(self,other):
        color = None
        if self.color == "red" and other.color == "yellow":
            color = "Orange"
        elif self.color == "red" and other.color == "blue":
            color = "Violet"
        elif self.color == "blue" and other.color == "yellow":
            color = "Green"
        elif other.color == "red" and self.color == "yellow":
            color = "Orange"
        elif other.color == "red" and self.color == "blue":
            color = "Violet"
        elif other.color == "blue" and self.color == "yellow":
            other = "Green"
        obj = Color(None)
        obj.clr = color
        return obj

C1 = Color(input("First Color: ").lower())
C2 = Color(input("Second Color: ").lower())
C3 = C1 + C2
print("Color formed:", C3.clr)