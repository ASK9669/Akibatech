

balance = int(input("Enter initial balance: "))
transactions = []


# Record a transaction
def record_transaction(transaction_type, amount, balance_after):
    transaction = {
        "type": transaction_type,
        "amount": amount,
        "balance_after": balance_after
    }

    transactions.append(transaction)


# Deposit money
def deposit(amount):
    global balance

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    balance += amount
    record_transaction("deposit", amount, balance)

    print("Deposit successful!")
    print("Current balance:", balance)


# Withdraw money
def withdraw(amount):
    global balance

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    if amount > balance:
        print("Insufficient balance.")
        return

    balance -= amount
    record_transaction("withdrawal", amount, balance)

    print("Withdrawal successful!")
    print("Current balance:", balance)


# Check current balance
def check_balance():
    print("Current balance:", balance)


# Generate transaction summary
def transaction_summary():
    total_deposited = 0
    total_withdrawn = 0

    print("\n===== TRANSACTION HISTORY =====")

    if len(transactions) == 0:
        print("No transactions yet.")

    for transaction in transactions:
        print(transaction)

        if transaction["type"] == "deposit":
            total_deposited += transaction["amount"]
        else:
            total_withdrawn += transaction["amount"]

    print("\nTotal deposited:", total_deposited)
    print("Total withdrawn:", total_withdrawn)
    print("Final balance:", balance)


while True:
    print("\n===== BANKING SYSTEM =====")
    print("1. Deposit money")
    print("2. Withdraw money")
    print("3. Check balance")
    print("4. Transaction summary")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        withdraw(amount)

    elif choice == "3":
        check_balance()

    elif choice == "4":
        transaction_summary()

    elif choice == "5":
        print("Thank you for using our banking system!")
        break

    else:
        print("Invalid choice. Please try again.")
