#This program asks the user for a letter and checks if it's a vowel or a consonant

def get_letter(prompt):
    while True:
        try:
            letter = str(input(prompt)).strip().upper()
            if len(letter) != 1 or not letter.isalpha():
                print("Please enter a single alphabet letter.")
                continue
            return letter
        except ValueError:
            print("Invalid input, try again")

Vowel = {"A", "E", "I", "O", "U"}

letter = get_letter("Tell us a letter: ")

if letter in Vowel:
    print("The letter is a vowel")
else:
    print("The letter is a consonant")