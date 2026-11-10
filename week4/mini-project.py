Orginal_marks = [85, 92, 78, 96, 88]
Shared_marks = Orginal_marks
Copied_marks = Orginal_marks.copy()

Copied_marks.append(100)
print("="*30)
print("Original marks:", Orginal_marks)
print("Shared marks:", Shared_marks)
print("Copied marks:", Copied_marks)
print("-"*30)
print(Orginal_marks is Shared_marks)
print(Orginal_marks is Copied_marks)
print(Shared_marks is Copied_marks)
print("-"*30)
print(Orginal_marks == Shared_marks)
print(Orginal_marks == Copied_marks)
print(Shared_marks == Copied_marks)
print("="*30)