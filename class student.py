class Student:
    def __init__(self, name, student_id, major, gpa=0.0):
        self.name = name
        self.student_id = student_id
        self.major = major
        self.gpa = gpa

    def update_gpa(self, new_gpa):
        self.gpa = new_gpa

    def show_profile(self):
        print(f"Name: {self.name} | ID: {self.student_id} | Major: {self.major} | GPA: {self.gpa}")


# Create students
s1 = Student("Alice", "S001", "CS")
s2 = Student("Bob", "S002", "Math")
s3 = Student("Charlie", "S003", "Physics")
s4 = Student("Dani", "S004", "Biology")

# Update GPA
s1.update_gpa(3.8)
s2.update_gpa(3.5)
s3.update_gpa(3.9)
s4.update_gpa(3.2)

# Show profiles
s1.show_profile()
s2.show_profile()
s3.show_profile()
s4.show_profile()