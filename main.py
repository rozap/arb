import argparse
import json
from lib.watcher import Watcher



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--settings', help = 'path to the settings json file', default = 'arb_settings.json')

    args = parser.parse_args()


    with open(args.settings) as s:
        settings = json.loads(s.read())

        #Various libraries are complaining when passed unicode strings...so... {:(
        def to_string(o):
        	if type(o) is dict:
        		return {k : to_string(v) for k, v in o.iteritems()}
        	elif type(o) is unicode:
        		return str(o)
        	return o

        settings = to_string(settings)
        w = Watcher(settings)
        w.watch()




if __name__ == '__main__':
    main()