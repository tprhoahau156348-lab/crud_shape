from rectangle import Rectangle

class Triangle(Rectangle):
    def __init__(self, base, height, side_a, side_b, side_c):
        for side in (side_a, side_b, side_c):
            if not isinstance(side, (int, float)):
                raise TypeError("Sides must be numbers")
            if side <= 0:
                raise ValueError("Side must be greater than 0")

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        
        super().__init__(base, height)

    def get_area(self):
        return (self.width * self.height) / 2
    
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def __str__(self):
        return "Shape: Triangle"

    def __repr__(self):
        return f"Triangle(base={self.width}, height={self.height}, side_a={self.side_a}, side_b={self.side_b}, side_c={self.side_c})"