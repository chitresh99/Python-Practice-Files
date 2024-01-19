class Employee:
    no_of_leaves = 9

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
        # params = string.split("-")                     #first do this
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))


chitresh = Employee("Chitresh", 9000, "Engineer")
vivek = Employee("Vivek", 10000, "Operations executive")
varun = Employee.from_dash("Varun-110000-Businessman")

print(varun.salary)

# When do we use this ?
# We use this when we have a large text file
# With data "Varun-11000-Businessman" like this then we use this split function method and print stuff
# This makes your code more efficient

# learn this before teaching again

