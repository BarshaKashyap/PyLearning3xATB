def compare_numbers(num1, num2):
    if num1 > num2:

        return "The first number is greater than the second number."

    elif num1 < num2:

        return "The first number is less than the second number."

    else:

        return "The first number is equal to the second number."

 #  Example usage
num1 = int(input("Enter the first no:"))
num2 = int(input("Enter the 2nd no:"))
result = compare_numbers(num1, num2)
print(result)
