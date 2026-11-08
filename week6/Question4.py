# Polymorphism
class Dog:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        return "Woof!"

class Cat:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        return "Meow!"
class Cow:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        return "Moo!"

# Abstration
class Shape:
    def __init__(self, name):
        self.name = name
    
class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width
    def calculate_area(self):
        return self.length * self.width
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    def calculate_area(self):
        return 3.14 * self.radius * self.radius

Dog1 = Dog("Buddy")
Cat1 = Cat("Whiskers")
Cow1 = Cow("Bessie")

Rectangle1 = Rectangle("Rectangle", 5, 3)
Circle1 = Circle("Circle", 4)

print("=" * 50)
print("Animal Sounds")
print("=" * 50)
animals = [Dog1, Cat1, Cow1]
for animal in animals:
    print(f"{animal.name} says: {animal.make_sound()}") 

print("\n" + "=" * 50)
print("Shape Areas")
print("=" * 50)
shapes = [Rectangle1, Circle1]
for shape in shapes:
    print(f"{shape.name} area: {shape.calculate_area()}")

print("=" * 50)