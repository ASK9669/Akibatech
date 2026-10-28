class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
    
R1 = Rectangle(5, 10)
R2 = Rectangle(3, 4)


print("Area of rectangle 1:", R1.area())
print("Perimeter of rectangle 1:", R1.perimeter())
print("Area of rectangle 2:", R2.area())
print("Perimeter of rectangle 2:", R2.perimeter())   