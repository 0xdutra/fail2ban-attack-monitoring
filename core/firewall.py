import requests
import sys
import core.config

from core.database import Database
from core.geohash import GeoHash

class Firewall():
    def __init__(self, ips_list = []):
        self._ip_list = ips_list
        self._db = Database()

        ipinfo_config_object = core.config.load_config_file()
        ipinfo = ipinfo_config_object["IPINFO"]

        self.ipinfo_host = ipinfo["host"]

    def _get_ip_localization(self, ip):
        request = requests.get(f"{self.ipinfo_host}/{ip}")

        if request.status_code != 200:
            sys.exit(1)

        try:
            country = request.json()['country']
            loc = request.json()['loc']
        except Exception as e:
            print("Exception: ".format(e))
            sys.exit(1)

        return country, loc

    def _ban_ip_address(self, ip, country):
        pass

    def start_firewall(self):
        for ip in self._ip_list:
            country, loc = self._get_ip_localization(ip)
            geohash = GeoHash.generate_geohash(loc)

            if country != 'BR':
                self._db.send_data_to_influxdb(ip, country, loc, geohash)
