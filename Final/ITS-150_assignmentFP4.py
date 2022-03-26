
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
        name = input("\nEnter employee's name: ")
        classification = input("Enter employee's classification (Salaried or Hourly): ")
        if classification.upper() == 'HOURLY': # if employee is hourly ask for hours worked and hourly wage
            hours = eval(input("Enter the number of hours worked in a month: "))
            wage = eval(input("Enter hourly wage: "))
            totalEmployees.append(HourlyEmployee(name, wage, hours)) # pass name, wage, and hours to HourlyEmployee class and append object to totalEmployee list
        if classification.upper() == 'SALARIED': # if salary employee ask for monthly wage 
            salary = eval(input("Enter monthly salary: "))
            totalEmployees.append(SalariedEmployee(name, salary))
            salariedEmployees.append(SalariedEmployee(name, salary)) # pass salary to SalariedEmployee class and append object to salariedEmployees list
        keepGoing = input("Do you want to continue (Y/N)? ")
    print()
    for obj in totalEmployees: # for each object in list, print employee name and monthly salary
        print(str(obj._name) + ": " + str('${:0,.2f}'.format(obj.calculatePay())))
        totalMonthlyPayroll += obj.calculatePay()
    print("Number of employees: ", len(totalEmployees))
    print("Number of salaried employees: ", len(salariedEmployees))
    print("Total monthly payroll: ", '${:0,.2f}'.format(totalMonthlyPayroll))
    print()

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