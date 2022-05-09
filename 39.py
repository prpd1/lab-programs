#39. Write a program to check whether the given input is digit or lowercase 
#character or uppercase character or a special character.

a = input("enter a digit or lower case or upper case or special character:")

if a.isdigit():
    print("{} is digit".format(a))

if  a.isupper():
    print("{} is upper".format(a))

if  a.islower():
    print("{} is lower".format(a))
    
else :
    print("{} is special character".format(a))

