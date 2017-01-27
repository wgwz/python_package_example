import requests
from my_package.mysecondmodule.utils import connection_to


maps = connection_to + 'maapps'

class Send(object):

    def __init__(self):
        self.resp = None

    def ping(self):

        self.resp = requests.get("http://google.com")

        if self.resp.status_code == 200:
            return "success"

        return "failure"