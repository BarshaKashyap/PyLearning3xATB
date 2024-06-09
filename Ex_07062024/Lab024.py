# List - Shopping List
# Apple, Banana, Cucumber, Dragonfruit
# 1. Add item
# 2. Remove item
# 3. Update item
# 4. View item
# 5. Exit


shopping_list = ["Apple", "Banana", "Cucumber", "Dragonfruit"]
print(shopping_list)
print(len(shopping_list))
print(shopping_list[0])
print(shopping_list[-1])

shopping_list.append("Eggplant") # Add item in the end
print(shopping_list)
shopping_list.insert(5, "Guava") # Add item in the middle
print(shopping_list)

shopping_list.extend(["Honey", "Icecream"]) # Add multiple items in the end
print(shopping_list)

shopping_list.remove("Apple") # Remove item
print(shopping_list)
print(shopping_list.pop()) #   Remove and return item at index (default last).
print(shopping_list.index("Cucumber"))
shopping_list.reverse()
print(shopping_list)
shopping_list.sort()
print(shopping_list)
print(shopping_list)
shopping_list[0] ="Replacedwith barsha"
print(shopping_list)

#
my_list = [1, 2, 3, 4, True, 3.14, "Barsha"]
print(type(my_list))  # <class 'list'>
print(len(my_list))
print(my_list[0])
my_list.reverse()
print(my_list)
