# This code defines a function to collect numbers from the user until they enter 'q' to quit but, it only 
# accepts values from 1 to 1000

def get_numbers():
    numbers = []
    while True:
        user_input = input("Enter a number (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        try:
            number = float(user_input)
            if 1 <= number <= 1000:
                numbers.append(number)
            else:
                print("Please, enter a value between 1 and 1000.")
        except ValueError:
                print("Please enter a valid number.")
    return numbers

def main():
     print("Welcome to number collection program!")
     number_list = get_numbers()
     print("You entered the folowwing numbers:")
     print(number_list)
     if number_list:
         print("The highest number is: ", max(number_list))
         print("The lowest number is: ", min(number_list))
         print("The sum of the numbers is: ", sum(number_list))
     else:
         print("No numbers were entered.")

if __name__ == "__main__":
    main()
# This code defines a function to collect numbers from the user until they enter 'q' to quit, but it only
# accepts values from 1 to 1000