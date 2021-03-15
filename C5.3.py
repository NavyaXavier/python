class Rect:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        area = self.length * self.width
        print("area of rectangle: " + str(area) + "m^2")
    def __lt__(self, other):
        a1 = self.length * self.width
        a2 = other.length * other.width
        if a1 < a2:
            print("the greater is the second one")
        else:
            print("the greater is the first one")


Length1 = int(input("enter the length of first rectangle : "))
Width1 = int(input("enter the width of first rectangle : "))

Length2 = int(input("enter the length of second rectangle : "))
Width2 = int(input("enter the width of second rectangle : "))

rect1 = Rect(Length1, Width1)
rect2 = Rect(Length2, Width2)
print("FIRST RECTANGLE")
rect1.area()
print("SECOND RECTANGLE")
rect2.area()
print(rect1 < rect2)
