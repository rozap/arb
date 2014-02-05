import argparse
import json
from src.watcher import Watcher


def load_settings(path):
    with open(path) as s:
        settings = json.loads(s.read())
        #Various libraries are complaining when passed unicode strings...so... {:(
        def to_string(o):
            if type(o) is dict:
                return {k : to_string(v) for k, v in o.iteritems()}
            elif type(o) is unicode:
                return str(o)
            return o

        return to_string(settings)

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--settings', help = 'path to the settings json file')
    return parser.parse_args()

def main():
    args = parse()
    settings = load_settings(args.settings)
    w = Watcher(settings)
    w.watch()




if __name__ == '__main__':
    main()