class Shape:
    def __init__(self,name):
        self.name=name
    def Area(self):
        return 0

class Rectangle(Shape):
    def __init__(self,name,length,width):
        super().__init__(name)
        self.length=length
        self.width=width
    def Area(self):
        print(f"Rectangle:{self.length}*{self.width}")
example=Rectangle("Rectangle","length","width")
example.Area()

class Triangle(Shape):
    def __init__(self,name,base,height):
        super().__init__(name)
        self.base=base
        self.height=height
    def Area(self):
        print(f"Triangle:({self.base}*{self.height})/2")
example=Triangle("Triangle","base","height")
example.Area()

# if shape==Rectangle:
Shape = input("Enter shape name")
if Shape=='Rectangle':

    length = int(input("Enter length"))
    width = int(input("Enter width"))
    print(length * width)
#Shape == input("Enter shaape name")
elif Shape=="Triangle":

    base = int(input("Enter base"))
    height = int(input("Enter height"))
    print((base * height) / 2)
else:
    print("Invalid shape")
# elif shape==Triangle

# if shape=="Rectangle":
#     print(length*width)
# elif shape==Triangle:
#     print((base*height)/2)
# else:
#     print("Invalid shape")


