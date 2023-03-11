class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        print(f"{self.name}")


class Rectangle(Shape):
    def __init__(self, name, length, width, symbol):
        super().__init__(name)
        self.length = length
        self.width = width
        self.symbol = symbol

    def area(self):
        print(f"rectangle-{self.length}{self.width}{self.symbol}")

# shape=input("Enter shape name")
# length=int(input("Enter length"))
# width=int(input("Enter width"))
# print(length*width)
example=Rectangle("Rectangle","length","*","width")
example.area()
