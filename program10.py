#Write a program to find the simple interest and compound interest.

principal = int(input("enter principal:"))
time_period = int(input("enter time period:"))
rate_of_interest = float(input("enter rate of interest:"))
simple_interest = (principal * time_period * rate_of_interest) / 100
compound_interest = principal *(1+( rate_of_interest *time_period / 100))
print(f'simple interest is  {simple_interest}')
print(f'compound interest is {compound_interest}')