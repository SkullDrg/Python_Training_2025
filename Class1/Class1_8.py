#Gas station program to calculate the cost of gas or alcohol based on how many liters are purchased.

A = 1.90
G = 2.50

def fuel_type(prompt):
    while True:
        try:
            fuel = str(input(prompt)).lower()
            if fuel in ['a', 'g']:
                return fuel
            else:
                print("Invalid input. Please enter 'A' for alcohol or 'G' for gas.")
        except ValueError:
            print("Invalid input. Please enter 'A' for alcohol or 'G' for gas.")

def liters(prompt):
    while True:
        try:
            liters = float(input(prompt))
            if liters > 0:
                return liters
            else:
                print("Please enter a positive number for liters.")
        except ValueError:
            print("Invalid input. Please enter a valid number for liters.")

def calculate_cost(fuel, liters):
    if fuel == 'a':
        discount = 0.03 if liters <= 20 else 0.05
        cost = liters * A * (1 - discount)
    else:
        discount = 0.04 if liters <= 20 else 0.06
        cost = liters * G * (1 - discount)
    return cost

print("Welcome to the Gas Station!")
fuel = fuel_type("Enter 'A' for alcohol or 'G' for gas: ")
liters_purchased = liters("Enter the number of liters purchased: ")
cost = calculate_cost(fuel, liters_purchased)
print(f"The total cost for {liters_purchased} liters of {'alcohol' if fuel == 'a' else 'gas'} is: ${cost:.2f}")