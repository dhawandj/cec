# Lab Program 3:
# AIM: Demonstration of manipulation of strings using string methods
# a) Write a Python program that accepts a sentence and find the number of words,
# digits,uppercase letters and lowercase letters.

s = input("Enter a sentence: ")
w, d, u, l = 0, 0, 0, 0
l_w = s.split()
w = len(l_w)
for c in s:
        if c.isdigit():
                d = d + 1
        elif c.isupper():
                u = u + 1
        elif c.islower():
                l = l + 1
print ("No of Words: ", w)
print ("No of Digits: ", d)
print ("No of Uppercase letters: ", u)
print ("No of Lowercase letters: ", l)


# OUTPUT:
# Case 1:
# Enter a sentence: Artificial Intelligence & Machine Learning 2021
# No of Words: 6
# No of Digits: 4
# No of Uppercase letters: 4
# No of Lowercase letters: 33
# Case 2:
# Enter a sentence: WElcome to Python Class 21CSL46
# No of Words: 5
# No of Digits: 4
# No of Uppercase letters: 7
# No of Lowercase letters: 16