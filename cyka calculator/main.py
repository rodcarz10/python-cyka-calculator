# Define functions for each operation
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Get the operation from the user
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation
if operation == "+":
    result = add(num1, num2)
elif operation == "-":
    result = sub(num1, num2)
elif operation == "*":
    result = mul(num1, num2)
elif operation == "/":
    result = div(num1, num2)
else:
    result = "Error: Invalid operation!"

# Display the result
print("Result:", result)