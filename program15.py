# Two numbers are input into two locations ‘a’ and ‘b’. Write a program to
#interchange the contents of ‘a’ and ‘b’ without using temporary variables.

a = int(input("enter a number for a:"))
b = int(input("enter a numberfor b:"))
a,b =b,a
print("interchange of contents of a and b:",a,b)