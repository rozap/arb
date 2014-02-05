from suite import ParametrizedTestCase
from src.watcher import Watcher
from main import load_settings
    
class TestWatcher(ParametrizedTestCase):

    def setUp(self):
        self.w = Watcher(self.settings)

    def test_load_exchanges(self):
        self.assertEqual(set(self.settings['exchanges']), set(self.w.exchanges.keys()))

    def test_find_trade(self):
        self.w.find_trade()
