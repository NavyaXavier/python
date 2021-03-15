class BankAccount:
        def __init__(self):
            self.balance = 0
            print("hello welcome")
            self.name = input("enter your name: ")
            self.ac_no = input("enter your account number: ")
            self.type = input("enter your account type : ")
        def deposit(self):
            amount = float(input("enter the amount to be deposited : "))
            self.balance = self.balance + amount
            print("\n amount deposited :", amount)
        def withdraw(self):
            amount = float(input("enter amount to be withdrawn : "))
            if self.balance >= amount:
                self.balance = self.balance-amount
                print("\n you withdraw:", amount)
            else:
                print("insufficient balance")
        def display(self):
            print(self.name, "net available balance= ", self.balance)


s = BankAccount()

s.deposit()
s.withdraw()
s.display()





    

