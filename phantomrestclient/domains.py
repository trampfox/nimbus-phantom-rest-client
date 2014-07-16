__author__ = 'Davide Monfrecola'

import json
from phantomrequests import PhantomRequests

class Domains():

    def __init__(self):
        self.pr = PhantomRequests()

    def get_all(self):
        """Retrieve all the running domains and create a new Domain instance for each one

        :return: Domain list that contains all the instances created
        """
        domains = []
        domains_json = json.loads(self.pr.get_all_domains())

        for domain_json in domains_json:
            domain = Domain()
            domain.load(domain_json)
            domains.append(domain)

        return domains

class Domain():

    def __init__(self, json=None):
        self.pr = PhantomRequests()
        self.name = None
        self.scaling_policy = None
        self.monitor_domain_sensors = None
        self.launch_configuration = None
        self.monitor_sensors = None
        self.id = None
        self.vm_count = None

    def load(self, json=None):
        if json is None:
            raise Exception("Incorrect JSON data!")

        self.name = json['name']
        self.scaling_policy = json['de_name']
        self.monitor_domain_sensors = json['monitor_domain_sensors']
        self.launch_configuration = json['lc_name']
        self.monitor_sensors = json['monitor_sensors']
        self.id = json['id']
        self.vm_count = json['vm_count']