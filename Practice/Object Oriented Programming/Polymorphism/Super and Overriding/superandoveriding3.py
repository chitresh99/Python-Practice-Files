# changing the order

class A:
    classvar1 = "I am in class variable"

    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "I am inside class A's constructor"
        self.special = "I am the star"


class B(A):
    classvar1 = "I am in class B"

    def __init__(self):
        # suppose we want a variable from class a so we use this super() a call to the constructor
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "I am inside class B's constructor"
        super().__init__()
        print(super().classvar1)  # accesing class variable of super class


a = A()
b = B()

print(b.special)
print(b.special, b.var1, b.classvar1)
