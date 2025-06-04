#This program asks the user for a value then checks if it's positve or negative

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a valid value, try again")

x = get_float("Tell me a value: ")

if (x > 0):
    print("The value is positive")
else:
    print("The value is negative")