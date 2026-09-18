import math

# Parent class
class Shape:
    def __init__(self, shape_name):
        self.shape_name = shape_name

    def display_name(self):
        print(f"\n--- Calculating Area for {self.shape_name} ---")

# Child class 1: Rectangle inherits from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Child class 2: Circle inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

# Child class 3: Triangle inherits from Shape
class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# --- Testing the Classes ---
rect = Rectangle(10, 5)
rect.display_name()
print(f"Area: {rect.area()}")

circle = Circle(7)
circle.display_name()
# Formatting to 2 decimal places
print(f"Area: {circle.area():.2f}") 

tri = Triangle(8, 4)
tri.display_name()
print(f"Area: {tri.area()}")