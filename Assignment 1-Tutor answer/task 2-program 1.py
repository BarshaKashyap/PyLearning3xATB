def calculate_circle_area(radius):

    pi = 3.14

    area = pi * (radius ** 2)

    return area

# Example usage

radius = float(input("Enter the radius of the circle: "))

area = calculate_circle_area(radius)

print(f"The area of the circle with radius {radius} is {area}")