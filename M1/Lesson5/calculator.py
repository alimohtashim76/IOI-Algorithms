# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

num1 = int(input("Enter First Number "))
num2 = int(input("Enter Second Number: "))
operation = input("Enter the operation: ")

if operation == '+':
    print("Sum :", add(num1, num2))
elif operation == '-':
    print("Difference :", subtract(num1, num2))
elif operation == '*':
    print("Product :", multiply(num1, num2))
elif operation == '/':
    print("Quotient :", divide(num1, num2))
else:
    print("Invalid Operation")



