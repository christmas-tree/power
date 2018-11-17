import requests


class Espurna:

    def __init__(self, host, api_key):
        self._hostname = host
        self._api_key = api_key

    def get_current(self):
        return int(requests.get("http://{}/api/current?apikey={}".format(self._hostname, self._api_key)).content)

    def get_voltage(self):
        return int(requests.get("http://{}/api/voltage?apikey={}".format(self._hostname, self._api_key)).content)

    def get_power(self):
        return int(requests.get("http://{}/api/power?apikey={}".format(self._hostname, self._api_key)).content)

    def get_reactive_power(self):
        return int(requests.get("http://{}/api/reactive?apikey={}".format(self._hostname, self._api_key)).content)

    def get_apparent_power(self):
        return int(requests.get("http://{}/api/apparent?apikey={}".format(self._hostname, self._api_key)).content)

    def get_power_factor(self):
        return float(requests.get("http://{}/api/factor?apikey={}".format(self._hostname, self._api_key)).content)

    def get_energy(self):
        return int(requests.get("http://{}/api/energy?apikey={}".format(self._hostname, self._api_key)).content)
