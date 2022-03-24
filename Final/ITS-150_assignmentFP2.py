





def main():
    nineDigitInt = getInteger()
    ISBN = calcChecksum(nineDigitInt)
    print(nineDigitInt)
    print()
    print(ISBN)

def getInteger():
    num = ""
    while num.isdigit() == False or len(num) != 9:
        num = input("\nPlease enter a nine digit integer: ")
        if num.isdigit() == False:
            print("Must be number")
        elif len(num) != 9:
            print("must be exactly 9 digits")
        else:
            return num

def calcChecksum(num):
    x = 10
    sum = 0
    for i in range(len(num)):
        newNum = int(num[i]) * x
        x -= 1
        sum += newNum
    for i in range(0, 11):
        y = sum + i
        z = y %  11
        if z == 0:
            digit = i
    if digit == 10:
        digit = 'X'
    ISBN = num + str(digit)
    return ISBN


main()