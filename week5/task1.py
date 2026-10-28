class Student:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Department: {self.department}")

student1 = Student("Awel", 20, "Software Engineering")
student2 = Student("Abdi", 22, "Computer Science")
student3 = Student("Milki", 18, "marketing")

student1.display_info()
student2.display_info()
student3.display_info()
