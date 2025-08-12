# Basic Calculator Program

# Step 1: Get user input
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operation = input("Enter the operation (+, -, *, /): ")

# Step 2: Convert input to float
num1 = float(num1)
num2 = float(num2)

# Step 3: Perform the operation
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operation"

# Step 4: Display the result
print(f"{num1} {operation} {num2} = {result}")
