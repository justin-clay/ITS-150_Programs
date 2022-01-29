### This program is used to record distance traveled and fuel used on a multi-leg trip.
### It will then calculate mpg mileage for each leg and for the total trip.

# Obtain starting odometer reading before trip, create variables and set them to zero.
startOdometer = eval(input("\nPlease enter the starting odometer reading: \n"))
odometer = 0
num = 0
leg = 0
# Create empty lists for mileage, fuel used and mpg for each leg.
miles = [] # list of miles traveled in each leg
fuelUsed = [] # list of fuel used in each leg
mpgList = [] # list of calculated mpg for each leg
# If user enters -1 in the starting mileage prompt, program will end.
if startOdometer == -1:
    print("\nGood Bye\n")  
    quit()

print("\nPlease enter your odometer reading and gallons of gas used on each leg of the trip.")
print("When you have entered data for all the legs then enter -1 for any of the values.")
# This is the input loop. It prompts the user for mileage and gas used on each leg of the trip. 
# Loop will continue until user enters -1
while odometer or startOdometer != -1:  
    num +=1 # counts the number of trip legs
    print("\nLeg #", num)
    odometer = eval(input("Enter odometer reading: "))
    if odometer == -1:
        break
    gallons = eval(input("Enter gallons used:  "))
    if gallons == -1:
        break
    fuelUsed.append(gallons) # adds gallons of gas used to a list
    miles.append(odometer - startOdometer) # calculates miles used per leg and adds to a list
    mpgList.append((odometer - startOdometer) / gallons) # calculates mpg per leg and adds to list
    startOdometer = odometer # sets current odometer reading to startOdometer so mileage can be calculated on next loop
print()
# This for loop will run for each leg mpg found in list.
# Will print the leg nmuber and calculated mpg for that leg.  
for i in mpgList:
    leg += 1 # counts the legs to be used in print statement below
    print("The mpg for leg", leg, "of the journey is:", "{:,}".format(round(i, 2)))
# If neither miles nor fuelUsed lists are empty, calculate and print total trip mpg.
# The if statement prevents a zero division error in one or both lists are empty.
if miles or fuelUsed != []:
    mpgTotal = sum(miles) / sum(fuelUsed)
    print("The total mpg for this trip is:", "{:,}".format(round(mpgTotal, 2)), "\n")

