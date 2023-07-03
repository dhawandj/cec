# b) Write a Python program to find the string similarity between two given string.



import difflib
def string_similarity(str1, str2):
        result = difflib.SequenceMatcher(a=str1.lower(), b=str2.lower())
        return result.ratio()

str1 = input("Enter First string")
str2 = input("Enter Second string")
print("Original string:")
print(str1)
print(str2)
print("Similarity between two said strings:")
print(string_similarity(str1,str2))


# OUTPUT:
# Original string:
# Python Exercises
# Python Exercises
# Similarity between two said strings:
# 1.0
# Original string:
# Python Exercises
# Python Exercise
# Similarity between two said strings:
# 0.967741935483871