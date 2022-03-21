# This program file has one parent class "Shape" and three 
# child class Square, Rectangle, and Circle.

# creates a Shape class that is passed dimensions in the for of parameters
# and then passes those dimensions to the child classes when called upon. 
# Then it will print the area and perimeter of shape that was called.
class Shape:
    def __init__(self, width=0, height=0):
        self._width = width # sets width parameter to the self variable
        self._height = height # sets height parameter to the self variable
        self._radius = width # uses the width parameter to pass to circle radius from user input. 

    def __str__(self): # will print this text string with the associated self.area and self.perimeter, whichever shape class is called.
        return "The area is " + str("{:.2f}".format(self.area())) + " and perimeter is " + str("{:.2f}".format(self.perimeter())) + "."

# creates the Square class using the passed dimensions and will calculate
# and return self.area() and self.perimeter() to be used in parent __str__ method
class Square(Shape):
    
    def perimeter(self):
        return self._width * 4

    def area(self):
         return self._width * self._width

# creates the Rectangle class using the passed dimensions and will calculate
# and return self.area() and self.perimeter() to be used in parent __str__ method
class Rectangle(Shape):

    def perimeter(self):
        return (self._width * 2) + (self._height * 2)

    def area(self):
        return self._width * self._height

# creates the Square class using the passed dimensions and will calculate
# and return self.area() and self.perimeter() to be used in parent __str__ method
class Circle(Shape):
    
    def perimeter(self):
        PI = 3.14
        return 2 * PI * self._radius

    def area(self):
        PI = 3.14
        return (self._radius ** 2) * PI

# creates a main() function that will test the above classes by prompting
# the user to input required dimensions for various shapes and them pass them to the appripriate classes
def main():
    width = float(input("Enter the length of a square: "))
    print(Square(width)) # will pass width to Square class and calculate area and perimeter

    width = float(input("Enter the width of a rectangle: "))
    height = float(input("Enter the height of a rectangle: "))
    print(Rectangle(width, height)) # will pass width to Rectangle class and calculate area and perimeter
  
    radius = float(input("Enter the radius of a circle: "))
    print(Circle(radius)) # will pass width to Circle class and calculate area and perimeter

main()