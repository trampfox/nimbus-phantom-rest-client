__author__ = 'Davide Monfrecola'

import json
from phantomrestclient.phantomrequests import PhantomRequests

class LaunchConfigurations():

    def __init__(self):
        self.pr = PhantomRequests()

    def get_all(self):
        """Retrieve all the launch configuration available and create a new LauncConfiguration instance for each one

        :return: LauncConfiguration list that contains all the instances created
        """
        lcs = []
        lcs_json = json.loads(self.pr.get_all_launchconfigurations())

        for lc_json in lcs_json:
            lc = LaunchConfiguration()
            lc.load(lc_json)
            lcs.append(lc)

        return lcs

class LaunchConfiguration():

    def __init__(self):
        self.pr = PhantomRequests()
        self.name = None
        self.user_data = None
        self.cloud_params = None
        self.owner = None
        self.uri = None
        self.contextualization_method = None
        self.id = None


    def load(self, json=None):
        """

        """
        if json is None:
            raise Exception("Incorrect JSON data!")

        self.name = json['name']
        if 'user_data' in json:
            self.user_data = json['user_data']
        cps = CloudParams()
        self.cloud_params = cps.load(json['cloud_params'])
        self.owner = json['owner']
        self.uri = json['uri']
        if 'contextualization_method' in json:
            self.contextualization_method = json['contextualization_method']
        self.id = json['id']

class CloudParams():

    def __init__(self):
        self.cloud_params = []

    def load(self, json=None):
        if json is None:
            raise Exception("Incorrect JSON data!")

        for cloud_name, params in json.items():
            cp = CloudParam(cloud_name)
            cp.load(params)
            self.cloud_params.append(cp)

        return self.cloud_params

class CloudParam():

    def __init__(self, cloud_name):
        self.cloud_name = cloud_name
        self.image_id = None
        self.max_vms = None
        self.common = None
        self.rank = None
        self.instance_type = None

    def load(self, json=None):
        if json is None:
            raise Exception("Incorrect JSON data!")

        self.image_id = json['image_id']
        self.max_vms = json['max_vms']
        self.common = json['common']
        self.rank = json['rank']
        self.instance_type = json['instance_type']