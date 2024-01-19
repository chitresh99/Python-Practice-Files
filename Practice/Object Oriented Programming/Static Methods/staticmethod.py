class Employee:
    no_of_leaves = 10

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.arole = arole

    def printdetails(self):
        return f"The name is {self.name} The salary is {self.salary} The role is {self.role}"

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgoods(string):
        print("This is good " + string)
        # return      return ke saath kuch bhi return likho woh return karega return 89


chitresh = Employee("Chitresh", 9000, "Engineer")
vivek = Employee("Vivek", 10000, "Operations executive")
varun = Employee.from_dash("Varun-110000-Businessman")

chitresh.printgoods("Chitresh")  # This won't return none
# print(chitresh.printgoods("Chitresh")) #this will return none as will
