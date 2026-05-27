from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

    def __str__(self):
        return "Shape: Square"

    def __repr__(self):
        return f"Square(side_length={self.width})"