
def main():
    while True:
        
        num1 = input("\nEnter a non-negative integer: ")
        num2 = input("\nEnter another non-negative integer: ")
        try:
            num1 = int(num1)
            num2 = int(num2)
            result = num1 // num2
        except ZeroDivisionError:
            print("\nDivision by Zero. Try again.")
        except ValueError:
            print("\nYou did not enter non-negative integer(s). Try again.")
        else:
            print("\nThe result of integer division is " + str(result) + ".\n")
            break
main()