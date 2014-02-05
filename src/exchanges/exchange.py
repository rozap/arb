from ..util import Logger

class Exchange(object):

    def __init__(self, settings):
        self.L = Logger(settings)

    def buy_price(self):
        price = self._buy_price()
        self.L.log('%s buy price %s' % (self.__class__.__name__, price), 'info')
        return price

    def sell_price(self):
        price = self._sell_price()
        self.L.log('%s sell price %s' % (self.__class__.__name__, price), 'info')
        return price
