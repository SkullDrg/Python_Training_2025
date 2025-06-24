def student_info():
    student = {}
    situation = ""

    while True:
        try:
            student_name = input("Enter student's name: ").strip()

            if not student_name:
                raise ValueError("Name cannot be empty")
            
            name_without_sapces = student_name.replace(" ", "")
            if not name_without_sapces.isalpha():
                raise ValueError("Name must contain only letters and spaces")
            
            break #Valid name
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
                break #Valid grade
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

    student[student_name]["Situation"] = situation
    return student

def main():
    all_students = {}

    for i in range(1, 8):  # Loop for 7 students
        print(f"\n--- Entering information for student {i} ---")
        student_info_dict = student_info()
        all_students.update(student_info_dict)

    # Print info for all students
    print("\n===== All Students Information =====")
    for student_name, info in all_students.items():
        print(f"\nStudent: {student_name}")
        print(f"Grades: {info['grade1']}, {info['grade2']}, {info['grade3']}, {info['grade4']}")
        print(f"Highest Grade: {info['Highest_Grade']}")
        print(f"Lowest Grade: {info['Lowest_Grade']}")
        print(f"Average Grade: {info['Average_Grade']:.2f}")
        print(f"Situation: {info['Situation']}")

    # Sort students by average grade in descending order
    sorted_students = sorted(all_students.items(), key=lambda item: item[1]["Average_Grade"], reverse=True)

    # Print sorted student names and their averages
    print("\n===== Students Ordered by Average Grade =====")
    for student_name, info in sorted_students:
        print(f"{student_name}: {info['Average_Grade']:.2f}")

if __name__ == "__main__":
    main()