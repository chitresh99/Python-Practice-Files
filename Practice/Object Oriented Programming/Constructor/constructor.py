class Employee:
    no_of_leaves = 0

    def printdetails(self):
        return f"Name is {self.name} Salary is {self.salary} and role is {self.role}"


chitresh = Employee()
vivek = Employee()

chitresh.name = "Chitresh"
chitresh.salary = 9000
chitresh.role = "Engineer"

vivek.name = "Vivek"
vivek.salary = 1000
vivek.role = "Operations Executive"

print(vivek.printdetails())  # inside these round brackets vivek will be passed automatically
# if you don't write self it will throw errors


