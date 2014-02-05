from exchange import Exchange
from bitstamp.client import Trading as TradingClient
from bitstamp.client import Public as PublicClient


class BitstampExchange(Exchange):

    def __init__(self, settings):
        super(BitstampExchange, self).__init__(settings)
        bs = settings['BITSTAMP']
        self._trading = TradingClient(
            username = bs['username'],
            key = bs['api']['key'],
            secret = bs['api']['secret'])

        self._public = PublicClient()


    '''
        How much can you buy a coin for, fee included for the exchange
    '''
    def _buy_price(self):
        ticker = self._public.ticker()
        balance = self._trading.account_balance()
        return float(ticker['ask']) + float(balance['fee'])



    '''
        How much can you get if you sell a coin, fee subtracted
    '''
    def _sell_price(self):
        ticker = self._public.ticker()
        balance = self._trading.account_balance()
        return float(ticker['bid']) - float(balance['fee'])

