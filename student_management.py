import json
import os

FILE_NAME = "students.json"


def load_students():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []
    return []


def save_students(students):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    roll_no = input("Enter Roll Number: ").strip()

    if any(s["roll_no"] == roll_no for s in students):
        print("Roll number already exists!")
        return

    name = input("Enter Student Name: ").strip()
    course = input("Enter Course: ").strip()

    try:
        marks = float(input("Enter Marks: "))
        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return
    except ValueError:
        print("Please enter valid marks.")
        return

    student = {
        "roll_no": roll_no,
        "name": name,
        "course": course,
        "marks": marks
    }

    students.append(student)
    save_students(students)
    print("Student added successfully!")


def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
    for student in students:
        print(f"Roll No: {student['roll_no']}")
        print(f"Name: {student['name']}")
        print(f"Course: {student['course']}")
        print(f"Marks: {student['marks']}")
        print("-" * 25)


def search_student(students):
    roll_no = input("Enter Roll Number to search: ").strip()

    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent Found!")
            print(f"Roll No: {student['roll_no']}")
            print(f"Name: {student['name']}")
            print(f"Course: {student['course']}")
            print(f"Marks: {student['marks']}")
            return

    print("Student not found.")


def update_student(students):
    roll_no = input("Enter Roll Number to update: ").strip()

    for student in students:
        if student["roll_no"] == roll_no:
            name = input("Enter new name (press Enter to keep current): ")
            course = input("Enter new course (press Enter to keep current): ")
            marks_input = input("Enter new marks (press Enter to keep current): ")

            if name.strip():
                student["name"] = name.strip()

            if course.strip():
                student["course"] = course.strip()

            if marks_input.strip():
                try:
                    marks = float(marks_input)
                    if not 0 <= marks <= 100:
                        print("Marks must be between 0 and 100.")
                        return
                    student["marks"] = marks
                except ValueError:
                    print("Invalid marks.")
                    return

            save_students(students)
            print("Student updated successfully!")
            return

    print("Student not found.")


def delete_student(students):
    roll_no = input("Enter Roll Number to delete: ").strip()

    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            return

    print("Student not found.")


def main():
    students = load_students()

    while True:
        print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please select 1-6.")


if __name__ == "__main__":
    main()
