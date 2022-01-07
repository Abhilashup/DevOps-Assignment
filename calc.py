def add(a, b):
    return int(a)+int(b)
        

def subtract(a, b):
    return int(a)-int(b)

def multiply(a, b):
    return int(a)*int(b)



num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
operation = input(str("Enter the operation : "))

if operation == "+":
    print(add(num1,num2))

elif operation == "-":
    print(subtract(num1, num2))

elif operation == "*":
    print(multiply(num1, num2))

else:
    print("Invalid Operation")






