# Program to print the odd numbers from 1 to 50

def odd_numbers():
    odds = []
    for i in range(51):
        if i % 2 != 0:
            odds.append(i)
    return odds

def main():
    print("Welcome to the odd numbers program!")
    odds_list = odd_numbers()
    print("The odd numbers from 1 to 50 are:")
    print(odds_list)

if __name__ == "__main__":
    main()
# This code defines a function to generate odd numbers from 1 to 50 and prints them.
# It uses a loop to check each number and collects the odd ones in a list.