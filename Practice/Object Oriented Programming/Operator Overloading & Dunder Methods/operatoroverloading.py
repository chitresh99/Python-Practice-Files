# str method gets first preference rather than repr

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


emp1 = Employee("Chitresh", 5000, "Engineer")
emp2 = Employee("Vivek", 50, "Music producer")

print(emp1 + emp2)  # can be performed with string and can be performed with numbers
print(emp1 / emp2)  # only numbers
print(emp1 // emp2)
