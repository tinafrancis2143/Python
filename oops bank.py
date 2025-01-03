class Bank:
    def __init__(self,acc_no,name,balance=0,acc_type="Savings"):
        self.acc_no=acc_no
        self.name=name
        self.acc_type=acc_type
        self.balance=balance
    def checkbalance(self):
        print(f"Your account balance is: {self.balance}")
    def withdraw(self,withdraw_amount):
        if withdraw_amount>self.balance:
            print("Insufficient Balance")
        else:
            print(f"{withdraw_amount} is debitted")
            self.balance=self.balance-withdraw_amount
            print(f"Your current balance is: {self.balance}")
    def deposit(self,deposit_amount):
        self.balance+=deposit_amount
        print(f"Amount deposited:{deposit_amount}")
        print(f"Your current balance is: {self.balance}")
    def AccountStatus(self):
        print(f"Name of account holder: {self.name}")
        print(f"Account Number: {self.acc_no}")
        print(f"Account Type: {self.acc_type}")

tiranavind=Bank(88480,"tiranavind",5000000000)

while(1):
    choice=int(input("Enter a choice\n1.Check Balance\n2.Withdrawal\n3.Deposit Amount\n4.Account Status\n"))
    if choice==1:
        tiranavind.checkbalance()
    elif choice==2:
        withdrawal_amount=int(input("Enter the amount you want to withdraw: "))
        tiranavind.withdraw(withdrawal_amount)
       
    elif choice==3:
        deposit_amount=int(input("enter the amount you want to deposit: "))
        tiranavind.deposit(deposit_amount)
        
    elif choice==4:
        tiranavind.AccountStatus()
        
    
        
        
    
