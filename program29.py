#29. Write a program to find the roots of a given quadratic equation and print the
#nature of roots.

a  = int(input("enter a number:"))
b  = int(input("enter a number:"))
c  = int(input("enter a number:"))
x1= (-b+((b**2-4*a*c)**.5))/2*a
x2= (-b-((b**2-4*a*c)**.5))/2*a
print("the roots are {}, {}".format(x1,x2))
if b**2>4*a*c :
    print("roots are real and different")
elif b**2==4*a*c :
    print("roots are real ")
else :
    print("roots are  complex")