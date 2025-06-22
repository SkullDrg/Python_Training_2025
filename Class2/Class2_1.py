def get_name(prompt):
#The `get_name` function handles input and validation.
    while True:
        try:
            name = str(input(prompt)).strip()
            reversed_name = name[::-1]
            return name, reversed_name
        except ValueError:
            print("Invalid input. Please enter a valid name.")

def main():
#The `main` function orchestrates the flow of the program.
    print("Welcome to the Name Reverser!")
    name, reversed_name = get_name("Please enter your name: ")
    print(f"Your name reversed is: {reversed_name}")

if __name__ == "__main__":
    main()

#This code defines a simple program that prompts the user for their name, reverses it, and prints the reversed name.  
#The code is complete and does not require any additional parts to function as intended.