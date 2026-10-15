
students = [
    {"name": "Sara", "score": 85},
    {"name": "Ahmed", "score": 42},
    {"name": "Musa", "score": 93},
    {"name": "Hana", "score": 67}
]


# 1. Validate a student's score
def validate_score(score):
    return 0 <= score <= 100


# 2. Calculate a grade
def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# 3. Calculate the average score
def calculate_average(students):
    total = 0
    count = 0

    for student in students:
        total += student["score"]
        count += 1

    if count == 0:
        return 0

    return total / count


# 4. Find highest and lowest scores
def find_highest_lowest(students):
    if len(students) == 0:
        return None, None

    highest = students[0]["score"]
    lowest = students[0]["score"]

    for student in students:
        score = student["score"]

        if score > highest:
            highest = score

        if score < lowest:
            lowest = score

    return highest, lowest


# 5. Count passed and failed students
def count_passed_failed(students):
    passed = 0
    failed = 0

    for student in students:
        if student["score"] >= 50:
            passed += 1
        else:
            failed += 1

    return passed, failed


# 6. Find students above the class average
def above_average_students(students):
    average = calculate_average(students)
    result = []

    for student in students:
        if student["score"] > average:
            result.append(student["name"])

    return result


# 7. Generate the class report
def generate_report(students):
    valid_students = []

    for student in students:
        if validate_score(student["score"]):
            valid_students.append(student)
        else:
            print("Invalid score for", student["name"])

    if len(valid_students) == 0:
        print("No valid student scores.")
        return

    average = calculate_average(valid_students)
    highest, lowest = find_highest_lowest(valid_students)
    passed, failed = count_passed_failed(valid_students)

    print("\n===== STUDENT PERFORMANCE REPORT =====")

    for student in valid_students:
        name = student["name"]
        score = student["score"]
        grade = calculate_grade(score)

        status = "Pass" if score >= 50 else "Fail"

        print(
            name,
            "| Score:", score,
            "| Grade:", grade,
            "| Status:", status
        )

    print("\nClass average:", round(average, 2))
    print("Highest score:", highest)
    print("Lowest score:", lowest)
    print("Passed students:", passed)
    print("Failed students:", failed)
    print("Above-average students:", above_average_students(valid_students))


generate_report(students)


