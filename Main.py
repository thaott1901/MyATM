import BankData

# Set up customer data and transaction:
cust1 = BankData.Customer("12345", "123")
cust1.createAccount("a1", 12)
cust1.createAccount("a2", 32)
cust2 = BankData.Customer("54321", "543")
cust2.createAccount("b1", 43)
cust2.createAccount("b2", 15)

cust1.getAccount("a1").depositCash(38)
cust2.getAccount("b2").depositCash(22)

cust1.getAccount("a2").withdrawCash(3)
cust2.getAccount("b2").withdrawCash(7)
# End set up customer


idValid = False
count = 0

flagCard = False
while not flagCard:
    print("Insert your card:")
    cardNum = input()
    if cardNum in BankData.getCustomerList():
        cust = BankData.getCustomer(cardNum)
        flagCard = True
    else:
        print("Invalid card")

accList = []
while not idValid:
    print("Input your pin number:")
    pinNum = input()
    if pinNum == cust.getPin():
        accList = cust.getAllAcounts()
        idValid = True

# print(accList)
print("Your list of current accounts:")
for acc in accList:
    print(acc.getAccId())

accIdValid = False
while not accIdValid:
    print("Please select the account you want to check:")
    accName = input()
    for acc in accList:
        if accName == acc.getAccId():
            print("Account id: ", acc.getAccId())
            print("Your account balance: ", acc.getBalance())
            print("Your deposit history: ", acc.getDeposit())
            print("Your withdraw history: ", acc.getWithdraw())
            accIdValid = True
