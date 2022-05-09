#22. Write a program to print the area of a triangle if three sides are given

a = int(input("enter first side:"))
b = int(input("enter second side:"))
c = int(input("enter third side:"))
s = (a+b+c)/2 #semi_perimeter calculation
area_of_triangle = (s*(s-a)*(s-b)*(s-c))**.5
print(f'area of triangle is {area_of_triangle}')
