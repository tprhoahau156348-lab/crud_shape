import math

from calculator import Shape


class Hexagon(Shape):

    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return (3 * math.sqrt(3) * self.side_length ** 2) / 2

    def get_perimeter(self):
        return 6 * self.side_length

    def __str__(self):
        return f"Hexagon(side_length={self.side_length})"