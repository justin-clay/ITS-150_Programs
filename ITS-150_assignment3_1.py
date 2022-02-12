## This program will prompt the user to enter a radius for a circle.
## It will then calculate and print out the area and perimeter of the circle


# This creates a function to calculate the area using the formula A=πr^2
# The circle radius is passed as a parameter from main() 
def circleArea(radius):
    area = 3.141592653589793 * radius ** 2
    return area

# This creates a function to calculate circle perimeter using this formula P=2πr
#  The circle radius is passed as a parameter from main()
def circlePerimeter(radius):
    perimeter = 2 * 3.141592653589793 * radius
    return perimeter

# This creates the main() program funciton.
# This will prompt the user for a circle radius, pass it to the two functions, 
# and return and print the area and perimeter results.
def main():
    circleRadius = eval(input("\nEnter the radius of the circle: "))
    print("Area of the circle is", round(circleArea(circleRadius), 1))
    print("Perimeter of the circle is", round(circlePerimeter(circleRadius), 1))
    print()

# Runs the main function
main() 

