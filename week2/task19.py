pin = 1234
for i in range(3):
    user_input = int(input("Enter your PIN: "))
    if user_input == pin:
        print("\n 1Successfully logged in")
        break
    else:
        print("Incorrect PIN.\n Attempts left:" , 2-i)
else:
    print("Too many failed attempts. try again later.")