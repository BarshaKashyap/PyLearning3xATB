# ✅ Conditions
# age > 18 -> You are allowed to vote
# age < 18 -> You are not allowed

# barsha -> vote -> govt permission
# barsha -> no vote -> no permission

# If, ELSE
# Syntax
# if condition:
#     code to be executed
# else:
#     code to be executed when condition is false

# Write a program to take a user age and let him know if he can go the club.

# Take a user input

age = int(input("Enter your Age"))

if age >= 18:
    print("Go to vote")
else:
    print("Not allowed to vote")