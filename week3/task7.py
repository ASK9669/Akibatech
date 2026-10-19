
def check_minimum_length(password, min_length=8):
    return len(password) >= min_length


def check_uppercase(password):
    for char in password:
        if char.isupper():
            return True
    return False


def check_lowercase(password):
    for char in password:
        if char.islower():
            return True
    return False


def check_digit(password):
    for char in password:
        if char.isdigit():
            return True
    return False


def check_special_character(password):
    for char in password:
        if not char.isalnum() and not char.isspace():
            return True
    return False


def analyze_password(password, min_length=8):
    report = {
        "Minimum length": check_minimum_length(password, min_length),
        "Uppercase letter": check_uppercase(password),
        "Lowercase letter": check_lowercase(password),
        "Digit": check_digit(password),
        "Special character": check_special_character(password)
    }

    passed = []
    failed = []

    for requirement, result in report.items():
        if result:
            passed.append(requirement)
        else:
            failed.append(requirement)

    return {
        "password": password,
        "valid": len(failed) == 0,
        "passed": passed,
        "failed": failed,
        "requirements": report
    }


# Test five fictional passwords
test_passwords = [
    "Hello@123",
    "hello",
    "HELLOWORLD",
    "Abcdefg1",
    "Python@2026"
]

for password in test_passwords:
    result = analyze_password(password)

    print("\nPassword:", result["password"])
    print("Valid:", result["valid"])
    print("Passed:", result["passed"])
    print("Failed:", result["failed"])
