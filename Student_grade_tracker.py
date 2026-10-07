import json


class StudentGradeTracker:
    def __init__(self):
        self.students = {}
        self.results = {}

    def add_student(self):
        try:
            num_students = int(input("Enter number of students: "))

            if num_students <= 0:
                print("Number of students must be greater than 0.")
                return

        except ValueError:
            print("Please enter a valid number.")
            return

        for _ in range(num_students):
            student_id = input("Enter student ID: ").strip()

            if student_id in self.students:
                print("Student ID already exists.")
                continue

            name = input("Enter student name: ").strip()

            if not name:
                print("Name cannot be empty.")
                continue

            try:
                num_subjects = int(input("Enter number of subjects: "))

                if num_subjects <= 0:
                    print("Number of subjects must be greater than 0.")
                    continue

            except ValueError:
                print("Please enter a valid number.")
                continue

            subjects = {}

            for _ in range(num_subjects):
                subject = input("Enter subject name: ").strip()

                while True:
                    try:
                        marks = int(input(f"Enter marks for {subject}: "))

                        if 0 <= marks <= 100:
                            break

                        print("Marks must be between 0 and 100.")

                    except ValueError:
                        print("Please enter a valid number.")

                subjects[subject] = marks

            self.students[student_id] = {
                "name": name,
                "subjects": subjects
            }

            print(f"{name} added successfully.")


    def calculate_results(self):
        self.results = {}

        for student_id, student_data in self.students.items():

            name = student_data["name"]
            subjects = student_data["subjects"]

            marks = list(subjects.values())

            average = sum(marks) / len(marks)
            highest = max(marks)
            lowest = min(marks)

            if average >= 90:
                grade = "A"
            elif average >= 70:
                grade = "B"
            elif average >= 50:
                grade = "C"
            else:
                grade = "F"

            self.results[student_id] = {
                "name": name,
                "subjects": subjects,
                "average": round(average, 2),
                "highest": highest,
                "lowest": lowest,
                "grade": grade
            }


    def view_results(self):

        if not self.results:
            print("No results available. Calculate results first.")
            return

        for student_id, result in self.results.items():

            print("\n-------------------------")
            print(f"Student ID : {student_id}")
            print(f"Name       : {result['name']}")

            print("Subjects:")

            for subject, marks in result["subjects"].items():
                print(f"  {subject}: {marks}")

            print(f"Average    : {result['average']}")
            print(f"Highest    : {result['highest']}")
            print(f"Lowest     : {result['lowest']}")
            print(f"Grade      : {result['grade']}")


    def search_student(self):

        student_id = input("Enter student ID: ").strip()

        if student_id not in self.results:
            print("Student not found.")
            return

        result = self.results[student_id]

        print("\nStudent Details")
        print("-------------------------")
        print(f"ID      : {student_id}")
        print(f"Name    : {result['name']}")

        for subject, marks in result["subjects"].items():
            print(f"{subject}: {marks}")

        print(f"Average : {result['average']}")
        print(f"Grade   : {result['grade']}")


    def save_to_json(self):

        if not self.results:
            print("Calculate results before saving.")
            return

        with open("students.json", "w") as file:
            json.dump(self.results, file, indent=4)

        print("Results saved to students.json")


    def menu(self):

        while True:

            print("\n===== STUDENT GRADE TRACKER =====")
            print("1. Add Students")
            print("2. Calculate Results")
            print("3. View Results")
            print("4. Search Student")
            print("5. Save Results")
            print("6. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.add_student()

            elif choice == "2":
                self.calculate_results()
                print("Results calculated successfully.")

            elif choice == "3":
                self.view_results()

            elif choice == "4":
                self.search_student()

            elif choice == "5":
                self.save_to_json()

            elif choice == "6":
                print("Thank you for using Student Grade Tracker.")
                break

            else:
                print("Invalid choice. Please try again.")


tracker = StudentGradeTracker()
tracker.menu()