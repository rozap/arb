from exchange import Exchange
from coinbase import CoinbaseAccount

class CoinbaseExchange(Exchange):

    def __init__(self, settings):
        super(CoinbaseExchange, self).__init__(settings)
        self._trading = CoinbaseAccount(api_key = settings['COINBASE']['api']['key'])


    '''
        How much can you buy a coin for, fee included for the exchange
    '''
    def _buy_price(self):
        price = self._trading.buy_price()
        return price



    '''
        How much can you get if you sell a coin, fee subtracted
    '''
    def _sell_price(self):
        price = self._trading.sell_price()
        return price


