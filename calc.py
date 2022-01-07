#function to add numbers
def add(a, b):
    return int(a)+int(b)
        
#function to subtract numbers
def subtract(a, b):
    return int(a)-int(b)

#function to multiply numbers
def multiply(a, b):
    return int(a)*int(b)





if __name__ == '__main__':
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
    
    








