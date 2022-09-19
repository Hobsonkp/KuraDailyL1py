# Return the Sum of Two Numbers
# Create a function that takes two numbers as arguments and returns their sum.
# Examples
#   addition(3, 2) ➞ 5
#   addition(-3, -6) ➞ -9
#   addition(7, 3) ➞ 10
#import math

def add_function(firstNumber, secondNumber):
    sumNumbers=int(firstNumber)+int(secondNumber)
    return sumNumbers

print("Lets enter two numbers for addition")
firstNumber = input("Enter first number : ")
secondNumber = input("Enter second number : ")


print("Sum of the numbers = ",add_function(firstNumber, secondNumber))