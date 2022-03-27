
# Assuming that:

# Caffeine is absorbed into the body immediately.
# Once absorbed, 20% is eliminated from the body each hour.

# Write a program that asks the user for the amount of coffee consumed, in milligrams (mg), and then compute (and output) the following:

# The number of hours required until there is less than half of the caffeine left in the body
# The amount of caffeine left in the body after 8 hours

# Then, assuming that the person drinks a cup of coffee at 8 am and then drinks a cup of coffee at the end of each hour until 6 pm, compute and output the following:

# How much caffeine will there be in the body at the end of the 10 hours?

# A sample run would be as follows.

# Enter the amount of caffeine in mg: 200
# Less than half of it will be left after 4 hours.
# The amount of caffeine left in the body after 8 hours: 33.55 mg
###############################################################################################


def main():
    caff = getInput() # get user input and set caff
    halfCaffHours = caffeineLossHalf(caff) # send caff to caffeineLoss() and get result
    print("\nLess than half of it will be left after " + str(halfCaffHours) + " hours.") # print the amount of hours caffeine will be less than half
    eightHours = caffeineLossEightHours(caff) # send caff to func and get result
    print("\nThe amount of caffeine left in the body after 8 hours is: " + str("{:.2f}".format(eightHours)) + " mg") # print amount of caff left after 8 hours
    tenHours = caffeineLossTenHours(caff) #send caff to func get result
    print("\nThe amount remaining after 10 hours: " + str("{:.2f}".format(tenHours)) + " mg") # print caff after 10 hour. See the function notes below for more info
    print()
    

def getInput(): # ask user to enter the starting caffeine amount that was in a consumed cup of coffee
    while True: # continuous loop
        userInput = input("\nEnter the amount of caffeine in mg: ") # get caffeine input from user
        if userInput.isdigit(): # if userInput consists of only whole numbers
            return int(userInput) # return the integer of userInput
            break
        else: # if input is anything other than all numbers
            print("\nYour entered a non-integer.")
            print("Please only enter whole numbers. Try again...")

# calculate when caffiene will be less than half of starting at 20% loss per hour
def caffeineLossHalf(startingCaff):
    caffeine = startingCaff
    hours = 0 # start with 0 hours
    while caffeine >= (.5 * startingCaff): # loop will run until caff current caff value is less than half of the starting value from input
        caffeine = caffeine * .80 # for each hour that pass multiply caff by 80% and set new caff
        hours += 1 # add 1 hour to total hours
    return hours # return total hours after loop stops

# calculate caffeine loss after eight hours of time at 20% per hour
def caffeineLossEightHours(startingCaff):
    hours = 8 # set amount of hours
    caffeine = startingCaff 
    for i in range(hours):
        caffeine = caffeine  * .8 # for each hour in hours, multiply by 80% and set as new caff value
    return caffeine # return total caff value after the total hours

# Assuming that the person drinks a cup of coffee at 8 am and then drinks a cup 
# of coffee at the end of each hour until 6 pm, then calculate how much caffeine 
# will be left after 10 hours.
def caffeineLossTenHours(startingCaff):
    caffeine = startingCaff # set starting caff from user input
    hours = 10 # set the amount of hours
    for i in range(hours):
        caffeine = caffeine * .8 # for each hour multiply caff by 80% and set as new caff variable
        caffeine += startingCaff # at the end of each hour drink another coffee aka caff will add the starting caff to its value
    return caffeine # return total caff value after the amount of hours


main()