# Public


class Employee:
    no_of_leaves = 9
    var = 9

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


# public means you can access that variable anywhere from the code

chitresh = Employee("Chitresh", 9000, "Engineer")

print(chitresh.var)


