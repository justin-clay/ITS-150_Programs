
# A=πr^2
def circleArea(radius):
    area = 3.141592653589793 * radius ** 2
    return area

# P=2πr
def circlePerimeter(radius):
    perimeter = 2 * 3.141592653589793 * radius
    return perimeter

def main():
    circleRadius = eval(input("\nEnter the radius of the circle: "))
    print("Area of the circle is", round(circleArea(circleRadius), 1))
    print("Perimeter of the circle is", round(circlePerimeter(circleRadius), 1))
    print()

main()

