
# This program is written in response to a problem that wanted to calculate 
# a 10 digit ISBN number from a 9 digit integer entered by the user. It is 
# a little difficult to explain the algorithm for this, so I will copy and
# paste an the example and explanation from the book.
#############################################################################################################################
# Example:                                                                                                                  #
# The checksum digit corresponding to 032149805 is 4 since 4 is the only value of x between 0 and 10 (both inclusive),      #
# for which 10·0 + 9·3 + 8·2 + 7·1 + 6·4 + 5·9 +4·8 +3·0 + 2·5 + 1·x is a multiple of 11.                                   #
#                                                                                                                           #
# The checksum digit d1 can be any value from 0 to 10. The ISBN convention is to use the character X to denote 10.          #
#############################################################################################################################

# This is the main function that calls for user input and set the nineDigitInt variable
# Then calls funtions to calculate the ISBN, then prints the ISBN.
def main():
    nineDigitInt = getInteger()
    ISBN = calcChecksum(nineDigitInt)
    print("\nThe corresponding ISBN number would be " + str(ISBN) + '.')
    print()
    
# This funciton asks user to input a nine digit integer, then uses input validation
# and error handling to confirm nothing except a nine digit integer exactly has been entered.
# After that is confirmed the the integer is returned.
def getInteger():
    num = ""
    while num.isdigit() == False or len(num) != 9: # Loop will continue to run until user inputs exactly 9 digits that are all integers.
        num = input("\nPlease enter a nine digit integer: ")
        if num.isdigit() == False: # if any digit is not number print error and try loop again
            print("\nAll digits must be a number (0-9)")
            print("no letters or symbols. Please try again.")
        elif len(num) != 9: # if length is not exactly 9 digits print error and loop again
            print("\nYou entered more/less than 9 digits.")
            print("Please enter exactly 9 digits. Try again.")
        else:
            return num

# This function will is passed the nine digit number and will calculate the 10 digit ISBN from
# it usinng the algorithm explained in the example above in header comment section.
def calcChecksum(num):
    x = 10
    sum = 0
    for i in range(len(num)):
        newNum = int(num[i]) * x # applies the algorithm above to each digit
        x -= 1
        sum += newNum # sumation or the nine digits with algorithm applied
    for i in range(0, 11):
        y = sum + i # add (0-10) one at a time to 9 digit sumation from above
        if y % 11 == 0: # divides each total sumation by 11 
            digit = i # if division by 11 has no remainder (divides evenly), set that as the digit variable
    if digit == 10:
        digit = 'X' # if digit is 10 change digit to 'X' string instead
    ISBN = num + str(digit) # add the digit string on the end of the nine digit number
    return ISBN # return full ISBN


main()