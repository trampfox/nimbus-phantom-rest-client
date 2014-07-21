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
        r = requests.get(("%s/%s/%s" % self.api_url, entity, id),
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
        return self.get_request("domains")

    def get_all_launchconfigurations(self):
        r = requests.get('https://phantom.nimbusproject.org/api/dev/launchconfigurations',
                         headers={'Authorization': 'Basic %s' % self.access_token})
        return r.text

    def get_all_sites(self, details=True):
        url = 'https://phantom.nimbusproject.org/api/dev/sites'

        if details is True:
            url + '?details=true'

        r = requests.get(url, headers={'Authorization': 'Basic %s' % self.access_token})
        return r.text

    def get_credentials(self, cloud_name):
        url = 'https://phantom.nimbusproject.org/api/dev/credentials/sites/' + cloud_name
        r = requests.get(url, headers={'Authorization': 'Basic %s' % self.access_token})
        return r.text

    def create_lc(self, parameters):
        response = self.post_request(entity="launchconfigurations", data=parameters)
        return response

    def update_lc(self, id, parameters):
        response = self.put_request(entity="launchconfigurations", id=id, data=parameters)
        return response

    def delete_lc(self, id):
        response = self.delete_request(entity="launchconfigurations", id=id)
        return response

    def create_domain(self, parameters):
        url = 'https://phantom.nimbusproject.org/api/dev/domains'
        headers = {'content-type': 'application/json', 'Authorization': 'Basic %s' % self.access_token}
        r = requests.post(url, data=json.dumps(parameters), headers=headers)

        if r.status_code == requests.codes.ok:
            return r.text
        else:
            r.raise_for_status()