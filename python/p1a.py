# PYTHON LAB PROGRAM 1

# 1) AIM: Introduce the Python fundamentals, data types, operators, flow control andexception
# handling in Python
# a) Write a python program to find the best of two test average marks out of three test’smarks
# accepted from the user.
m1 = int(input("Enter the marks in the first test: "))
m2 = int(input("Enter the marks in the second test: "))
m3 = int(input("Enter the marks in the third test: "))
if m1 > m2:
        if m2 > m3:
                total = m1 + m2
        else:
                total = m1 + m3
elif m1 > m3:
        total = m1 + m2
else:
        total = m2 + m3
        avg = total / 2
print("The average of the best two test marks is:", avg)

# Output:
# CASE 1:
# Enter the marks in the first test: 20
# Enter the marks in second test: 15
# Enter the marks in third test: 22
# The average of the best two test marks is: 21.0

# CASE 2:
# Enter the marks in the first test: 24
# Enter the marks in second test: 25
# Enter the marks in third test: 23
# The average of the best two test marks is: 24.5