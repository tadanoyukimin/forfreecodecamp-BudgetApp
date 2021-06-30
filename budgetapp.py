class Category:

    def __init__(self, category):
        self.category = category
        self.amount = 0
        self.ledger = []

    def deposit(self, amount, description = ''):
        self.amount += amount
        totaldeposit = self.amount
        self.ledger.append({'amount': self.amount,  'description': description})

    def withdraw(self, amount, description = ''):
        if not self.check_funds(amount):
            return False
        else:
            withdrawpercentage = amount // self.amount
            self.amount -= amount
            self.ledger.append({'amount':-amount, 'description': description})
            return True

    def get_balance(self):
        return self.amount

    def transfer(self, amount, transfercategory):
        if self.category != transfercategory.category:
            if not self.check_funds(amount):
                return False
            else:
                self.amount -= amount
                self.ledger.append({'amount': -amount, 'description': 'Transfer to ' + transfercategory.category})
                transfercategory.amount += amount
                transfercategory.ledger.append({'amount': transfercategory.amount, 'description': 'Transfer from ' + self.category})
                return True
        else:
            return False
    
    def check_funds(self, amount):
        if self.amount <= amount:
            return False
        else:
            return True

    def __repr__(self):
        header = f'{self.category:*^30}' + '\n'
        budgetoutput = ''
        totalbudget = 'Total: ' + f'{self.amount:.2f}'
        for i in range(len(self.ledger)):
            spaces = 29 - len(self.ledger[i]['description'][:23])
            amount = self.ledger[i]['amount']
            famount = f'{amount:>{spaces}.2f}'
            xdescription = self.ledger[i]['description'][:23]
            budgetoutput += xdescription + ' ' + famount + '\n'
        return str(header + budgetoutput + totalbudget)

food = Category ('Food')
clothing = Category('Clothing')
entertainment = Category('Entertainment')
food.deposit(500.24)
food.withdraw(223.44, 'a bunch of food 23 character test')
food.get_balance()
print(food.transfer(25.00, clothing))
food.check_funds(500)
print(food)
# def create_spend_chart(categories):
#     #categories include Food, Clothing and Entertainment
#     if categories:
#         for i in range(len(categories)):
#             categories[i] = Category(str(categories[i]))
#     categories[i].deposit(500.24)
#     print(categories[i])
# print(create_spend_chart(['Food', 'Clothing']))