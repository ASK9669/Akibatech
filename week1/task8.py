student = input("Enter student name: ")
python_score = float(input("Enter Python score: "))
English_score = float(input("Enter English score: "))
math_score = float(input("Enter Math score: "))

average_score = (python_score + English_score + math_score) / 3

print("="*30)
print("        STUDENT RESULT   ")
print("="*30)
print()
print("Student:", student)
print()
print("Python Score:", python_score)
print("English Score:", English_score)
print("Math Score:", math_score)
print("---------------------")
print(f"Average:  {average_score:.2f}")
print("="*30)