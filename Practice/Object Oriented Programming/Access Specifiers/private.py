# Private
class Employee:
    no_of_leaves = 9
    __var = 9  # you define a private variable with a double underscore

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The name is {self.name} Salary is {self.salary} Role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))


# Accessing the private variable using name mangling
chitresh = Employee("Chitresh", 9000, "Engineer")
print(chitresh._Employee__var)


# # fuck the pycharm error it's not a common practice our method is right
# if you just print using print(chitresh.__var) it will give you a
# name mangling error
#
# so we use chitresh._Employee__var to prevent and access the variable
