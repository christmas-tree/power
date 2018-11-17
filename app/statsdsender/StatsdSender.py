import statsd


class StatsdSender:

    def __init__(self, host, port, prefix):
        self._statsdclient = statsd.StatsClient(host=host, port=port, prefix=prefix)

    def send_current(self, value):
        self._statsdclient.gauge('current', value)

    def send_voltage(self, value):
        self._statsdclient.gauge('voltage', value)

    def send_power(self, value):
        self._statsdclient.gauge('power', value)

    def send_reactive_power(self, value):
        self._statsdclient.gauge('reactive_power', value)

    def send_apparent_power(self, value):
        self._statsdclient.gauge('apparent_power', value)

    def send_power_factor(self, value):
        self._statsdclient.gauge('power_factor', value)

    def send_energy(self, value):
        self._statsdclient.gauge('energy', value)
