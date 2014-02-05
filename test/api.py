from suite import ParametrizedTestCase
from src.api.btce import BTCEClient

    
class TestBTCEClient(ParametrizedTestCase):

    def setUp(self):
        self.c = BTCEClient(settings.BTCE)

    def test_get_info(self):
        self.c.get_info()

    def test_get_prices(self):
        self.c.get_prices()