arb
===

btc arbitrage



#### tests
python -m test.test --settings /path/to/your/settings_file.json

#### settings

```javascript
{
	"COINBASE": {
		"api": {
			"key": "<your coinbase api key>"
		}
	},


	"BTCE": {
		"api": {
			"key": "<btce key>",
			"secret": "<btce secret>"
		}
	},


	"BITSTAMP": {
		"api": {
			"key": "<bitstamp key",
			"secret": "<bitstamp secret>"
		},
		"username": "<user id>"
	},


	"log_level": "info",
	//how many dollars in price difference is an acceptable trade
	"trade_threshold": 1,
	//how often to check exchanges (seconds)
	"poll_interval": 10,
	//the exchanges you want to load
	"exchanges": ["Coinbase", "Bitstamp", "BTCE"]
}
