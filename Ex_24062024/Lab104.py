#Filter in Python
#The filter() function in python is a built in function
#allows you to filter elements in list,tuple,set

numbers = [1,2,3,4,5,6,7,8,9,10]

def is_even(numbers):
    return numbers % 2 == 0

def is_greater_5(numbers):
    return numbers>= 5

new_numbers_even = filter(is_even, numbers)
print(list(new_numbers_even))

new_numbers_greater = filter(is_greater_5, numbers)
print(list(new_numbers_greater))