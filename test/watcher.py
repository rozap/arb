import unittest
from settings import settings
from lib.watcher import Watcher

    
class TestWatcher(unittest.TestCase):

    def setUp(self):
        self.w = Watcher(settings)

    def test_load_exchanges(self):
        self.assertEqual(set(settings.exchanges), set(self.w.exchanges.keys()))

    def test_find_trade(self):
        self.w.find_trade()
