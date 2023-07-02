# b) Develop a Python program to check whether a given number is palindrome or not and also
# count the number of occurrences of each digit in the input number.
try:

        number = int(input("Enter the number: "))
        temp = number
        reverse = 0
        count = 0
        occurrences = {}
        while number > 0:
                digit = number % 10

                if digit in occurrences:
                         occurrences[digit] += 1
                else:
                        occurrences[digit] = 1

                reverse = reverse * 10 + digit
                number //= 10
                count += 1
        

        print("The reverse number is:", reverse)

        if temp == reverse:
                print("The number is a palindrome")
        else:
                print("The number is not a palindrome")

        print("Number of digits:", count)
        print("Digit occurrences:", occurrences)
except ValueError:
        print("Invalid input. Please enter a valid integer.")


# OUTPUT:
# Case 1:
# Enter the number: 1233
# The reverse number is: 3321
# The number is not a palindrome
# Number of digits: 4
# Digit occurrences: {3: 2, 2: 1, 1: 1}
# Case 2:
# Enter the number: 121
# The reverse number is: 121
# The number is a palindrome
# Number of digits: 3
# Digit occurrences: {1: 2, 2: 1}
# Case 3:
# Enter the number: ABC
# Invalid input. Please enter a valid integer.