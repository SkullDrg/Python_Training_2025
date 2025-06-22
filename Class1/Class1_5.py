#This program is goig to ask for the user 4 grades, then gonna calculate the student's final grade

def get_name(prompt):
    while True:
        name = input(prompt).title().strip()
        if name.replace(" ", "").isalpha():
            return name
        else:
            print("Invalid name. Please enter only alphabetic characters")
            
def get_grade(prompt):
    while True:
        try:
            grade = float(input(prompt))
            if 0 <= grade <= 10:
                 return grade
            else:
                print("Grade must be between 0 and 10.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 10.")

def final_grade(x, y, z, w):
    return(x + y + z + w)/4

def main():
    print("Welcome to the Grade Average Calculator!")
    print("You will be prompted to enter 4 grades between 0 and 10.")
    name = get_name("Enter the student's name: ")
    x = get_grade(f"Enter {name}'s first grade: ")
    y = get_grade(f"Enter {name}'s second grade: ")
    z = get_grade(f"Enter {name}'s third grade: ")
    w = get_grade(f"Enter {name}'s fourth grade: ")

    Avg = final_grade(x, y, z, w)

    if Avg > 7 and Avg != 10:
        print(f"{name}'s final grade is {Avg}, so it is approved")
    elif Avg < 7:
        print(f"{name}'s final grade is {Avg}, so it failed")
    else:
        print(f"{name}'s final grade is {Avg}, so it is approved with a golden star")

if __name__ == "__main__":
    main()