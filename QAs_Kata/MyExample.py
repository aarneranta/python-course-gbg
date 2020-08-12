class MyExampleCo:
    def __init__(self):
        self.employees = []
        self.paidSalaries = 0

    def createEmployee(self, name, salary, employeeType):
        newEmployee = None
        incorrectType = True
        while(incorrectType):
            if employeeType == "employee":
                newEmployee = Employee(name, salary)
                incorrectType = False
            elif employeeType == "intern":
                newEmployee = Intern(name, salary)
                incorrectType = False
            else:
                print("Invalid type, try \"intern\" or \"employee\"")
        self.employees.append(newEmployee)
        self.paidSalaries += salary

    def calculateSalaries(self):
        totalNetto = 0
        for emp in self.employees:
            totalNetto += int(emp.calculateNetto())
        print(f"The sum of brutto salaries is {self.paidSalaries}")
        print(f"The sum of netto salaries is {totalNetto}")


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tax = 0.3

    def calculateNetto(self):
        return self.salary*(1-self.tax)


class Intern(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.tax = 0


def main():
    corporation = MyExampleCo()
    corporation.createEmployee("Tom",20,"employee")
    corporation.createEmployee("Emily",30,"employee")
    corporation.createEmployee("Charles",10, "intern")
    corporation.calculateSalaries()

main()