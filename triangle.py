from rectangle import Rectangle

class Triangle(Rectangle):

    def __init__(self, base, height, side_a, side_b, side_c):
        super().__init__(base, height)

    def get_area(self):
        pass