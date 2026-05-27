# hexagon.py
import math
from calculator import Shape

class Hexagon(Shape):
    def __init__(self, side):
        if not isinstance(side, (int, float)):
            raise TypeError("Side must be a number")
            
        if side <= 0:
            raise ValueError("Side must be greater than 0")
            
        self.side = side

    def get_area(self):
        return (3 * math.sqrt(3) * (self.side ** 2)) / 2

    def get_perimeter(self):
        return 6 * self.side

    def __str__(self):
        return "Shape: Hexagon"

    def __repr__(self):
        return f"Hexagon(side={self.side})"