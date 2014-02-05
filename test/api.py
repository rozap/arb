import unittest
from settings import settings
from lib.api.btce import BTCEClient

    
class TestBTCEClient(unittest.TestCase):

    def setUp(self):
        self.c = BTCEClient(settings.BTCE)

    def test_get_info(self):
        self.c.get_info()

    def test_get_prices(self):
        self.c.get_prices()