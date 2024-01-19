class Employee:
    no_of_leaves = 10

    def __init__(self, aname, asalary, arole):  # setting the parameters here
        self.name = aname
        self.salary = asalary
        self.role = arole  # values of passed parameters being stored

    def printdetails(self):
        return f"The name is {self.name} Salary is {self.salary} Role is {self.role}" #formatting a string


chitresh = Employee("Chitresh", 9000, "Intructor")  # creating an instance

print(chitresh.name)
print(chitresh.printdetails())

