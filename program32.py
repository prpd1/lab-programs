#32. Write a program to read three sides a, b, c of a triangle and print the type of 
#the triangle.
a = int(input("enter side:"))
b = int(input("enter side:"))
c = int(input("enter side:"))
if ( a==b ) and (b==c) and (c==a)  :
    print("the triangle is equilateral")
elif ( a==b ) or (b==c) or (c==a) :
    print("the triangle is isoceles")
else :
    print("the triangle is scalene")