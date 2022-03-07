## This program will ask for two user inputs and then 
## return the result of integer division. 

def main():
    while True: # this loop will run until two integers are entered that don't cause an error or a key interupt is used
        num1 = input("\nEnter a non-negative integer: ") # sets first variable
        num2 = input("\nEnter another non-negative integer: ") # sets second variable
        try: # try loop will try to turn variable into integer and divide num1 by num2
            num1 = int(num1)
            num2 = int(num2)
            result = num1 // num2
        except ZeroDivisionError: # if second number entered is a zero this block will run
            print("\nDivision by Zero. Try again.")
        except ValueError: # if either value entered was a string, this block will run
            print("\nYou did not enter non-negative integer(s). Try again.")
        else: # if an error above is not created then this block will print the result and break the loop
            print("\nThe result of integer division is " + str(result) + ".\n")
            break

main()