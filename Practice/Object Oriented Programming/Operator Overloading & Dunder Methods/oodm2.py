class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # This method defines the string representation of the object
        return f"MyClass(x={self.x}, y={self.y})"


# Creating an instance of MyClass
obj = MyClass(10, 20)

# Using repr() to get the string representation of the object
representation = repr(obj)

print(representation)
