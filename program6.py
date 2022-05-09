#Write a program to find the area and circumference of a circle.

radius = int(input("enter a number:"))
area_of_circle = (22/7)*radius*radius
circumference_of_circle  = 2*(22/7)*radius
print(f'area of circle is {round(area_of_circle,2)}')
print(f'circumference of circle is {round(circumference_of_circle,2)}')