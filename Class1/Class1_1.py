#This program asks for two values to the user and checks which one is greater

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a number, try again")

x = get_float("Tell me a number: ")
y = get_float("Tell me another number: ")

tolerance = 1e-9

if abs(x - y) < tolerance:
    print("Both numbers are equal.")
elif (x > y):
    print("The first number is greater")
else:
    print("The second number is greater")