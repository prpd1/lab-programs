#31. Write a program to read ten numbers and print their sum by using ‘if’ statement.

a = (1,2,3,4,5,6,7,8,9,10,11,12)
sum = 0
for i in a:
    sum = sum+i
    if(i == 10):
        break
print("sum of Number of characters entered:",sum)
