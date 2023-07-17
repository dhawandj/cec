# PYTHON LAB PROGRAM 6
# 6) AIM: Demonstration Of reading, writing and organising files
# a) Write a python program to accept a file name from the user and perform the followingoperations
# 1. Display the first N line of the file
# 2. Find the frequency of occurrence of the word accepted from the user in the file
# Code:

import os.path
import sys

fname = input("Enter the filename: ")

if not os.path.isfile(fname):
        print("File", fname, "doesn't exist")
        sys.exit(0)

with open(fname, "r") as infile:
        lineList = infile.readlines()

for i in range(min(8, len(lineList))):
        print(i+1, ":", lineList[i].strip())

word = input("Enter a word: ")
cnt = 0
for line in lineList:
        cnt += line.count(word)

print("The word", word, "appears", cnt, "times in the file")

# OUTPUT:
# Enter the filename: example.txt
# 1 : Hello my name is Tom the cat.
# 2 : I like to play and work with my dear friend jerry mouse.
# 3 : We both have our office and email addresses
# 4 : They are tomcat@gmail.com, jerrymouse@gmail.com.
# 5 : Our friend spike has also joined us in our company.
# 6 : His email address is spikethedog@gmail.com.
# 7 : We all entertaint the children through our show.
# 8 : My phone number is +919986059013, +918310681568
# Enter a word: email
# The word email appears 2 times in the file