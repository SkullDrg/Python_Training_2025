#This code calculates the average of 4 grades entered by the user.

def get_grades(prompt):
    grades = []
    for i in range(4):
        while True:
            try:
                grade = float(input(f"{prompt} {i + 1}: "))
                if 0 <= grade <= 10:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 10. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    return grades

def get_avg(grades):
    if not grades:
        return 0
    return sum(grades) / len(grades)

def main():
    print("Welcome to the Grade Average Calculator!")
    print("You will be prompted to enter 4 grades between 0 and 10.")
    grades = get_grades("Enter grade")  
    avg = get_avg(grades)
    print(f"The average grade is: {avg:.2f}")

if __name__ == "__main__":
    main()