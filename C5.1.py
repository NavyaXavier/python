class Rectangle:
        def __init__(self,length,breadth):
            self.length = length
            self.breadth = breadth
        def  area(self):
            return self.length * self.breadth
        def perimeter(self):
            return 2 * (self.length + self.breadth)


print("rectangle 1")
a = int(input("enter the length:"))
b = int(input("enter the breadth: "))
obj = Rectangle(a, b)

print("area 1=", obj.area())
print("perimeter 1= ", obj.perimeter())

print("rectangle 2")
a = int(input("enter the length:"))
b = int(input("enter the breadth:"))
ob = Rectangle(a, b)

print("area 2=", ob.area())
print("perimeter 2=", ob.perimeter())

if obj.area() == ob.area():
    print("the two rectangle have same area")
else:
    print("not equal")






