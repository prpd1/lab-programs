#Given the coordinates of two points (x1, y1) and (x2, y2). Write a program to find
#the distance between these two points.

x1 = int(input("enter a number:"))
x2 = int(input("enter a number:"))
y1 = int(input("enter a number:"))
y2 = int(input("enter a number:"))
distance = ((x1-x2)**2+(y1-y2)**2)**.5
print("the distance between these two points is:",distance)