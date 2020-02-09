
class Portfolio():
    def __init__(self):
        self.cash=0
        self.stock={}
        self.mutual_funds={}
        self.transactions=[]
    def __str__(self):
        return ("cash: "+self.cash+ '\nstock: '+{key:value for (key,value) in self.stock.items()}+'\nmutual funds: '+ {key:value for (key,value) in self.mutual_funds.items()})
    def addCash(self,amount):
        self.cash+=amount
        self.transactions.append(str(amount)+'$ cash added')
    def withdrawCash(self,amount):
        self.cash-=amount
        self.transactions.append(amount+'$ cash withdrew')

    def buyStock(self,shares,symbol):
        if symbol in self.stock.keys():
            self.stock[symbol]+=shares
        else:
            self.stock[symbol]=shares

    def buyMutualFund(self,shares,symbol):
        if symbol in self.mutual_funds.keys():
            self.mutual_funds[symbol]+=shares
        else:
            self.mutual_funds[symbol]=shares

    def sellMutualFund(self,shares,symbol):
        if symbol in self.mutual_funds.keys():
            self.mutual_funds[symbol]-=shares
        else:
            self.mutual_funds[symbol]=shares

    def history(self):
        print(self.transactions)


class Stock():
    def __init__(self,price,symbol):
        self.price=price
        self.symbol=symbol

class MutualFund():
    def __init__(self,symbol):
        self.symbol=symbol
