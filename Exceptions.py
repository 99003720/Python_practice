

try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = a/b
except:
    print("Can't divide with zero")

try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = a/b
    print("a/b = %d"%c)

except Exception:
    print("can't divide by zero")
    print(Exception)
else:
    print("Hi I am else block")



try:
    a = int(input("Enter a:"))
    b = int(input("Enter b:"))
    c = a/b
    print("a/b = %d"%c)

except Exception as e:
    print("can't divide by zero")
    print(e)
else:
    print("Hi I am else block")


try:
    age = int(input("Enter the age:"))
    if(age < 18):
        raise ValueError
    else:
        print("the age is valid")
except ValueError:
    print("The age is not valid")

try:
     num = int(input("Enter a positive integer: "))
     if(num <= 0):
    
         raise ValueError
except ValueError as e:
     print(e)

