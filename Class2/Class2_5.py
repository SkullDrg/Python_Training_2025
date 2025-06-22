def get_values(prompt):
    values = []
    for i in range(10):
        while True:
            try:
                value = int(input(f"{prompt} {i + 1}: "))
                values.append(value)
                break
            except ValueError:
                print("Invalid input. Please enter an integer value.")
    return values

def main():
    print("Welcome to the value collector!")
    print("You will be prompted to enter 10 integer values.")
    values = get_values("Enter value")
    print(f"You have entered: {values}")
    print(f"Here is a list of the values in ascending order: {sorted(values)}")
    print(f"Here is a list of the values in descending order: {sorted(values, reverse=True)}")

if __name__ == "__main__":
    main()