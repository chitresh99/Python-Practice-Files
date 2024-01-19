class Employee:
    no_of_leaves = 10

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The name is {self.name} The salary is {self.salary} The role is {self.role}"

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgoods(string):
        print("This is good " + string)


class Programmer(Employee):
    def __init__(self, aname, asalary, arole, languages):
        super().__init__(aname, asalary, arole)  # Call the constructor of the parent class
        self.languages = languages

    def printprog(self):
        return f"The programmer's Name is {self.name} Salary is {self.salary} and role is {self.role} The languages are {self.languages}"

chitresh = Employee("Chitresh", 9000, "Engineer")
varun = Employee("Varun", 10000, "Business Man")

raj = Programmer("Raj", 10000, "Programmer", ["Python"])
siddesh = Programmer("Siddesh", 10000, "Programmer", ["Python"])

print(raj.printprog())

