def get_values(prompt):
    values = []
    even_values = []
    odd_values = []
    for i in range(10):
        while True:
            try:
                value = int(input(f"{prompt} {i + 1}: "))
                values.append(value)
                # Check if the value is even or odd
                if value %2 == 0:
                    even_values.append(value)
                else:
                    odd_values.append(value)
                break
            except ValueError:
                print("Invalid input. Please enter an integer value.")
    return values, even_values, odd_values

def main():
    print("Welcome to the value collector!")
    print("You will be prompeted to enter 10 integer values.")
    values, even_values, odd_values = get_values("Enter value")
    print(f"You have entered: {values}")
    print(f"The even values are: {even_values}")
    print(f"The odd values are: {odd_values}")
    print(f"Among the even values, the biggest is: {max(even_values)} and the smallest is: {min(even_values)}")
    print(f"Among the odd values, the biggest is: {max(odd_values)} and the smallest is: {min(odd_values)}")

if __name__ == "__main__":
    main()