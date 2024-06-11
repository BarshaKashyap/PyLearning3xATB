"""= is Assignment operator.It is used to assign value to a variable.
The value on the left of = will be the variable name or identifiers
and the value on the right of the = will be variable value or literals
== is comparison operator.
It is used to compare two values to check if they are equal(compare value on the left and right of the == operator)
and it returns bool type
** operator in Python is used to solve mathematical
problem which is required for getting the power of a certain number.

In Python, the ^ operator is known as the bitwise XOR (exclusive OR) operator.
The bitwise XOR operator compares each bit of two integers and returns a new integer."""
x = 6
y = 4

x = x ^ y
y = x ^ y
x = x ^ y

print(x, y)
