class Employee:
    no_of_leaves = 8  # this will be same for all objects you can access this with any object or even class


chitresh = Employee()
vivek = Employee()

chitresh.name = "Chitresh"
chitresh.salary = 9000
chitresh.role = "Engineer"

vivek.name = "Vivek"
vivek.salary = 10000
vivek.role = "Operations Executive"  # all of these three are objects own property/attribute we create a class based
# no_of_leaves because we want something from the template

# print(chitresh.no_of_leaves)
# print(vivek.no_of_leaves)

print(vivek.name)  # first print this 1 first step **

print(vivek.no_of_leaves)
print(chitresh.no_of_leaves)
print(Employee.no_of_leaves)  # Second print this to show it's for all

Employee.no_of_leaves = 9
print(Employee.__dict__)  # Sixth
print(Employee.no_of_leaves)  # We can change it with class but not object #Third

chitresh.no_of_leaves = 10

print(chitresh.no_of_leaves)  # It will remain unchanged #This creates a new instance variable
# This will be objects new property  #Fourth
print(chitresh.__dict__)  # Fifth

# print(Employee.no_of_leaves)
# Employee.no_of_leaves = 10
# print(Employee.no_of_leaves) # This will first print 8 and then print 10 because of the order

# print(vivek.__dict__)
# Changing with objects
# vivek.no_of_leaves = 10  # This creates a new instance variable which means object's own property
# print(vivek.__dict__)  # This will print everything even the number of leaves inside a dictionary
# print(Employee.no_of_leaves)

print(Employee.no_of_leaves)
print(Employee.__dict__)
Employee.no_of_leaves = 10  # This creates a new instance variable which means object's own property
print(Employee.__dict__)  # This will print everything even the number of leaves inside a dictionary
print(Employee.no_of_leaves)
# This above code will end up changing the no_of_leaves

# Basically with instance we can't change the class variable
