__author__ = 'Davide Monfrecola'

import sys
try:
    import configparser     # Python 3.x
except ImportError:
    import ConfigParser     # Python 2.x


class PhantomAuth():

    def __init__(self):
        self.access_token = None

    def read_token_from_file(self):
        if sys.version_info >= (3, 0):
            self.parser = configparser.ConfigParser()
        if sys.version_info < (3, 0):
            self.parser = ConfigParser.SafeConfigParser()
        self.parser.read('phantomrestclient/conf/auth.txt')
        return self.parser.get('phantom', 'access_token')

class TokenRequest():

    def __init__(self):
        pass