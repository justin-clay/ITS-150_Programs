## This program creates a series of numbers and then prompts the user to enter a number.
## Then the program will return the value of the series on the iteration that matches the user input.

# Creates a function that will take number x and multiply each digit of x that is not a zero.
# Then take that result and add it to the number x. That becomes the next number in the series.
# Then the cycle repeats however many times the user prompts it to run.
def some_series(n):
    x = 1
    counter = 0
    while counter <= n:
        counter += 1
        num = 1
        for digit in str(x):
            if int(digit) != 0:
                num *= int(digit)
        num += x  
        x = num
        if counter + 1 == n:
            return x
# Create a main function that will prompt the user to enter a number.
# That number is then passes to some_series() through the n parameter. 
# Program will then print the number of the series iteration, and the value at that location of the series.
def main():
    count = int(input("Enter a positive integer: "))
    print("\nThe", str(count) + "th", "number of the series would be", some_series(count))
    print()
# Runs main program
main()