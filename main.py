# https://github.com/tprhoahau156348-lab/crud_shape.git

from rectangle import Rectangle
from square import Square
from triangle import Triangle
from circle import Circle
from hexagon import Hexagon

def main():
    print("--- יצירת אובייקטים והדגמת פולימורפיזם ---")
    print("-" * 40)
    
    try:
        rect = Rectangle(10, 5)
        square = Square(6)
        triangle = Triangle(6, 4, 6, 5, 5)
        circle = Circle(7)
        hexagon = Hexagon(4)
        
        shapes = [rect, square, triangle, circle, hexagon]
        
        for shape in shapes:
            print(shape)  
            print(f"Area: {shape.get_area()}")
            print(f"Perimeter: {shape.get_perimeter()}")
            print("-" * 20)
            
        print("\n--- בדיקת מנגנון הטיפול בשגיאות ---")
        print("מנסה ליצור מלבן עם צלע שלילית (width = -5)...")
        invalid_shape = Rectangle(-5, 10)

    except (ValueError, TypeError) as error:
        print(f"Error occurred: {error}")

if __name__ == "__main__":
    main()