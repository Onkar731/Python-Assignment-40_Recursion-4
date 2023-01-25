"""
Write a recursive function to calculate sum of digits of a given number
"""

# defining a function "sum_of_digits()" which takes a number as an argument
# and return the sum of all digits of the number
def sum_of_digits(num):
    if num <= 0:
        return 0
    else:
        return num%10 + (sum_of_digits(num//10))
    
    
# taking input from the user
num = int(input("Enter a number : "))

# printing sum of digits
print("Sum of digits :", sum_of_digits(num))