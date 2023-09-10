#pgm p7b
class Employee:
        def __init__(self):
                self.name = ""
                self.empId = ""
                self.dept = ""
                self.salary = 0

        def getEmpDetails(self):
                self.name = input("Enter Employee name: ")
                self.empId = input("Enter Employee ID: ")
                self.dept = input("Enter Employee Dept: ")
                self.salary = int(input("Enter Employee Salary: "))

        def showEmpDetails(self):
                print("Employee Details")
                print("Name:", self.name)
                print("ID:", self.empId)
                print("Dept:", self.dept)
                print("Salary:", self.salary)

        def updtSalary(self):
                self.salary = int(input("Enter new Salary: "))
                print("Updated Salary:", self.salary)

e1 = Employee()
e1.getEmpDetails()
e1.showEmpDetails()
e1.updtSalary()

# OUTPUT:
# Enter Employee name: Aaryan
# Enter Employee ID: 123
# Enter Employee Dept: cse
# Enter Employee Salary: 50000
# Employee Details
# Name: Aaryan
# ID: 123
# Dept: cse
# Salary: 50000
# Enter new Salary: 60600
# Updated Salary: 60600