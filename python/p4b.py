# b) Write a python program to convert Roman numbers into integer numbers usingdictionaries

class py_solution:
        def roman_to_int(self, s):
                rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
                int_val = 0
                for i in range(len(s)):
                        if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                                        int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
                        else:
                                int_val += rom_val[s[i]]
                return int_val
print(py_solution().roman_to_int('MMMCMLXXXVI'))
print(py_solution().roman_to_int('VIII'))
print(py_solution().roman_to_int('C'))

# OUTPUT:
# 3986
# 8
# 100