#Write a program to calculate the monthly income of a person using the 
#following commission schedule:
#Monthly sales income
#>= Rs.50,000 Rs.375 + 16% sales.
#>= Rs.50,000 but >=Rs.40,000 Rs. 350+14% sales.
#<= Rs.40,000 but >=Rs.30,000 Rs. 325+12% sales.<= Rs.30,000 but >=Rs.20,000 Rs. 300+9% sales.
#<= Rs.20,000 but >=Rs.10,000 Rs. 250+5% sales.
#<= Rs.10,000 Rs. 200+3% sales.

sales_income = int(input("enter number of sales:"))
if sales_income >= 50000:
    commission = (375 + sales_income * (16/100))
    print("commission for {} is {}".format(sales_income,commission))
if sales_income <= 50000 and sales_income >= 40000:
    commission = (350 + sales_income *(14/100))
    print("commission for {} is {}".format(sales_income,commission))
if sales_income <= 40000 and sales_income >= 30000:
    commission = 325 + sales_income *(12/100)
    print("commission for {} is {}".format(sales_income,commission))
if sales_income <=30000 and sales_income >= 20000:
    commission = 300 + sales_income *(9/100)
    print("commission for {} is {}".format(sales_income,commission))
if sales_income <=20000 and sales_income >= 10000:
    commission = 250 + sales_income *(5/100)
    print("commission for {} is {}".format(sales_income,commission))
if sales_income <= 10000:
    commission = 200 + sales_income * (3/100)
    print("commission for {} is {}".format(sales_income,commission))