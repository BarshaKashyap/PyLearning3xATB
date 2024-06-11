"""Develop a Python script that calculates the square and cube of a given number.
 num = 2 sq - 4, c = 8"""
import math

num = 2
print(num)
square = num ** 2
cube = num ** 3
print("square of the num is:", square)# Calculate square of a number
print("cube of the num is:", cube)    # Calculate Cube of a number

#OR

print("square of the num is: ", math.pow(num,2))# Calculate square of a number
print("cube of the num is: ", math.pow(num,3))  # Calculate Cube of a number

# We can also do it if user inputs the number
num = float(input("Enter a number:"))
print(num)
square = num ** 2
cube = num ** 3

#OR

print("square of the num is: ", math.pow(num,2))  # Calculate square of a number
print("cube of the num is: ", math.pow(num,3))  # Calculate Cube of a number
