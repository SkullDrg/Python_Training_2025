def get_values(prompt):
    values = []
    for i in range(10):
        while True:
            try:
                value = float(input(f'{prompt} {i + 1}: '))
                values.append(value)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    return values

def main():
    print("Welcome to the Value Collector!")
    print("You will be prompted to enter 10 numeric values.")
    values = get_values("Enter value")
    print(f"You have entered: {values}")
    print(f"The biggest values is: {max(values)}")
    print(f"The smallest values is: {min(values)}")

if __name__ == "__main__":
    main()

# This code collects 10 numeric values from the user and displays the largest and smallest values.
# It includes error handling to ensure valid numeric input.