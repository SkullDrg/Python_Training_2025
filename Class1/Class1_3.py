#This program asks for the user to input it's gender, then checks for "Masculine" or "Feminine"

def get_gender(prompt):
    while True:
        gender = input(prompt).strip().upper()
        if gender == "F":
            return "F"
        elif gender == "M":
            return "M"
        else:
            print("Invalid gender, Please enter 'F' or 'M'.")

gender = get_gender("Tell us your gender, 'F' for Feminine or 'M' for masculine: ")

if gender == "F":
    print("So, you are a woman.")
else:
    print("So you are a man.")