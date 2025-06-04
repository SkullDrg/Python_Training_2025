#Program to test the WHILE method

def grade(prompt):
    while True:
        try:
            value = int(input(prompt))
            if 0 <= value <= 10:
                return value
            else:
                print("Please enter a number between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 10.")

print("Welcome to the grading system!")
grade1 = grade("Please enter a number: ")
print(f"The value inputed was: {grade1}")