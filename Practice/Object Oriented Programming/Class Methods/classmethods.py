class Employee:
    no_of_leaves = 9

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name} Salary is {self.salary} and role is {self.role}"

    @classmethod  # decorators a topic to study
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves  # if you change the name of no of leaves to something else it won't work


chitresh = Employee("Chitresh", 9000, "Instructor")
vivek = Employee("Vivek", 10000, "Operations executive")

chitresh.change_leaves(56)
print(chitresh.no_of_leaves)
print(Employee.no_of_leaves)

# class methods is basically a way to change the variable inside the class
