class Student:
    pass


chitresh = Student()
vivek = Student()

# Assigning attributes to the chitresh instance
chitresh.name = "Chitresh"
chitresh.std = 10       # well in oop we assign attributes inside the class
chitresh.section = 1  # You can even create lists here not limited till numbers and strings

vivek.std = 12
vivek.subjects = ["maths","science"]
print(chitresh.name, vivek.subjects)  # if we write vivek.name here it will definitely throw an error because
# vivek doesn't have a name here

# Objects and instance are same here they can be used inter changeably




