marks = [99, 95, 96]
i = 0

while i < len(marks):  # while loop length of marks more than i till then we print marks of i
    print(marks[i])  # writing only this line will result in an infinity loop
    i = i + 1

# i = 0 is the index which is 0 i.e 99
# it will keep printing the value at index 0 i.e 99
# we update the value of marks by using +1
