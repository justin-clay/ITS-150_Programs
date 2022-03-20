

class Shape:

    def __init__(self, width=0, height=0):
        self._width = width
        self._height = height
        self._radius = width

    def __str__(self):
        return "The area is " + str(self.area()) + " and perimeter is " + str(self.perimeter()) + "."

class Square(Shape):
    
    def perimeter(self):
        return self._width * 4

    def area(self):
         return self._width * self._width

class Rectangle(Shape):

    def perimeter(self):
        return (self._width * 2) + (self._height * 2)

    def area(self):
        return self._width * self._height

class Circle(Shape):
    
    def perimeter(self):
        PI = 3.14
        return 2 * PI * self._radius

    def area(self):
        PI = 3.14
        return (self._radius ** 2) * PI


def main():
    width = float(input("Enter the length of a square: "))
    print(Square(width))

    width = float(input("Enter the width of a rectangle: "))
    height = float(input("Enter the height of a rectangle: "))
    print(Rectangle(width, height))
  
    radius = float(input("Enter the radius of a circle: "))
    print(Circle(radius))
    
main()