class Atm(object):
    def __init__(self,cardNumber,pinNumber,nameOnCard):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber
        self.nameOnCard=nameOnCard
    def CashWithdrawl(self):
        print("with drawing cash")
    def BalanceEnquiry(self):
        print("***** is the amount in your account")

ATM=Atm("card number","pin number","nameOnCard")
print(ATM.cardNumber)
print(ATM.pinNumber)
print(ATM.nameOnCard)

ATM.CashWithdrawl()
ATM.BalanceEnquiry()


