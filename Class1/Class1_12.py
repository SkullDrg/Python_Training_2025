#Program to ask for 5 values and print the biggest one

def get_value(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    print("Welcome to the value comparison program!")
    values = []
    for i in range(5):
        value = get_value(f"Please enter value {i + 1}: ")
        values.append(value)
    
    biggest_value = max(values)
    print(f"The biggest value is: {biggest_value}")

if __name__ == "__main__":
    main()