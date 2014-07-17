__author__ = 'Davide Monfrecola'

import json
from phantomrestclient.phantomrequests import PhantomRequests

class Sensors():

    def __init__(self):
        self.pr = PhantomRequests()

    def get_all(self):
        """Retrieve all the sensors available and create a new Sensor instance for each one

        :return: Sensor list that contains all the instances created
        """
        sensors = []
        sensors_json = json.loads(self.pr.get_all_launchconfigurations())

        for sensor_json in sensors_json:
            s = Sensor()
            s.load(sensor_json)
            sensors.append(s)

        return sensors

class Sensor():

    def __init__(self):
        self.id = None
        self.uri = None

    def load(self, json=None):
        """

        """
        if json is None:
            raise Exception("Incorrect JSON data!")

        self.id = json['id']
        self.uri = json['uri']