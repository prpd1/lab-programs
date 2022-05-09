
#18. The distance between two cities in Km. is input through the keyboard. Write a
#program to convert and print the result in meters and centimetres.
 
distance_bw_two_cities = int(input("enter distance between two cities in km:"))
meter_conversion = distance_bw_two_cities/1000
centimeter_conversion = distance_bw_two_cities/100000
print(f'km in meters is {meter_conversion}')
print(f'km in centimeters is {centimeter_conversion}')