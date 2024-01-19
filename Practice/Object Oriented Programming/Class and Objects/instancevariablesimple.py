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

print(Employee.no_of_leaves)
print(chitresh.__dict__)
chitresh.no_of_leaves = 10
print(chitresh.__dict__)  # dict is an attribute

print(Employee.no_of_leaves)

# Only class can change it's variable not instance(objects)

