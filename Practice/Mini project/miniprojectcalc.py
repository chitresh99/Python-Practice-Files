first = input("Enter first Number :")
operator = input("Enter operator +,-,*,% :")
second = input("Enter the second Number :")

first = int(first)
second = int(second)

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "%":
    print(first % second)
else:
    print("Invalid Operator")





