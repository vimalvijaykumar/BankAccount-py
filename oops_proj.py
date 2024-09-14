class BalanceException(Exception):
    pass
class BankAccount:
    def __init__(self,initial_amount,acct_name):
        self.balance=initial_amount
        self.name=acct_name
        print(
            f"\nAccount {self.name} created.\nBalance =${self.balance}"
        )
    def check_balance(self):
        print(f"\nAccount {self.name} balance= ${self.balance:.2f}" )
    def deposit(self,deposit_amnt):
        self.balance+=deposit_amnt
        print("\nDeposit complete.")
        self.check_balance()
    def viable_transaction(self,amount):
        if self.balance>=amount:
            return
        else:
            raise BalanceException(
                f"\n sorry,account {self.name} only has a balance of ${self.balance:.2f}"
            )
    def withdraw(Self,amount):
       try:
           Self.viable_transaction(amount)
           Self.balance=Self.balance-amount
           print("\nWithdraw compleltee.")
           Self.check_balance()
       except BalanceException as error:
           print(f"\nwithdraw interrupted:{error}")

        
        