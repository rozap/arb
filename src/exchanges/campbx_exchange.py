from exchange import Exchange
from ..api.campbx import CampBX


class CampbxExchange(Exchange):

    def __init__(self, settings):
        super(CampbxExchange, self).__init__(settings)
        bx = settings['CAMPBX']
        self._trading = CampBX(bx['username'], bx['password'])


    '''
        How much can you buy a coin for, fee included for the exchange
    '''
    def _buy_price(self):
        tick = self._trading.xticker()
        base_price = float(tick['Best Ask'])
        fee = float(1) / 100
        return base_price + (fee * base_price)



    '''
        How much can you get if you sell a coin, fee subtracted
    '''
    def _sell_price(self):
        tick = self._trading.xticker()
        base_price = float(tick['Best Bid'])
        fee = float(1) / 100
        return base_price - (fee * base_price)
