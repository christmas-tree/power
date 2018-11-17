from six.moves import configparser
import six

if six.PY2:
    ConfigParser = configparser.SafeConfigParser
else:
    ConfigParser = configparser.ConfigParser


class Config:

    def __init__(self):
        self._config = ConfigParser()
        self._config.read('app/config/default.ini')
        self._config.read('config/user.ini')

    def get_espurna_hostname(self):
        return self._config.get('ESPURNA', 'hostname')

    def get_espurna_api_key(self):
        return self._config.get('ESPURNA', 'api_key')

    def get_statd_hostname(self):
        return self._config.get('STATSD', 'hostname')

    def get_port(self):
        return int(self._config.get('STATSD', 'port'), 0)

    def get_prefix(self):
        return self._config.get('STATSD', 'prefix')
