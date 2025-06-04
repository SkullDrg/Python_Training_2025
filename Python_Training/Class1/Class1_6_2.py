#Cleaner version of the class 1_6

def get_value(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operation():
    while True:
        try:
            op = int(input("Choose an operation:\n1 = Add\n2 = Subtract\n3 = Multiply\n4 = Divide\nYour choice: "))
            if op in (1, 2, 3, 4):
                return op
            print("Only options 1 to 4 are valid.")
        except ValueError:
            print("Please enter a number between 1 and 4.")

# Get inputs
x = get_value("Enter first number: ")
y = get_value("Enter second number: ")
op = get_operation()

# Perform operation
operations = {
    1: x + y,
    2: x - y,
    3: x * y,
    4: x / y if y != 0 else None
}

result = operations[op]

# Result checks
if result is None:
    print("Division by zero is not allowed.")
else:
    print(f"Result: {result}")
    print("Even" if result % 2 == 0 else "Odd")
    print("Positive" if result > 0 else "Negative" if result < 0 else "Zero")
    print("Integer" if result == int(result) else "Decimal")