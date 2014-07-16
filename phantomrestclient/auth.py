__author__ = 'Davide Monfrecola'

import ConfigParser

class PhantomAuth():

    def __init__(self):
        self.parser = ConfigParser.SafeConfigParser()
        self.parser.read('phantomrestclient/conf/auth.txt')
        self.access_token = None

    def read_token(self):
        return self.parser.get('phantom', 'access_token')

class TokenRequest():

    def __init__(self):
        pass