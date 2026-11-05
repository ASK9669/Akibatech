
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.__balance += amount
            print(f"{self.account_holder}, successfully deposited {amount} ETB.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"{self.account_holder}, successfully withdrew {amount} ETB.")

    def get_balance(self):
        print(f"{self.account_holder}, Balance: {self.__balance} ETB")


T1 = BankAccount("Abdi", 1000)
T2 = BankAccount("Bontu", 500)
T3 = BankAccount("Chala", 2000)

print("=" * 50)
print("Bank Transactions")
print("=" * 50)

T1.deposit(2000)
T2.withdraw(100)

T1.get_balance()
T2.get_balance()
T3.get_balance()

print("=" * 50)
