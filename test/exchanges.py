from suite import ParametrizedTestCase
from src.exchanges import *


class ExchangeTest(ParametrizedTestCase):


    def test_buy_price(self):
        price = self.e.buy_price()
        self.assertTrue(price > 100)
        self.assertIsInstance(price, float)

    def test_sell_price(self):
        price = self.e.sell_price()
        self.assertTrue(price > 100)
        self.assertIsInstance(price, float)


class TestBitstamp(ExchangeTest):

    def setUp(self):
        self.e = BitstampExchange(self.settings)

    
class TestCoinbase(ExchangeTest):

    def setUp(self):
        self.e = CoinbaseExchange(self.settings)