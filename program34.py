#Write a program to read a 3-digit number and find whether the middle digit is 
#numerically equal to the sum of the other two digits and prints an appropriate 
#response.
import math
a = int(input("enter three digit number:"))
middle_digit = round((a/10)%10)
last_digit  = a%10
first_digit = round(a/100)
if middle_digit == first_digit+last_digit:
    print('sum of {} and {} is equal to {} '.format(first_digit,last_digit,middle_digit))
else :
    print('sum of {} and {} is not equal to {} '.format(first_digit,last_digit,middle_digit))
