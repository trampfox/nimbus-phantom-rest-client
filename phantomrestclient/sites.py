__author__ = 'Davide Monfrecola'

import json
from phantomrestclient.phantomrequests import PhantomRequests

class Sites():

    def __init__(self):
        self.pr = PhantomRequests()

    def get_all(self):
        """Retrieve all the sites and create a new Site instance for each one

        :return: Site list that contains all the instances created
        """
        sites = []
        sites_json = json.loads(self.pr.get_all_sites())

        for site_json in sites_json:
            site = Site()
            site.load(site_json)
            sites.append(site)

        return sites

class Site():

    def __init__(self):
        self.id = None
        self.credentials = None
        self.instance_types = None
        self.uri = None
        self.public_images = None
        self.user_images = None

    def load(self, json=None):
        if json is None:
            raise Exception("Incorrect JSON data!")

        self.id = json['id']
        self.credentials = json['credentials']
        self.instance_types = json['instance_types']
        self.uri = json['uri']
        if 'public_images' in json:
            self.public_images = json['public_images']
        if 'user_images' in json:
            self.user_images = json['user_images']
    # TODO add details fields management

class Credentials():

    def __init__(self):
        pass