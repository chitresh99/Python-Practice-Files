# str gets first preference rather than repr

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
        cls.no_of_leaves = newleaves

    def __add__(self, other):
        return self.name + other.name

    def __truediv__(self, other):
        return self.salary / other.salary

    def __floordiv__(self, other):
        return self.salary // other.salary

    def __repr__(self):  # This method is used to convert object to string
        return f"Employee ({self.name} , {self.salary} . {self.role})"

    def __str__(self):
        return f"The Name is {self.name} Salary is {self.salary} and role is {self.role}"


emp1 = Employee("Chitresh", 5000, "Engineer")

print(emp1)  # it prefers to print a string if nothing is specified
print(str(emp1))
print(repr(emp1))  # if we specify a dunder we can get what we want like here it is repr
# We specified it instead we would have got string
