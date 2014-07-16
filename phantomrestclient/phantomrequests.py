__author__ = 'Davide Monfrecola'

import requests
from phantomrestclient import auth

class PhantomRequests():

    def __init__(self):
        self.auth = auth.PhantomAuth()
        self.access_token = self.auth.read_token()

    def get_all_domains(self):
        r = requests.get('https://phantom.nimbusproject.org/api/dev/domains',
                         headers={'Authorization': 'Basic %s' % self.access_token})
        return r.text

    def get_all_launchconfigurations(self):
        r = requests.get('https://phantom.nimbusproject.org/api/dev/launchconfigurations',
                         headers={'Authorization': 'Basic %s' % self.access_token})
        return r.text