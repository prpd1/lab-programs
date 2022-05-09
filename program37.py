#37. Write a program to read a character and find out whether it is uppercase or 
#lowercase.

a = input("enter a  lower case or upper case :")

if  a.isupper():
    print("{} is upper".format(a))

if  a.islower():
    print("{} is lower".format(a))
    
