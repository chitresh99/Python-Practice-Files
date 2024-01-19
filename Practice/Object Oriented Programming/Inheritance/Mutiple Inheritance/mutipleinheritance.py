class Employee:
    var = 5
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


class Player:
    var = 6
    no_of_games = 4

    def __init__(self, name, game):  # creating a constructor helps initialize the properties or
        # attributes of an object when it is created.
        self.name = name
        self.game = game

    def printdetails(self):
        return f"The name is {self.name} Game is {self.game}"


class CoolProgrammer(Employee, Player):  # order is important #if you do (Player,Employee)
    # then make sure to count the number of arguments
    # pass  # we wrote this because this is a placeholder
    #  first use pass

    language = "C++", "Java"

    def printlanguages(self):
        print(self.language)
    # print(", ".join(self.language))  # to remove the square brackets
    # also found out that commenting out multiple lines at the same time can be done by ctrl + /
    # i mean you have to select the part which you want to comment out first


chitresh = Employee("Chitresh", 9000, "Engineer")
varun = Employee("Varun", 10000, "Business Man")

raj = Player("Raj", ["Cricket"])
siddesh = CoolProgrammer("Siddesh", 10000, "Machine learning engineer")

print(raj.printdetails())
# siddesh.printlanguages()
# siddesh.printgoods("good stuff")
# print(siddesh.var)
siddesh.printlanguages()
# 1 why order is important explain that with the var example
# Then change the number of arguments in Cool programmer and make it a list of games then print var
# siddesh.printgoods() use with pass
