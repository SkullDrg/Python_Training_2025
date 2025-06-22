#This program is going to evaluate some infos provided by the user

def get_name(prompt):
    while True:
        try:
            name = str(input(prompt)).strip()
            if len(name) > 3:
                return name
            else:
                print("Name must be at least 4 characters long.")
        except ValueError:
            print("Invalid input. Please enter a valid name.")

def get_age(prompt):
    while True:
        try:
            age = int(input(prompt))
            if 0 <= age <= 150:
                return age
            else:
                print("You cant be older than 150 or younger than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid age.")

def get_salary(prompt):
    while True:
        try:
            salary = float(input(prompt))
            if salary >= 0:
                return salary
            else:
                print("Salary cant be negative.")
        except ValueError:
            print("Invalid input. Please enter a valid salary.")

def get_gender(prompt):
    gender_map = {"f": "feminine", "m": "masculine"}
    while True:
        try:
            gender = str(input(prompt)).strip().lower()
            if gender in gender_map:
                return gender_map[gender]
            else:
                print("Please enter 'f' for feminine or 'm' for masculine.")
        except ValueError:
            print("Invalid input. Please enter a valid gender.")

def get_marital_status(prompt):
    marital_status_map = {
        "s": "Single",
        "m": "Married",
        "d": "Divorced",
        "w": "Widowed"
    }
    while True:
        try:
            status = str(input(prompt)).strip().lower()
            if status in marital_status_map:
                return marital_status_map[status]
            else:
                print("Please enter 's' for Single, 'm' for Married, 'd' for Divorced, or 'w' for Widowed.")
        except ValueError:
            print("Invalid input. Please enter a valid marital status.")

def main():
    print("Welcome to the user information system!")
    name = get_name("Please enter your name: ")
    age = get_age("Please enter your age: ")
    salary = get_salary("Please enter your salary: ")
    gender = get_gender("Please enter your gender ")
    marital_status = get_marital_status("Please enter your marital status (s/m/d/w): ")
    print("\nUser Information:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Salary: {salary}")
    print(f"Gender: {gender}")
    print(f"Marital Status: {marital_status}")

if __name__ == "__main__":
    main()