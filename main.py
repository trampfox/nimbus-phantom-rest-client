__author__ = 'Davide Monfrecola'

from phantomrestclient import auth
from phantomrestclient import launchconfigurations
from phantomrestclient import domains
from phantomrestclient import phantomrequests

# only for testing purpouse
if __name__ == "__main__":
    #d = domains.Domains()
    #d.get_all()
    lc = launchconfigurations.LaunchConfigurations()
    lc.get_all()