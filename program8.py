#Write a program to find the volume of a cylinder.

radius = int(input("enter a number:"))
height = int(input("enter a number:"))
volume_of_cylinder = (22/7) * (radius ** 2) * height
print(f'volume of cylinder is {round(volume_of_cylinder,2)}')