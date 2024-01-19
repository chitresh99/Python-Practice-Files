from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0


class Rectangle(Shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.breath = 10

    def printarea(self):
        return self.length * self.breath


a = Rectangle()

print(a.printarea())

# Basically abstract class defines that we have to use that method without which the program won't work
# It gives us a blue print
