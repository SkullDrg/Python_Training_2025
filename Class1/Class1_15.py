#This code gonna get values till the user enters 'q' to quit. Then it's going to print the highest, the lowest
#and the sum of it

def get_numbers():
    numbers = []
    while True:
        user_input = input("Enter a number (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Please enter a valid number.")
    return numbers  

def main():
    print("Welcome to the number collection program!")
    numbers_list = get_numbers()
    print("You entered the following numbers:")
    print(numbers_list)
    if numbers_list:
        print("The highest number is: ", max(numbers_list))
        print("The lowest number is: ", min(numbers_list))
        print("The sum of the numbers is: ", sum(numbers_list))
    else:
        print("No numbers were entered.")

if __name__ == "__main__":
    main()
# This code defines a function to collect numbers from the user until they enter 'q' to quit.
