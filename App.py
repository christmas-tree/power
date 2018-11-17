import time
from app.statsdsender import StatsdSender
from app.config import Config
from app.espurna import Espurna

def main():

    _config = Config()
    _statsdsender = StatsdSender(host=_config.get_statd_hostname(), port=_config.get_port(), prefix=_config.get_prefix())
    _espurna = Espurna(host=_config.get_espurna_hostname(), api_key=_config.get_espurna_api_key())

    while True:
        _statsdsender.send_current(_espurna.get_current())
        _statsdsender.send_voltage(_espurna.get_voltage())
        _statsdsender.send_power(_espurna.get_power())
        _statsdsender.send_reactive_power(_espurna.get_reactive_power())
        _statsdsender.send_apparent_power(_espurna.get_apparent_power())
        _statsdsender.send_power_factor(_espurna.get_power_factor())
        _statsdsender.send_energy(_espurna.get_energy())
        time.sleep(5)


if __name__ == '__main__':
    main()
