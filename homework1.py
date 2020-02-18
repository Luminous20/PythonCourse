
# Homework by Clara Schlosser KU 0073323
# For INTL 308


import random #Import the package random to afterwards get
# a random value to define stock prices

market = {} # create list market (global variable )

class Portfolio(object): # defining what is a portfolio it is an object
    def __init__(self):
        self.cash = 0 # At the beginning there is no money in the portfolio
        self.stocklst = {} # list of the stocks
        self.fundlst = {} # list of the  funds
        self.historylst = ['new Portfolio'] # making a list to afterwards put in the history

    def addCash(self, value): # defining the addCash function:
        self.value = value #value = the amount added
        if (value < 0): # if function only positive amount can be added
            self.historylst.append("Warn - cash must be a positive value")
            return bool(False)
        self.cash = self.cash + value # adding the amount = the new cash amount
        self.historylst.append(str("{:.2f}".format(value)) + " cash added") # add the amount added to the history
        return bool(True)

    def withdrawCash(self, value): # define the Withdraw function:
        self.value = value #value = the amount were going to withdraw
        if (value < 0): # if function only positive amount can be withdrawn
            self.historylst.append("Warn - cash must be a positive value")
            return bool(False)
        if (self.cash < value): # puts out a waring if you going to withdraw cash so that you go in debt
            self.historylst.append("Warn - not enough money")
            return bool(False)
        self.cash = self.cash - value # withdraws the amount = the new cash amount
        self.historylst.append(str("{:.2f}".format(value)) + " cash withdrawn") # add the amount withdrawn to the history
        return bool(True)

    def buyStock(self, shares, symbol):# define the buyStock function
        self.shares = shares # define the shares
        self.symbol = symbol #define the symbols of the share
        price = market[symbol.symbol] # looks for the price in the marcet list for the specific symbol
        val = shares*price # the value is calculated by multiplying the amount of shares with the prices
        if self.cash < val: # puts out a waring if you going to withdraw cash so that you go in debt
           self.historylst.append("Warn - not enough money")
           return bool(False)
        self.historylst.append(str(shares) + " Stock "+str(self.symbol.symbol) +" purchased at " + str("{:.2f}".format(price)) + " per share")# adds the transaction to the history
        self.withdrawCash(val) # uses the withdraw function to withdraw the value

        if self.symbol.symbol in self.stocklst:# updates the stocks you have in the Portfolio
            self.stocklst[self.symbol.symbol] = self.symbol.symbol[self.symbol.symbol] + shares # applies if you have already shares from that firm
        else:
            self.stocklst[self.symbol.symbol] = shares #  applies if you have not already shares from that firm
        return bool(True)

    def sellStock(self, symbol, shares): # define the sellStock function
        self.shares = shares # define the shares
        self.symbol = symbol #define the symbols of the share
        fac = random.uniform(0.5, 1.5) #determines a random factor between (0.5, 1.5)
        price = market[symbol] # reads the price in the market list
        price = price * fac # determines the sell price by multiplying the share price with the factor
        price = round(price, 2) # rounds the price
        self.historylst.append(str(shares) + " Stock "+str(self.symbol) +" sold at " + str("{:.2f}".format(price)) + " per share") # adds the transaction to the history
        self.addCash(shares*price) # uses the addCash function to add the price times the amount of shares
        self.stocklst[self.symbol] = self.stocklst[self.symbol] - shares

    def buyMutualFund(self, shares, symbol): # define the buyMutualFundfunction
        self.shares = shares # define the shares
        self.symbol = symbol #define the symbols of the share
        price = 1 # price is set at 1
        val = shares*price # value is calculated shares times price
        if self.cash < val: #puts out a waring if you going to withdraw cash so that you go in debt
            self.historylst.append("Warn - not enough money")
            return bool(False)
        self.withdrawCash(shares*price) # uses the withdraw function to withdraw the price times the shares
        if self.symbol in self.fundlst: # updates the fundlist you have in the Portfolio
            self.fundlst[self.symbol] = self.fundlst[self.symbol] + shares
        else:
           self.fundlst[self.symbol.symbol] = shares
        self.historylst.append(str(shares) + " Mutual Fund " +str(self.symbol.symbol) + " purchased at " + str("{:.2f}".format(price)) + " per share") # adds the transaction to the history
        return bool(True)

    def sellMutualFund(self, symbol, shares): # define the buyStock function
        self.shares = shares  # define the shares
        self.symbol = symbol #define the symbols of the share
        price = round(random.uniform(0.9, 1.2),2) # determines a random price between (0.9, 1.2)and rounds
        self.addCash(shares*price)  # uses the addCash function to add the price times the amount of shares
        self.fundlst[symbol] = self.fundlst[symbol] - shares  # updates the fundlist you have in the Portfolio
        self.historylst.append(str(shares) + " Mutual Fund "+str(self.symbol) +" sold at " + str("{:.2f}".format(price)) + " per share")  # adds the transaction to the history


    def history(self): # define the history function
        print ("")
        print ("History")
        print(*self.historylst,sep="\n")

    def __str__(self): # printing the portfolio
        return str(self.print_portfolio())

    def print_portfolio(self): # defines the history function
        print("Portfolio")
        print("cash:  ",str("{:.2f}".format(self.cash)))
        print("stock: ",str(self.stocklst))
        print("nfund: ",str(self.fundlst))

class MutualFund(object): # defines the class Mutualfund
    def __init__(self, symbol):
        self.symbol = symbol

class Stock(object): # defines the class stock
    def __init__(self, price, symbol):
        self.symbol = symbol
        market[symbol] = price # Has a list in which the price is determined and specified by the symbol

if __name__ == '__main__': #Add this if you want to run the test with this script.
    portfolio = Portfolio()              # create a new portfolio
    portfolio.addCash(300.50)            # add cash to the portfolio
    s = Stock(price=20, symbol="HFH")    # create a stock HFH
    portfolio.buyStock(5, s)             # buy 5 shares of stock s
    mf1 = MutualFund("BRT")              # create MF BRT
    mf2 = MutualFund("GHT")              # create MF GHT
    portfolio.buyMutualFund(10.3, mf1)   # Buy 10.3 shares of BRT
    portfolio.buyMutualFund(2, mf2)      # Buy 2 shares of GHT
    portfolio.print_portfolio()          # print portfolio
    portfolio.sellMutualFund("BRT", 3)   # Sell 3 shares of BRT
    portfolio.sellStock("HFH", 1)        # Sell 1 share of HFH
    portfolio.withdrawCash(50)           # Withdraw 50
    portfolio.addCash(19.80)             #add cash  add cash to the portfolio
    portfolio.history()                  # Show a transaction history ordered by time
