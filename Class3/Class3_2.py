def student_info():
    student = {}
    situation = ""

    while True:
        try:
            student_name = input("Enter student's name: ").strip()

            if not student_name:
                raise ValueError("Name cannot be empty")
            
            name_without_spaces = student_name.replace(" ", "")
            if not name_without_spaces.isalpha():
                raise ValueError("Name must contain only letters and spaces")
            
            break  # Valid name
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

    grades = []
    for i in range(1, 5):
        while True:
            try:
                student_grade = float(input(f"Enter {student_name}'s {i}º grade: "))
                if student_grade < 0 or student_grade > 10:
                    raise ValueError("Grade must be between 0 and 10")
                grades.append(student_grade)
                break  # Valid grade
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

    student[student_name] = {
        "grade1": grades[0],
        "grade2": grades[1],
        "grade3": grades[2],
        "grade4": grades[3],
        "Highest_Grade": max(grades),
        "Lowest_Grade": min(grades),
        "Average_Grade": sum(grades) / len(grades)
    }

    if student[student_name]["Average_Grade"] >= 7:
        situation = "Approved"
    else:
        situation = "Reproved"

    return student, situation

def main():
    student, situation = student_info()
    student_name = list(student.keys())[0]
    print(f"\nStudent: {student_name}")
    print(f"Grades: {student[student_name]['grade1']}, {student[student_name]['grade2']}, "
          f"{student[student_name]['grade3']}, {student[student_name]['grade4']}")
    print(f"Highest Grade: {student[student_name]['Highest_Grade']}")
    print(f"Lowest Grade: {student[student_name]['Lowest_Grade']}")
    print(f"Average Grade: {student[student_name]['Average_Grade']:.2f}")
    print(f"Situation: {situation}")

if __name__ == "__main__":
    main()