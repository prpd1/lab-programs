#Rajesh’s basic salary is input through the keyboard. His D.A. is 40% of basic
#salary, and H.R.A. is 20% of basic salary. Write a program to calculate his
#gross salary.

basic_salary = int(input("enter basic salary:"))
dearance_allowance  = (40/100)*basic_salary
h_r_a = (20/100)*basic_salary
gross_salary = (basic_salary)+(dearance_allowance)+(h_r_a)
print(f"gross salary is {gross_salary}")
