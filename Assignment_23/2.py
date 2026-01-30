class BankAccount:
    ROI = 10.5

    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder's Name : ",self.Name)
        print("Current Balance : ",self.Amount)

    def Deposit(self):
        A =float(input("Enter deposit amount : "))
        self.Amount = self.Amount+A

    def Withdraw(self):
        A =float(input("Enter withdrawal aomunt : "))
        if (A <= self.Amount):
            self.Amount =self.Amount-A
        else:
            print("Insufficient balance")

    def CalculateInterest(self):
        print((self.Amount*BankAccount.ROI) / 100)


obj1 =BankAccount("Amar : ", 5000)

obj1.Display()
obj1.Deposit()
obj1.Withdraw()
print("Total Interest : ",obj1.CalculateInterest())

print("-"*40)

obj2 =BankAccount("Pruthvi : ", 10000)

obj2.Display()
obj2.Deposit()
obj2.Withdraw()
print("Total Interest : ",obj2.CalculateInterest())
