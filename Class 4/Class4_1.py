def choosing_function():
    Options = ['+', '-', '*', '/']
    while True:
        try:
            choice = input("Please, choose a function based on the following options:\n" \
            " (+) Add\n (-) Subtract\n (*) Multiply\n (/) Divide\n\nYour choice: ").strip()
            if choice in Options:
                return choice
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print("Error:", e)

def calculate(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        if b != 0:
            return a / b
        else:
            raise ValueError("Cannot divide by zero.")
    else:
        raise ValueError("Invalid operation.")
    
def main():
    try:
        print("Welcome to the Simple Calculator!")
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        operation = choosing_function()
        result = calculate(a, b, operation)
        print(f"The result of {a} {operation} {b} is: {result}")
    except ValueError as ve:
        print("Value Error:", ve)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
# This code defines a simple calculator that allows the user to choose an operation and perform calculations.