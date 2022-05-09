#Write a program to read the marks of 3 subjects and display the total, average,
#class.

subject1 = int(input("enter the marks:"))
subject2 = int(input("enter the marks:"))
subject3 = int(input("enter the marks:"))
total = subject1+subject2+subject3
average = total/3
print(f'toatal marks is {total}')
print(f'average marks is {average}')