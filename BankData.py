customerList = {}


def getCustomer(cardId):
    if cardId in customerList:
        return customerList.get(cardId)

def getCustomerList():
    return customerList

class Customer:
    def __init__(self, cardID, pin):
        self.cardID = cardID
        self.pin = pin
        self.account = {}
        customerList[cardID] = self

    def createAccount(self, accId, amt):
        acc = Account(accId, amt)
        self.account[accId] = acc

    def getAccount(self, accId):
        return self.account.get(accId)

    def getAllAcounts(self):
        return self.account.values()


    def pinValid(self, input):
        return input == self.pin

    def getCardId(self):
        return self.cardID

    def getPin(self):
        return self.pin

class Account:
    def __init__(self, accId, amt):
        self.accId = accId
        self.balance = amt
        self.deposit = {}
        self.withdraw = {}
        self.timeSeed = 0

    def depositCash(self, amount):
        if amount > 0:
            self.balance += amount
            self.deposit[self.timeSeed] = amount
            self.timeSeed += 1

    def withdrawCash(self, amount):
        if amount > 0:
            self.balance -= amount
            self.withdraw[self.timeSeed] = amount
            self.timeSeed += 1

    def getBalance(self):
        return self.balance

    def getDeposit(self):
        return self.deposit

    def getWithdraw(self):
        return self.withdraw

    def getAccId(self):
        return self.accId



# p1 = Customer("12345", "123")
# p2 = Customer("54321", "543")
# print(p1)
# input = "1234"
# print(p1.pinValid(input))
#
# print("Balance:", p1.balance)
# print("Deposit:", p1.deposit)
# print("Withdraw:", p1.withdraw)
# print("-----------------------")
# p1.depositCash(100)
# print("Balance:", p1.balance)
# print("Deposit:", p1.deposit)
# print("Withdraw:", p1.withdraw)
# print("-----------------------")
# p1.withdrawCash(17)
# print("Balance:", p1.balance)
# print("Deposit:", p1.deposit)
# print("Withdraw:", p1.withdraw)

# print(customerList)
# person1 = customerList.get(p1.cardID)
# print(person1.pinValid("1234"))
