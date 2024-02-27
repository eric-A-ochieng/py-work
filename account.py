from datetime import datetime

class BankAccount:
    def __init__(self, account_number, balance, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = datetime.now()
        self.customer_name = customer_name

    def deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        self.balance += amount
        return amount

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        if amount > self.balance:
            
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount

    def check_balance(self):
        print("Current Balance:", self.balance)

    def customer_details(self):
        print("Customer Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of Opening:", self.date_of_opening)
        print("Balance:", self.balance)


account1 = BankAccount(account_number="223745690211", balance=950.00, customer_name="Eric Otieno")


deposited_amount = account1.deposit()
print("Amount Deposited:", deposited_amount)
account1.check_balance()


withdrawn_amount = account1.withdraw()
print("Amount Withdrawn:", withdrawn_amount)
account1.check_balance()


insufficient_balance = account1.withdraw()
print(insufficient_balance)


account1.customer_details()
