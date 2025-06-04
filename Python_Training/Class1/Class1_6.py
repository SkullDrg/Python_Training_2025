#This program is going to take two values from the user and show the result based on the 
# 4 basics math operations

def get_value(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("This aint a valid value, please enter a numerical value")

def math_operation(prompt):
    while True:
        try:
            operation = int(input(prompt))
            if 1 <= operation <= 4:
                return operation
            else:
                print("1 to 4 options available only.")
        except ValueError:
            print("Choose an operation between 1 to 4.")

def result_operation(x, y, operation):
    if operation == 1:
        return x + y
    elif operation == 2:
        return x - y
    elif operation == 3:
        return x * y
    elif operation == 4:
        if y == 0:
            print("Division by 0 is not allowed.")
            return None
        return x/y

x = get_value("Tell us the first value: ")
y= get_value("Tell us the second value: ")
z = math_operation("Chose a math operation between 1 to 4 being them the respective operations: 1 = add," \
" 2 = sub, 3 = mult and 4 = div: ")

result = result_operation(x, y, z)

if result is not None:
    # Par ou ímpar
    if result % 2 == 0:
        print(f"{result} is even.")
    else:
        print(f"{result} is odd.")

    # Positivo ou negativo
    if result > 0:
        print(f"{result} is positive.")
    elif result < 0:
        print(f"{result} is negative.")
    else:
        print(f"{result} is zero.")

    # Inteiro ou decimal
    if result == int(result):
        print(f"{result} is an integer.")
    else:
        print(f"{result} is a decimal.")