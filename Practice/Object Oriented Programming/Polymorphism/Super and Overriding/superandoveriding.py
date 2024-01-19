class A:
    classvar1 = "I am in class variable"

    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        # self.classvar1 = "I am inside class A's constructor"


class B(A):
    # classvar1 = "I am in class B"
    pass


a = A()
b = B()

print(b.classvar1)

# perference is given to class variable
