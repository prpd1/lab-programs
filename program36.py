#Write a program to read the characters continuously until ‘$’ is given and 
#display the number of characters entered.

a = str(input("Enter characters: "))
char_count = 0
for i in a:
    char_count = char_count+1
    if ( i == '$' ):
        break
print("Number of characters entered:",char_count)
