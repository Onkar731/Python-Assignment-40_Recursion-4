"""
Write a recursive function to print octal of a given decimal number
"""

# defining a function "octal()" which takes a number as an argument
# and print the equivalent octal of the decimal number
def octal(num):  
    if num >= 1:
        octal(num//8)
        print(num%8, end='')
        

# taking input from the user
num = int(input("Enter a number : "))

# calling octal() to print octal of the decimal number
print('0o', end='')
octal(num)