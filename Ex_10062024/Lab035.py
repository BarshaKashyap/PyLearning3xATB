# Program - Calculate the area of circle.
# input -> radius
# output -> area
"""
import math

# data types
# input -> int or float -> float
# output -> float

# Core Logic -> pi*r*r = 3.14

radius = float(input("Enter the radius\n"))
# print(math.pi)
area = math.pi * (radius ** 2)
area2 = math.pi * (math.pow(radius, 2))
print(area)
print(area2)

# Single line
print(3.141592653589793 * (float(input("Enter the radius\n")) ** 2))"""

def calculate_square_and_cube(number):

    square = number ** 2

    cube = number ** 3

    return square, cube

number = float(input("Enter the number:"))
square, cube = calculate_square_and_cube(number)
print(f"The square of {number} is {square}")

print(f"The cube of {number} is {cube}")