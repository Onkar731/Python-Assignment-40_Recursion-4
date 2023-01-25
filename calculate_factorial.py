"""
Write a recursive function to calculate factorial of a given number
"""

# defining a funtion "factorial()" which takes a number as an agrgument
# and returns the factorial of given number
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)
    
    
# taking input from the user
num = int(input("Enter a number : "))

# printing factorial of given number
print("Factorial :", factorial(num))