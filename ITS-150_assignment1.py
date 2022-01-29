# #!/usr/bin/python3
# 
# This application has been created to calculate the total amount at a future date with compunding interest.
# The formula you see below in the comment section is the basis for this calculation.
# The code below that formula that is commented out was my first build on making a working formula. 
# That program was then made more usable by creating user prompts to obtain the values to place in the formula.

# Using this formula A = P (1 + r/n)٨(nt)

# t = 10 # number of years money is invested
# n = 4 # number of times money is compounded in year
# r = .052 # annual interest rate
# P = 10000 # principal investment

# # This is the compunding interest formula, A = the total amount
# A = P * (1+(r/n))**(n*t)
# print(A)

#------------------------------------------------#

print("\nThank you for using this calculator.")
print("This program is meant to calculate the total amount you will have with compounding interest.")
print("Please enter the the requested amounts when prompted.\n")

# Prompts user for the amount of years money is invested and sets the 'years_invested' variable.
years_invested = float(input("\tEnter the number of years the money is invested: "))

# Prompts the user for the number of times interest is compunded in one year, and sets the 'annual_compound' variable.
annual_compound = float(input("\tEnter the number of times the interest is compounded in one year: "))

# Prompts the user for to enter the annual interest rate and sets the 'interest_rate' variable.
interest_rate = float(input("\tPlease enter the interest rate percentage here: "))

# Prompts the user to enter the intitial invested amount and set the 'principal' variable.
principal = float(input("\tPlease enter the initial principal investment amount: "))


## This is the formula to calulate the compunded interest, see notes in the top comment section above.
## The interest rate is divided by 100 to converts it to decimal form to use in the equation.
total_amount = principal * (1+((interest_rate / 100)/annual_compound))**(annual_compound*years_invested)

### This next line prints the calulated total amount for the user.
### The format and round functions are used here to round the dollar output to 2 decimal places and to input commas every 3 digits.
print("\n\t*** The calculated total amount is: $" + "{:,}".format(round(total_amount, 2)) + " ***\n")
print("\nWith the entered values of $" + "{:,}".format(round(principal, 2)) + " initial investment that is invested for",\
     years_invested, "years \nwith an interest rate of " + str(interest_rate) + "% that compounds", annual_compound, "times a year.\n" )
10