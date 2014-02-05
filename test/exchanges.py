import unittest
from settings import settings
from lib.exchanges import *


class ExchangeTest(object):

    def test_buy_price(self):
        price = self.e.buy_price()
        self.assertTrue(price > 100)
        self.assertIsInstance(price, float)

    def test_sell_price(self):
        price = self.e.sell_price()
        self.assertTrue(price > 100)
        self.assertIsInstance(price, float)


class TestBitstamp(unittest.TestCase, ExchangeTest):

    def setUp(self):
        self.e = BitstampExchange(settings)

    
class TestCoinbase(unittest.TestCase, ExchangeTest):

    def setUp(self):
        self.e = CoinbaseExchange(settings)