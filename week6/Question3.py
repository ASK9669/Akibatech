# inheritance and method overriding
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary} ETB")

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        print(f"Manager Name: {self.name}, Salary: {self.salary} ETB, Department: {self.department}")
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_info(self):
        print(f"Developer Name: {self.name}, Salary: {self.salary} ETB, Programming Language: {self.programming_language}")
O1 = Employee("Abdi", 1000)
O2 = Manager("Bontu", 2000, "IT")
O3 = Developer("Chala", 1500, "Python")

print("=" * 50)
print("Information")
print("=" * 50)
O1.display_info()
O2.display_info()
O3.display_info()
print("=" * 50)