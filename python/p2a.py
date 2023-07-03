# 2) AIM: Demonstrating creation of functions, passing parameters and return values
# a) Defined a function F as Fn= Fn-1+Fn-2 . Write a python program which accepts a value for
# N (where N>0) as input and pass this value to the function. Display suitable error message if
# the condition for input value is not allowed.
def recur_fibo(n):

        if n <= 1:
                return n
        else:
                return(recur_fibo(n-1) + recur_fibo(n-2))
        
        
nterms = int(input("Enter the number"))

# check if the number of terms is valid
if nterms <= 0:
        
        print("Please enter a positive integer")
else:
        print("Fibonacci sequence:")
                
for i in range(nterms):
        print(recur_fibo(i))

# OUTPUT:
# CASE1:
# Enter the number5
# Fibonacci sequence:
# 0
# 1
# 1
# 2
# 3

# CASE 2:
# Enter the number-5
# Please enter a positive integer