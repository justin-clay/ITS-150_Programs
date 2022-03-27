
# This program will ask the user for employee name, hourly or salary classification,
# and wage and hours worked accordingly. It will then print out a list of employee names
# and their monthly wages. It will then display the total number of emloyees and how many 
# are salaried. After that the total monthly payroll will be calculated and printed.




def main():
    salariedEmployees = [] # create an empty list for salary emloyees
    totalEmployees = [] # create a list for all employees
    totalMonthlyPayroll = 0 # create a varibale to calculate and store total payroll
    keepGoing = 'Y' # create a keep going flag used in while loop execution
    while keepGoing.capitalize() == 'Y': # as long as keepGoing flag is Y then loop will continue to ask for input
        name = getInput("\nEnter employee's name: ")
        classification = getInput("Enter employee's classification (Salaried or Hourly): ")
        if classification.upper() == 'HOURLY': # if employee is hourly ask for hours worked and hourly wage
            hours = floatValidation("Enter the number of hours worked in a month: ")
            wage = floatValidation("Enter hourly wage: ")
            totalEmployees.append(HourlyEmployee(name, wage, hours)) # pass name, wage, and hours to HourlyEmployee class and append object to totalEmployee list
        elif classification.upper() == 'SALARIED': # if salary employee ask for monthly wage 
            salary = floatValidation("Enter monthly salary: ")
            totalEmployees.append(SalariedEmployee(name, salary))
            salariedEmployees.append(SalariedEmployee(name, salary)) # pass salary to SalariedEmployee class and append object to salariedEmployees list
        else:
            print("\nYou entered something other than Salaried or Hourly.")
            print("Please check the spelling and try again...\n")
        keepGoing = getInput("Do you want to continue (Y/N)? ")
    print()
    for obj in totalEmployees: # for each object in list, print employee name and monthly salary
        print(str(obj._name) + ": " + str('${:0,.2f}'.format(obj.calculatePay())))
        totalMonthlyPayroll += obj.calculatePay()
    print("Number of employees: ", len(totalEmployees))
    print("Number of salaried employees: ", len(salariedEmployees))
    print("Total monthly payroll: ", '${:0,.2f}'.format(totalMonthlyPayroll))
    print()
    
def getInput(userPrompt): # allows user to properly and safely exit with keyboard interupt at any prompt
    try: 
        userInput = input(userPrompt) # try the getting the user prompt passed into function
        return userInput 
    except KeyboardInterrupt: # if user enters keyboard interupt, safely exit below
        print("\nProgram stopped by user with Keyboard Interupt.")
        print("Good Bye\n")
        quit()

def floatValidation(userPrompt): # confirm input is a number (integer or float) then return float
    while True: # continuoas loop
        try: # asks user for input
            userInput = input(userPrompt)
        except KeyboardInterrupt: # safely exits if user enter keyboard interupt
            print("\nProgram stopped by user with Keyboard Interupt.")
            print("Good Bye\n")
            quit()
        try:
            userInput = float(userInput) # attempts to make user input a float
            return userInput # if successful, returns the input in float format
            break # stops the while loop
        except ValueError: # if input is string or symbols and can't be made a float
            print("\nInput must be a float or integer.")
            print("Only enter numbers or a decimal.")
            print("No letters or symbols. Please try again...\n")
            
class Employee: # create parent class that accepts name, wage, and hours worked
    def __init__(self, name, wage, hoursWorked=0):
        self._name = name
        self._wage = wage
        self._hours = hoursWorked

    def setName(self, name):
        self._name = name

    def __str__(self): # can print name and monthly salary if asked
        return self._name, self.calculatePay()

class SalariedEmployee(Employee):

    def calculatePay(self): # calculate and return the monthly salary of employee
        self._salary = self._wage
        return self._salary

class HourlyEmployee(Employee):

    def calculatePay(self): # calculate and return the monthly salary of salaried employees
        self._salary = self._wage * self._hours
        return self._salary



main()