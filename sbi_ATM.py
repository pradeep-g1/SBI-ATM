#let us assume some random persons data which is given backend like database
data={6303464362:'pradeep',8106402639:'Dinesh',8639162700:'Rajesh',7981656026:'Naveen_basha',9398553385:'sreekanth'}
data_balance={6303464362:50000002364.0,8639162700:696969.0,8106402639:856749.0,7981656026:10.0,9398553385:12.0}
pin={6303464362:4362,8639162700:2700,8106402639:2639,7981656026:6026,9398553385:5335}
print("welcome to State Bank of India","\N{grinning face}")

class ATM:
    #function for depositing amount into acccount
    def cashdeposit(self,amount,account_number,data_balan):
        self.amount=amount
        self.data_balan=data_balan
        self.account_number=account_number
        self.a=self.data_balan[self.account_number]
        self.data_balan[self.account_number]=self.a+self.amount
        return self.data_balan
    #function for withdraw the amount from account
    def cash_withdrawl(self,amount,account_number,data_balan):
        self.amount=amount
        self.data_balan=data_balan
        self.account_number=account_number
        self.a=self.data_balan[self.account_number]
        self.data_balan[self.account_number]=self.a-self.amount
        return self.data_balan
    #function for pin generation/Pin change
    def change_pin(self,account_number,pin):
        self.pin=pin
        self.account_number=int(input("enter the pin :"))
        if self.account_number in self.pin.values():
            self.a=int(input("enter the new pin:"))
            self.pin[account_number]=self.a
            print("PIN is changed successfully")
            return self.pin
        else:
            print("Match not found!\nENTER valid accountnumber")
     #function for balance enquiry
    def balance_enquiry(self,account_number,data_balan):
        self.account_number=account_number
        self.data_balan=data_balan
        return self.data_balan[account_number]
acc_number=int(input("enter the account number :"))
a=data[acc_number]
print(f'WELCOM To SBI {a}')
if acc_number in data.keys():
    print("great joy")
    print(" 0 cash deposit:\n","1 cash withdrawl:\n","2 balance enquiry:\n","3 Change the pin :\n")
else:
    print("the account number is invalid")
SBI=ATM()
operation_num=int(input("enter the operation number:"))
if(operation_num==0):
    print("cash deposit:")
    pin_number=int(input("enter the pin number :"))
    if pin[acc_number]==pin_number: 
        amount=int(input("enter the amount to be dopsited :"))            
        data_balance=SBI.cashdeposit(amount,acc_number,data_balance)
        print("Resultant balance is",data_balance[acc_number])
        print("Cash is deposited successfully\n","Thank you","\N{grinning face}","\N{grinning face}")
    else:
        print("PIN is invalid:")
elif(operation_num==1):
    print("cash withdrawl")
    pin_number=int(input("enter the pin number :"))
    if pin[acc_number]==pin_number:
        amount=int(input("enter the amount to be drawn :"))
        if(amount<=data_balance[acc_number]):
            data_balance=SBI.cash_withdrawl(amount,acc_number,data_balance)
            print("Transaction is under process! Please wait")
            print("Transaction is successful\n","Thank you\n","\N{grinning face}")
            print("Resultant balance is",data_balance[acc_number])
        else:
            print("Balance is not sufficient\n","Sorry\n")
    else:
        print("PIN is Invalid")
elif(operation_num==2):
    print("balance enquiry :\n")
    pin_number=int(input("enter the pin number :"))
    if pin[acc_number]==pin_number:
        print(SBI.balance_enquiry(acc_number,data_balance))
        print("Thank You","\N{grinning face}","\N{grinning face}","\N{grinning face}")
    else:
        print("PIN is invalid")
elif(operation_num==3):
    print("change the pin :")
    pin=SBI.change_pin(acc_number,pin)
else:
    print("Choose the valid option:")
