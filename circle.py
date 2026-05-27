import math
from calculator import Shape

class Circle(Shape):
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a number")
            
        if radius <= 0:
            raise ValueError("Radius must be greater than 0")
            
        self.radius = radius

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def get_area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return "Shape: Circle"

    def __repr__(self):
        return f"Circle(radius={self.radius})"