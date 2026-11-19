class Student:
    def __init__(self, name, student_id, course):
        self.name = name
        self.student_id = student_id
        self.course = course

    def display(self):
        print(f"ID: {self.student_id} | Name: {self.name} | Course: {self.course}")


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Student name: ").strip()
        student_id = input("Student ID: ").strip()
        course = input("Course: ").strip()
        self.students.append(Student(name, student_id, course))
        print("Student added.")

    def list_students(self):
        if not self.students:
            print("No records yet.")
            return
        for student in self.students:
            student.display()

    def search_student(self):
        student_id = input("Enter ID to search: ").strip()
        for student in self.students:
            if student.student_id == student_id:
                student.display()
                return
        print("Student not found.")


def main():
    manager = StudentManager()
    while True:
        print("\n1. Add student  2. List students  3. Search  4. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.list_students()
        elif choice == "3":
            manager.search_student()
        elif choice == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
