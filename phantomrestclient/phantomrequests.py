__author__ = 'Davide Monfrecola'

import requests
import json
from phantomrestclient import auth

class PhantomRequests():

    def __init__(self):
        self.auth = auth.PhantomAuth()
        self.api_url = 'https://phantom.nimbusproject.org/api/dev'
        self.access_token = self.auth.read_token_from_file()

    def get_request(self, entity, id=""):
        if id is not "":
            url = "%s/%s/%s" % (self.api_url, entity, id)
        else:
            url = "%s/%s" % (self.api_url, entity)
        r = requests.get(url,
                         headers={'Authorization': 'Basic %s' % self.access_token})

        if r.status_code == requests.codes.ok:
            return r.text
        else:
            r.raise_for_status()

    def post_request(self, entity, data):
        r = requests.post("%s/%s" % (self.api_url, entity), data=json.dumps(data),
                          headers={'Authorization': 'Basic %s' % self.access_token})

        if r.status_code == requests.codes.ok:
            return r.text
        else:
            r.raise_for_status()

    def put_request(self, entity, id, data):
        r = requests.put("%s/%s/%s" % (self.api_url, entity, id), data=json.dumps(data),
                          headers={'Authorization': 'Basic %s' % self.access_token})

        if r.status_code == requests.codes.ok:
            return r.text
        else:
            r.raise_for_status()

    def delete_request(self, entity, id):
        r = requests.delete("%s/%s/%s" % (self.api_url, entity, id),
                          headers={'Authorization': 'Basic %s' % self.access_token})

        if r.status_code == requests.codes.ok:
            return r.text
        else:
            r.raise_for_status()

    def get_all_domains(self):
        return self.get_request('domains')

    def get_all_launchconfigurations(self):
        return self.get_request('launchconfigurations')

    def get_all_sites(self, details=True):
        entity = 'sites'
        if details is True:
            entity + '?details=true'
        return self.get_request(entity=entity)

    def get_credentials(self, cloud_name):
        return self.get_request('credentials/sites/' + cloud_name)

    def create_lc(self, parameters):
        return self.post_request(entity='launchconfigurations', data=parameters)

    def update_lc(self, id, parameters):
        return self.put_request(entity='launchconfigurations', id=id, data=parameters)

    def delete_lc(self, id):
        return self.delete_request(entity='launchconfigurations', id=id)

    def create_domain(self, parameters):
        return self.post_request(entity='domains', data=parameters)

    def update_domain(self, id, parameters):
        return self.put_request(entity='domains', id=id, data=parameters)

    def delete_domain(self, id):
        return self.delete_request(entity='domains', id=id)