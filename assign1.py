from random import uniform

class Stock():
    def __init__(self,price,symbol):
        self.price=price
        self.symbol=symbol

class MutualFund():
    def __init__(self,symbol):
        self.symbol=symbol

class Portfolio():

    def __init__(self):
        self.cash=0
        self.stocks={}
        self.mutual_funds={}
        self.transactions=[]

    def __str__(self):
        x= "cash: $"+str(self.cash)+'\n'
        x+='stocks: '
        if len(list(self.stocks.keys()))>0:
            for key in self.stocks.keys():
                x+=str(key.symbol)+' '+str(self.stocks[key])+'\n'
        if len(list(self.mutual_funds.keys()))>0:
            for key in self.mutual_funds.keys():
                x+=str(key.symbol)+' '+str(self.mutual_funds[key])+'\n'
        return x

    def addCash(self,amount):
        self.cash+=amount
        self.transactions.append(str(amount)+'$ cash added')

    def withdrawCash(self,amount):
        self.cash-=amount
        self.transactions.append(str(amount)+'$ cash withdrew')

    def buyStock(self,amount_shares,stock):
        self.cash-=amount_shares*stock.price
        if stock.symbol in self.stocks.keys():
            self.stocks[stock]+=amount_shares
        else:
            self.stocks[stock]=amount_shares
        self.transactions.append(str(amount_shares) + " " + stock.symbol + " stock bought for $ " + str(amount_shares * stock.price))

    def buyMutualFund(self,amount_shares,mutual_fund):
        self.cash-=amount_shares
        if mutual_fund.symbol in self.mutual_funds.keys():
            self.mutual_funds[mutual_fund]+=amount_shares
        else:
            self.mutual_funds[mutual_fund]=amount_shares
        self.transactions.append(str(amount_shares) + " " + mutual_fund.symbol + " mutual fund bought for $" + str(amount_shares))

    def sellStock(self,symbol,amount_shares):
        for stock in self.stocks.keys():
            if stock.symbol == symbol:
                self.stocks[stock]-=amount_shares
                sales_price=amount_shares*uniform(0.5*stock.price,1.5*stock.price)
                self.cash+=sales_price
                break

        self.transactions.append(str(amount_shares) + " " + stock.symbol + " stock sold for $" + str(sales_price))


    def sellMutualFund(self,symbol,amount_shares):
        for mutual_fund in self.mutual_funds.keys():
            if mutual_fund.symbol == symbol:
                self.mutual_funds[mutual_fund]-=amount_shares
                break
        sales_price=amount_shares*uniform(0.9,1.2)
        self.cash+=sales_price
        self.transactions.append(str(amount_shares) + " " + symbol + " mutual fund sold for $" + str(sales_price))

    def history(self):
        for x in self.transactions:
            print(x)
