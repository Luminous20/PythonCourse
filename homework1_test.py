import unittest
from homework1 import Portfolio
from homework1 import MutualFund
from homework1 import Stock
#import homework1

class Homework1Test(unittest.TestCase):

    def test_addCash(self):
        portfolio = Portfolio()
        portfolio.addCash(10)
        self.assertEqual(portfolio.cash, 10)

    def test_addCash_pos(self):
        portfolio = Portfolio()
        self.assertEqual(portfolio.addCash(10),True)

    def test_addCash_neg(self):
        portfolio = Portfolio()
        self.assertEqual(portfolio.addCash(-10),True)

    def test_withdrawCash(self):
        portfolio = Portfolio()
        portfolio.addCash(10)
        portfolio.withdrawCash(6)
        self.assertEqual(portfolio.cash, 4)

    def test_withdrawCash_neg(self):
        portfolio = Portfolio()
        portfolio.addCash(10)
        self.assertEqual(portfolio.withdrawCash(20),True)

    def test_buyStock(self):
        portfolio = Portfolio()
        portfolio.addCash(150)
        s = Stock(price=20, symbol="HFH")
        portfolio.buyStock(5, s)
        self.assertEqual(portfolio.cash, 50)

    def test_buyMutualFund(self):
        portfolio = Portfolio()
        portfolio.addCash(10)
        mf2 = MutualFund("GHT")              # create MF GHT
        portfolio.buyMutualFund(2, mf2)      # Buy 2 shares of GHT
        self.assertEqual(portfolio.cash, 8)


if __name__ == "__main__":
    unittest.main()
