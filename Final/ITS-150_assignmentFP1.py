

from curses import has_extended_color_support


def main():
    caff = getInput()
    halfCaffHours = caffeineLossHalf(caff)
    print("\nLess than half of it will be left after " + str(halfCaffHours) + " hours.")

def getInput():
    caffeine = eval(input("\nEnter the amount of caffeine in mg: "))
    return caffeine

# calculate when caffiene will be less than half of starting at 20% loss per hour
def caffeineLossHalf(startingCaff):
    caffeine = startingCaff
    hours = 0
    while caffeine >= (.5 * startingCaff):
        caffeine = caffeine * .80
        hours += 1

    return hours


main()