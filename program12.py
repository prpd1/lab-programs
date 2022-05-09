#Write a program to convert the given seconds into hours – minutes – seconds.

x = int(input("enter seconds"))
hours = x//3600
y = x%3600
minutes = y//60
sec = x%60
print(f'{x} is {hours} hours {minutes} minutes and {sec} seconds')