## This program will ask the user to input a floatin point number between 10.0 and 20.0
## and then check to see if it matches that range.

def main():
    while True: # loop will run until correct numbers are entered or key interupt is used
        try: # will ask for float input and check if it is within range
            num = float(input("Enter a floating point number between 10.0 and 20.0 (both inclusive): "))
            if num >= 10.0 and num <= 20.0: # if number in range then the message is printed out and the loop broken
                print("Your number is", str(num) + ".")
                break
            else: # if num not in range then error message printed and loop starts again
                print("You did not enter a floating point number in the given range.")
        except ValueError: # if a ValueError, such as from entering a string, then this message printed and restart loop
            print("You did not enter a floating point number in the given range.")

main()