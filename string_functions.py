# Using single quotes
str1 = 'Hello Python'
print(str1)
# Using double quotes
str2 = "Hello Python"
print(str2)

# Using triple quotes
str3 = '''''Triple quotes are generally used for  
    represent the multiline or 
    docstring'''
print(str3)

str = "HELLO"
print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])
# It returns the IndexError because 6th index doesn't exist
#print(str[6])

str = "JAVATPOINT"
# Start Oth index to end
print(str[0:])
# Starts 1th index to 4th index
print(str[1:5])
# Starts 2nd index to 3rd index
print(str[2:4])
# Starts 0th to 2nd index
print(str[:3])
#Starts 4th to 6th index
print(str[4:7])

str = 'JAVATPOINT'
print(str[-1])
print(str[-3])
print(str[-2:])
print(str[-4:-1])
print(str[-7:-2])
# Reversing the given string
print(str[::-1])
print(str[-12])

str = "HELLO"
str[0] = "h"
print(str)

