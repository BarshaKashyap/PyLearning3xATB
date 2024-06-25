
my_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}
#to find a key
"""for k,v in my_dict.items():
    if k == 'b':
        print("key with the name b is found")

op = 'b' in my_dict
print(op)"""

# Iterate through the keys and print their values
for key in my_dict:
    print(f"The value of the key '{key}' is {my_dict[key]}")

# Iterate through the values and print them
for value in my_dict.values():
    print(value)

