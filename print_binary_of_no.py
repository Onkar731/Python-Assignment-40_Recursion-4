"""
Write a recursive function to print binary of a given decimal number
"""

# defining a function "binary()" which takes a number as an argument
# and print the equivalent binary of the decimal number
def binary(num):  
    if num >= 1:
        binary(num//2)
        print(num%2, end='')
        

# taking input from the user
num = int(input("Enter a number : "))

# calling binary() to print binary of the decimal number
print('0b', end='')
binary(num)