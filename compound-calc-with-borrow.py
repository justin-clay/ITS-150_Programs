# Using this formula A = P (1 + r/n)٨(nt)

# t = 10 # number of years money is invested
# n = 4 # number of times money is compounded in year
# r = .052 # annual interest rate
# P = 10000 # principal investment

# # This is the compunding interest formula, A = the total amount
# A = P * (1+(r/n))**(n*t)
# print(A)

#------------------------------------------------#
user_selection = input("\nIf you want to calculate compunded interest enter a '1'...\
    \nIf you want to calculate money lost from borrowing press '2': " )
if user_selection == '1':
    print("\nThank you for using this calculator.")
    print("This program is meant to calculate what your total amount will be with compounding interest.")
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
    total_amount = principal * (1+((interest_rate / 100)/annual_compound))**(annual_compound*years_invested)

    ### This next line prints the calulated total amount for the user.
    print("\n--- The calculated total amount is: $" + "{:,}".format(round(total_amount, 2)) + " ---\n")
    print("\nWith the entered values of $" + "{:,}".format(round(principal, 2)) + " initial investment that is invested for",\
        years_invested, "years \nwith an interest rate of " + str(interest_rate) + "% that compounds", annual_compound, "times a year.\n" )
elif user_selection == '2':
    principal = float(input("\nEnter the amount you currently have in the investment account: "))
    interest_rate = float(input("\tPlease enter the interest rate percentage here: "))
    annual_compound = float(input("\tEnter the number of times the interest is compounded in one year: "))
    years_invested = float(input("\tEnter the number of years the money is invested: "))
    borrowed_amount = float(input("\tPlease enter the amount you want to borrow from your account: "))
    years_borrowed = float(input("\tEnter the amount of years until you return the borrowed money: "))

    principal_less_borrowed = principal - borrowed_amount

    years_after_borrow = years_invested - years_borrowed


    compound_borrowed_years = principal_less_borrowed * (1+((interest_rate / 100)/annual_compound))**(annual_compound*years_borrowed)
    compound_without_borrow = principal * (1+((interest_rate / 100)/annual_compound))**(annual_compound*years_invested)
    amount_after_return = compound_borrowed_years + borrowed_amount
    total_amount = amount_after_return * (1+((interest_rate / 100)/annual_compound))**(annual_compound*(years_invested - years_borrowed))

    difference = compound_without_borrow - total_amount

    print("\n--- The calculated total amount is: $" + "{:,}".format(round(total_amount, 2)) + " ---\n")

    print("\n--- The calculated difference if you had not borrowed at all is: $" + "{:,}".format(round(difference, 2)) + " ---\n")

    percentage = (difference / borrowed_amount) * 100

    print( "{:,}".format(round(percentage, 2)), "% is the percentage you paid on your borrowed loan\n")
else:
    print("\n*** That selection is not allowed. Please enter a 1 or 2. ***\n")



