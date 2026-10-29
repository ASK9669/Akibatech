class Student:
    school_name = "Akiba Academy"
    def __init__(self, name, score,department):
        self.name = name
        self.score = score
        self.department = department

    def Display(self):
        print(f"Name: {self.name}, Score: {self.score}, Department: {self.department}, School: {Student.school_name}")

s1 = Student("Awel", 90, "Mathematics")
s2 = Student("Abdi", 85, "Physics")
s3 = Student("chala", 95, "Chemistry")

print("====================================")
s1.Display()
s2.Display()
s3.Display()
print("\n-------------updated-------------\n")

s1.score = 95
s1.Display()
print("\n====================================\n")