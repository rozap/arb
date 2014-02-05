from exchange import Exchange
from ..api.btce import BTCEClient

class BTCEExchange(Exchange):

    def __init__(self, settings):
        super(BTCEExchange, self).__init__(settings)
        self._trading = BTCEClient(settings['BTCE'])


    '''
        How much can you buy a coin for, fee included for the exchange
    '''
    def _buy_price(self):
        prices = self._trading.get_prices()
        fees = self._trading.get_fees()
        base_sell = prices['ticker']['buy']
        fee = float(fees['trade'])
        return base_sell + ((fee / 100) * base_sell)



    '''
        How much can you get if you sell a coin, fee subtracted
    '''
    def _sell_price(self):
        prices = self._trading.get_prices()
        fees = self._trading.get_fees()
        base_sell = prices['ticker']['sell']
        fee = float(fees['trade'])
        return base_sell - ((fee / 100) * base_sell)


