




def main():
    salariedEmployees = []
    totalEmployees = []
    totalMonthlyPayroll = 0
    keepGoing = 'Y'
    while keepGoing.capitalize() == 'Y':
        name = input("\nEnter employee's name: ")
        classification = input("Enter employee's classification (Salaried or Hourly): ")
        if classification.upper() == 'HOURLY':
            hours = eval(input("Enter the number of hours worked in a month: "))
            wage = eval(input("Enter hourly wage: "))
            totalEmployees.append(HourlyEmployee(name, wage, hours))
        if classification.upper() == 'SALARIED':
            salary = eval(input("Enter monthly salary: "))
            totalEmployees.append(SalariedEmployee(name, salary))
            salariedEmployees.append(SalariedEmployee(name, salary))
        keepGoing = input("Do you want to continue (Y/N)? ")
    print()
    for obj in totalEmployees:
        print(str(obj._name) + ": " + str('${:0,.2f}'.format(obj.calculatePay())))
        totalMonthlyPayroll += obj.calculatePay()
    print("Number of employees: ", len(totalEmployees))
    print("Number of salaried employees: ", len(salariedEmployees))
    print("Total monthly paroll: ", '${:0,.2f}'.format(totalMonthlyPayroll))
    print()

class Employee:
    def __init__(self, name, wage, hoursWorked=0):
        self._name = name
        self._wage = wage
        self._hours = hoursWorked

    def setName(self, name):
        self._name = name

    def __str__(self):
        return self._name, self.calculatePay()

class SalariedEmployee(Employee):

    def calculatePay(self):
        self._salary = self._wage
        return self._salary

class HourlyEmployee(Employee):

    def calculatePay(self):
        self._salary = self._wage * self._hours
        return self._salary



main()