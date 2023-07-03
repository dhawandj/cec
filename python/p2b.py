# b) Develop a python program to convert binary to decimal, octal to hexadecimal using
# functions.
def binary_to_decimal(binary):
    decimal = 0
    power = 0
    while binary != 0:
        decimal += (binary % 10) * (2 ** power)
        binary //= 10
        power += 1
    return decimal

def octal_to_hexadecimal(octal):
    decimal = 0
    power = 0
    while octal != 0:
        decimal += (octal % 10) * (8 ** power)
        octal //= 10
        power += 1

    hexadecimal = ""
    while decimal != 0:
        remainder = decimal % 16
        if remainder < 10:
            hexadecimal = str(remainder) + hexadecimal
        else:
            hexadecimal = chr(ord('A') + remainder - 10) + hexadecimal
        decimal //= 16

    return hexadecimal

binary_number = input("Enter a binary number: ")
decimal_number = binary_to_decimal(int(binary_number))
print("Decimal equivalent:", decimal_number)

octal_number = input("Enter an octal number: ")
hexadecimal_number = octal_to_hexadecimal(int(octal_number))
print("Hexadecimal equivalent:", hexadecimal_number)



# Output:
# Enter a binary number: 101
# Decimal equivalent: 5
# Enter an octal number: 755
# Hexadecimal equivalent: 1ED