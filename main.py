from calculator import Shape       
from rectangle import Rectangle   
from square import Square         
from triangle import Triangle      
from circle import Circle         
from hexagon import Hexagon        

def main():
    
    try:
        rect = Rectangle(width=10, height=5)
        square = Square(side=6)
        triangle = Triangle(base=6, height=4, side_a=6, side_b=5, side_c=5)
        circle = Circle(radius=7)
        hexagon = Hexagon(side=4)
        
        shapes = [rect, square, triangle, circle, hexagon]
        
        for shape in shapes:
            print(shape) 
            print(f"Area: {shape.get_area()}")
            print(f"Perimeter: {shape.get_perimeter()}")
            print("-" * 20)
            

    except (ValueError, TypeError) as error:
        print(f"Error occurred: {error}")

if __name__ == "__main__":
    main()