

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

def main():
    count = int(input("Enter a positive integer: "))
    print("\nThe", str(count) + "th", "number of the series would be", some_series(count))
    print()

main()