class Student:
    def __init__(self, name, student_id, department):
        self.name = name
        self.student_id = student_id
        self.department = department
    def display_info(self):
            print(f"Name: {self.name}, Student ID: {self.student_id}, Department: {self.department}")
    def introduce(self):
        print(f"Hello, my name is {self.name}. I am a student in the {self.department} department.")
s1 = Student("Abdi", "001", "Computer Science")
s2 = Student("Aisha", "002", "Mathematics")
s3= Student("Ali", "003", "Physics")
print("\nStudent Information:\n")
s1.display_info()
s2.display_info()
s3.display_info()
print()
s1.introduce()
s2.introduce()
s3.introduce()