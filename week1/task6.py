Employee_name = input("Enter your name: ")
Basic_salary = float(input("Enter your basic salary: "))
transport_allowance = float(input("Enter your transport allowance: "))
food_allowance = float(input("Enter your food allowance: "))

gross_salary = Basic_salary + transport_allowance + food_allowance

print("=" * 30)
print("   EMPLOYEE PAYSLIP    ")
print("=" * 30)
print(f"Employee: {Employee_name}")
print(f"\nBasic Salary:      {Basic_salary:.2f}ETB")
print(f"Transport Allowance:      {transport_allowance:.2f}ETB")
print(f"Food Allowance:      {food_allowance:.2f}ETB")
print(f"-" * 27)
print(f"\nAGross Salary:    {gross_salary:.2f}ETB")
print("=" * 30)