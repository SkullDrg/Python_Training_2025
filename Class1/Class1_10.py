#Program to check if the username and password are the same

def get_username(prompt):
    while True:
        try:
            username = input(prompt)
            if username.isalnum() and len(username) >= 3:
                return username
            else:
                print("Username must be at least 3 characters long and contain only letters and numbers.")
        except ValueError:
            print("Invalid input. Please enter a valid username.")

def get_password(prompt):
    while True:
        try:
            password = input(prompt)
            if password != username:
                if len(password) >= 6:
                    return password
                else:
                    print("Password must contain more than 6 characters.")
            else:
                print("Password cannot be the same as the username.")
        except ValueError:
            print("Invalid input. Please enter a valid password.")

print("Welcome to login system!")
username = get_username("Please enter a username: ")
password = get_password("Please enter a password: ")
print(f"Username: {username}")
print(f"Password: {password}")