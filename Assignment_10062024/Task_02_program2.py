"""Create a program that takes two numbers as input and prints whether the
first number is greater than, less than, or equal to the second number."""


num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
greater_compare = (num1 > num2)
lessthan_compare = (num1 < num2)
equalto_compare = (num1 == num2)

if greater_compare:
    print("num1 is greater than num2")
elif lessthan_compare:
    print("num1 is less than num2")
else:
    print("num1 is equal to num2")
