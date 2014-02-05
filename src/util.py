

class Logger(object):

    __levels = {
        'debug' : 0, 
        'info' : 1,
        'warn' : 2,
        'error' : 3
    }

    def __init__(self, settings):
        self.log_level = self.__levels[settings['log_level']]


    def log(self, msg, level):
        if self.__levels[level] >= self.log_level:
            print msg
