import httplib
import urllib
import json
import hashlib
import hmac
import time
import requests



class BTCEClient(object):

    base_url = 'https://www.btc-e.com/'

    def __init__(self, btce_settings):
        self.btce_settings = btce_settings


    def r(self, method, *args, **kwargs):
        nonce = int(time.time())
        # method name and nonce go into the POST parameters
        params = {"method":method,
                  "nonce": nonce}
        params = urllib.urlencode(params)
         
        # Hash the params string to produce the Sign header value
        H = hmac.new(self.btce_settings['api']['secret'], digestmod=hashlib.sha512)
        H.update(params)
        sign = H.hexdigest()
         
        headers = {"Content-type": "application/x-www-form-urlencoded",
                           "Key":self.btce_settings['api']['key'],
                           "Sign":sign}
        return requests.post('%stapi' % self.base_url, data = params, headers = headers).json()



    def p(self, uri, *args, **kwargs):
        return requests.get('%s%s'%(self.base_url, uri)).json()

    def get_info(self):
        return self.r('getInfo')
 
    def get_fees(self):
        return self.p('api/2/btc_usd/fee')

    def get_prices(self):
        return self.p('api/2/btc_usd/ticker')
