# PYTHON LAB PROGRAM 5

# 5) AIM: Demonstration of pattern recognition with and without using regularexpressions.
# a) Write a function called isphonenumber () to recognize a pattern 415-555-242 without using regular expression
# and also write the code to recognize the same patternusing regular expression.
import re
def isphonenumber(numStr):
    
        if len(numStr) != 12:

                return False
        for i in range(len(numStr)):

                if i==3 or i==7:

                        if numStr[i] != "-":
                                return False
                else:
                                
                        if numStr[i].isdigit() == False:
                                        return False
        return True

def chkphonenumber(numStr):

        ph_no_pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
        if ph_no_pattern.match(numStr):
                return True
        else:
                return False

ph_num = input("Enter a phone number : ")
print("Without using Regular Expression")
if isphonenumber(ph_num):
        print("Valid phone number")
else:
        print("Invalid phone number")

print("Using Regular Expression")
if chkphonenumber(ph_num):
        print("Valid phone number")
else:
        print("Invalid phone number")



# OUTPUT:
# CASE 1:
# Enter a phone number: 2e34-334-32
# Without using Regular Expression
# Invalid phone number
# Using Regular Expression
# Invalid phone number
# CASE 2:
# Enter a phone number: 234-567-2345
# Without using Regular Expression
# Valid phone number
# Using Regular Expression
# Valid phone number