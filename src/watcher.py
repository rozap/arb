from util import Logger
import sys
import time
'''
    Watch the exchanges specified in settings and if a trade is possible, make it
'''
class Watcher(object):

    exchanges = {}

    def __init__(self, settings):
        self.set_settings(settings)
        self.L = Logger(settings)
        self.L.log('Setup watcher for %s' % (self.exchange_names), 'info')
        self.load_exchanges(settings)


    def set_settings(self, settings):
        self.trade_threshold = settings['trade_threshold']
        if self.trade_threshold <= 0:
            raise Error('settings variable trade_threshold must be above 0!')
        self.exchange_names = settings['exchanges']
        self.poll_interval = settings['poll_interval']



    def load_exchanges(self, settings):
        c_name = '%sExchange'

        modules = zip(self.exchange_names, [__import__('src.exchanges', fromlist=[str(c_name%e)]) for e in self.exchange_names])
        exchange_classes = [(e, getattr(module, c_name % e)) for e, module in modules]
        for name, klass in exchange_classes:
            self.exchanges[name] = klass(settings)
        
        self.L.log('Loaded exchanges %s' % self.exchanges, 'info')



    def find_trade(self):
        buys = [(name, exch.buy_price()) for name, exch in self.exchanges.iteritems()]
        sells = [(name, exch.sell_price()) for name, exch in self.exchanges.iteritems()]

        #find the minimum buy and the max sell price
        min_buy = min(buys, key = lambda x: x[1])
        max_sell = max(sells, key = lambda x : x[1])

        if max_sell[1] - min_buy[1] > self.trade_threshold:
            self.L.log('Possible Trade opportunity:', 'info')
            self.L.log('Buy from %s @ %s and sell to %s @ %s' % (min_buy + max_sell), 'info')
        else:
            self.L.log('No trading opportunity', 'info')
            self.L.log('Min buy from %s @ %s | Max sell to %s @ %s' % (min_buy + max_sell), 'info')

    def watch(self):
        while True:
            self.find_trade()
            time.sleep(self.poll_interval)
