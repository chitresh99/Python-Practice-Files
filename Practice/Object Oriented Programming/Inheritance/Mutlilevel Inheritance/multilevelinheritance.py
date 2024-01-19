class Dad:
    basketball = 6

    def isbasketball(self):
        return f"Yes i have played basketball {self.basketball} no of times"


class Son(Dad):
    dance = 1

    def isdance(self):
        return f"Yes I dance {self.dance} no of times"

    basketball = 7

    def isbasketball(self):
        return f"Yes i have played basketball {self.basketball} no of times"


class Grandson(Son):
    dance = 7
    basketball = 9

    def isdance(self):
        return f" jackson yeah Yes I dance {self.dance} no of times"

    def isbasketball(self):
        return f"I am the kobe bryant i scored {self.basketball}"

darry = Dad()
larry = Son()
harry = Grandson()

print(harry.dance)
print(harry.isdance())
print(harry.isbasketball())
print(larry.basketball)

# we can overwrite any function from any class in the last or a level above
