def sort_students(student_list):
    # Sort the list of students based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    
    return sorted_students

# Define the Student class
class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Example list of student objects
students = [
    Student("Alice", "A123", 3.8),
    Student("Bob", "B456", 3.6),
    Student("Charlie", "C789", 4.0),
    Student("David", "D567", 3.9)
]

# Call the function to sort students by CGPA
sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")