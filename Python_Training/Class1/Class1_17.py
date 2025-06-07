#This code defines a function to calculate the factorial of a number using recursion until the user enters 'q' to quit.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        print("Factorial is not defined for negative numbers.")
        return None
    else:
        return n * factorial(n - 1)
    
def get_numbers():
    number = None
    while True:
        user_input = input("Enter a number between 1 and 16 to calculate its factorial (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        try:
            number = int(user_input)
            if 1 <= number <= 16:
                return number
            elif number < 0:
                print("Please enter a non-negative integer.")
            else:
                print("Please enter a number between 1 and 16.")
        except ValueError:
            print("Please enter a valid integer.")

def main():
    print("Welcome to the factorial calculator!")
    while True:
        number = get_numbers()
        if number is None:
            break
        result = factorial(number)
        if result is not None:
            print(f"The factorial of {number} is: {result}")
    print("Thank you for using the factorial calculator!")

if __name__ == "__main__":
    main()