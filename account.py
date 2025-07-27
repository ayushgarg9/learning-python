class account():
    def __init__(self,bal,acc):
        self.bal = bal
        self.acc = acc

    def debit(self,amt):
        self.bal -= amt
        print("rs.", amt, "is debited")
        print("remaing balance is: ",self.print_bal())

    def credit(self,amt):
        self.bal += amt
        print("rs.", amt, "is credited")
        print("remaing balance is: ",self.print_bal())

    def print_bal(self):
        return self.bal


acc1 = account(10000,972007)
acc1.acc = int(input("enter account number: "))
print("your account number is: ",acc1.acc)
acc1.debit(int(input("enter amount: ")))
acc1.credit(int(input("enter amount: ")))
