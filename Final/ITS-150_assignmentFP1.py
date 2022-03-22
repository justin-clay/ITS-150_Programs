



def main():
    caff = getInput()
    halfCaffHours = caffeineLossHalf(caff)
    print("\nLess than half of it will be left after " + str(halfCaffHours) + " hours.")
    eightHours = caffeineLossEightHours(caff)
    print("\nThe amount of caffeine left in the body after 8 hours is: " + str("{:.2f}".format(eightHours)) + " mg")
    tenHours = caffeineLossTenHours(caff)
    print("\nThe amount remaining after 10 hours: " + str("{:.2f}".format(tenHours)) + " mg")
    print()
    

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

# calculate caffeine loss after eight hours of time at 20% per hour
def caffeineLossEightHours(startingCaff):
    hours = 8
    caffeine = startingCaff
    for i in range(hours):
        caffeine = caffeine  * .8
    return caffeine

# Assuming that the person drinks a cup of coffee at 8 am and then drinks a cup 
# of coffee at the end of each hour until 6 pm, then calculate how much caffeine 
# will be left after 10 hours.
def caffeineLossTenHours(startingCaff):
    caffeine = startingCaff
    hours = 10
    for i in range(hours):
        caffeine = caffeine * .8
        caffeine += startingCaff
    return caffeine


main()