class Employee:
    def __init__(self, name, lname):
        self.name = name
        self.lname = lname

    def explain(self):  # this is an instance method
        return f"This employee is {self.name} {self.lname}"

    @property  # as so as we use this property decorator we don't need parenthesis
    def email(self):
        return f"{self.name}.{self.lname}@codewithharry.com"


chitresh_poojary = Employee("Chitresh", "Poojary")

print(chitresh_poojary.email)  # we don't need parenthesis here because we used @property decorator above

chitresh_poojary.lname = "US"  # this is an instance variable

print(chitresh_poojary.email)
