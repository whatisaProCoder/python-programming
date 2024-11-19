# Calculate area of a triangle by taking values of edges from user.

base, height = map(float, input(
    "Enter base and height of triangle : ").split())

area = 0.5 * base * height
print(f"Area of triangle = {area}")
