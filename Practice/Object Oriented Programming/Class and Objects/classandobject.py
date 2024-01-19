class Person:
    name = "Chitresh"
    occupation = "Graphic Designer"
    Networth = 10

    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
c = Person()

a.name = "Chitresh"
a.occupation = "Software engineer"
b.name = "Vivek"
b.occupation = "Operations executive"

a.info()
b.info()
c.info()  # printing default values from the class

# a b and c are objects here
# Person is the class here
# info is a method
