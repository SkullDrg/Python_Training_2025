def Person_info():
    person = {}
    while True:
        try:
            person_name = input("Enter person's name: ").strip()

            if not person_name:
                raise ValueError("Name cannot be empty")
            
            name_without_spaces = person_name.replace(" ", "")
            if not name_without_spaces.isalpha():
                raise ValueError("Name must contain only letters and spaces")
            
            break # Valid name
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

    while True:
        try:
            person_surname = input(f"Enter {person_name}'s surname: ").strip()

            if not person_surname:
                raise ValueError("Surname cannot be empty")
            
            surname_without_spaces = person_surname.replace(" ", "")
            if not surname_without_spaces.isalpha():
                raise ValueError("Surname must contain only letters and spaces")
            
            break # Valid surname
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

    while True:
        try:
            person_age = int(input(f"Enter {person_name}'s age: "))
            if person_age < 0 or person_age > 120:
                raise ValueError("Age must be between 0 and 120")
            
            break # Valid age
        except ValueError as e:
            print(f"Invalid input: Age must be a number between 0 and 120. Please try again.")

    while True:
        try:
            person_email = input(f"Enter {person_name}'s email: ").strip()
            if not person_email:
                raise ValueError("Email cannot be empty")
            if "@" not in person_email or "." not in person_email:
                raise ValueError("Email must contain '@' and '.' characters")
            
            break # Valid email
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

    person[person_name] = {
        "surname": person_surname,
        "age": person_age,
        "email": person_email
    }

    return person

def main():
    person_info = Person_info()
    print("\nPerson Information:")
    for name, details in person_info.items():
        print(
            f"\nName: {name}\n"
            f"Surname: {details['surname']}\n"
            f"Age: {details['age']}\n"
            f"Email: {details['email']}\n"
        )

if __name__ == "__main__":
    main()