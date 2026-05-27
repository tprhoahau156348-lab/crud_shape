from calculator import Shape

class Rectangle(Shape):
    def __init__(self, width, height):
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("Sides must be numbers")
            
        if width <= 0 or height <= 0:
            raise ValueError("Side must be greater than 0")

        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return "Shape: Rectangle"

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"