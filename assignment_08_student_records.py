def display_menu():
    """
    Displays the main menu options to the user.
    """
    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU   ")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def calculate_average(scores):
    """
    Calculates and returns the average of a list of numeric scores.
    Returns 0.0 if the scores list is empty.
    """
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def add_student(students):
    """
    Prompts the user for student details (name, ID, scores)
    and appends a dictionary record to the students list.
    """
    name = input("Student name: ").strip()
    if not name:
        print("Error: Student name cannot be empty.")
        return

    try:
        student_id = input("Student ID: ").strip()
        
        # Check for unique student ID
        if any(s["id"] == student_id for s in students):
            print(f"Error: A student with ID '{student_id}' already exists.")
            return

        num_scores = int(input("How many scores? "))
        if num_scores < 0:
            print("Error: Number of scores cannot be negative.")
            return

        scores = []
        for i in range(1, num_scores + 1):
            while True:
                try:
                    score = float(input(f"Enter score {i}: "))
                    if 0 <= score <= 100:
                        scores.append(score)
                        break
                    else:
                        print("Please enter a score between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a valid number for score.")

        student_record = {
            "name": name,
            "id": student_id,
            "scores": scores
        }
        students.append(student_record)
        print(f'Student "{name}" added successfully.')

    except ValueError:
        print("Error: Invalid input. Please enter a valid integer for the count.")


def display_all_students(students):
    """
    Displays all student records in a formatted table layout.
    """
    if not students:
        print("\nNo student records found.")
        return

    print("\n" + "-" * 60)
    print(f"{'Name':<18} {'ID':<12} {'Scores':<18} {'Average':<8}")
    print("-" * 60)

    for student in students:
        scores_str = ", ".join(map(str, [int(s) if s.is_integer() else s for s in student["scores"]]))
        avg = calculate_average(student["scores"])
        print(f"{student['name']:<18} {student['id']:<12} {scores_str:<18} {avg:<8.2f}")

    print("-" * 60)


def calculate_student_average(students):
    """
    Finds a student by their ID and prints their average score.
    """
    if not students:
        print("\nNo student records available.")
        return

    target_id = input("Enter student ID: ").strip()

    for student in students:
        if student["id"] == target_id:
            avg = calculate_average(student["scores"])
            print(f"{student['name']}'s average score: {avg:.2f}")
            return

    print(f"Error: Student with ID '{target_id}' not found.")


def main():
    students = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            calculate_student_average(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()