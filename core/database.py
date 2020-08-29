import sys
import core.config

from influxdb import InfluxDBClient


class Database():
    def __init__(self):

        database_config_object = core.config.load_config_file()
        database_info = database_config_object["INFLUXDB"]

        host = database_info["host"]
        port = database_info["port"]
        database = database_info["database"]

        self.measurement = database_info["measurement"]

        self._influxdb_client = InfluxDBClient(host=host,
                                               port=port,
                                               database=database)

    def check_value_exist_in_db(self, ip):
        q = f"select * from {self.measurement}"
        rs = self._influxdb_client.query(q)

        check = list(rs.get_points(tags={'ip': ip}))
        return check

    def send_data_to_influxdb(self, ip, country, localization, geohash):
        if not self.check_value_exist_in_db(ip):

            json_body = [
                {
                    "measurement": self.measurement,
                    "tags": {
                        "ip": ip
                    },
                    "fields": {
                        "country": country,
                        "localization": localization,
                        "geohash": geohash
                    }
                }
            ]

            try:
                self._influxdb_client.write_points(json_body)
            except Exception as error:
                print(error)
                sys.exit(1)
