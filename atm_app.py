class ATM:
    def __init__(self,balance=1000):
        self.balance=balance
    def check_balance(self):
        return f"your account balance is ${self.balance}"
    def deposit(self,amount):
        self.balance+=amount
        return f"Deposited ${amount}.Your new balance is {self.balance}"
    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            return f"Withdraw  ${amount}.Your new balance is ${self.balance}"
        else: 
            return "Insufficient funds. Withdrawl failed"
atm=ATM()
while True:
    print("1.Check balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")
   
    choice=int(input("Enter your choice:"))
    
    if choice==1:
        print(atm.check_balance())
    elif choice==2:
        amount=float(input("Enter the deposit amount:"))
        print(atm.deposit(amount))
    elif choice==3:
        amount=float(input("Enter the withdrawl amount:"))
        print(atm.withdraw(amount))
    elif choice==4:
        print("Thank you for using the ATM.Have a nice day.Goodbye👋:)")
        break
    else:
        print("Invalid choice.Please select a valid option")