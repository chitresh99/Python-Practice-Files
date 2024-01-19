class MyClass:
    common_variable = "Class Variable"

    def __init__(self, instance_variable):
        self.common_variable = instance_variable


# Creating an instance of the class
obj = MyClass("Instance Variable")

# # Accessing the variable using the class
# print(MyClass.common_variable)  # his will print "Class Variable"

# Accessing the variable using the instance
print(obj.common_variable)  # This will print "Instance Variable"


