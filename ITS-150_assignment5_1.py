
def main():
    while True:
        try:
            num = float(input("Enter a floating point number between 10.0 and 20.0 (both inclusive): "))
            if num >= 10.0 and num <= 20.0:
                print("Your number is", str(num) + ".")
                break
            else:
                print("You did not enter a floating point number in the given range.")
        except ValueError:
            print("You did not enter a floating point number in the given range.")

main()