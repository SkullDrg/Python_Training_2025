#Program to ask for 5 values, sum them up, and present the average of the values

def get_value(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Welcome to value program!")
    values = []
    for i in range(5):
        value = get_value(f"Please enter value {i + 1}: ")
        values.append(value)
    total_sum = sum(values)
    print(f"The sum of the values is: {total_sum}")
    average_value = total_sum / len(values)
    print(f"The average of the values is: {average_value}")

if __name__ == "__main__":
    main()
# This code prompts the user to enter 5 values, calculates their sum, and computes the average.