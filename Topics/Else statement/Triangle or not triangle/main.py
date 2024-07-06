x = int(input())
y = int(input())
z = int(input())

angles_sum = x + y + z
triangle_validation = 180

if angles_sum != triangle_validation:
    print("The triangle is not valid!")
else:
    print("The triangle is valid!")