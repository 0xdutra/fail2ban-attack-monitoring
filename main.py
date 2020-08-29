import json
import core.config

from core.jail import Jails
from core.firewall import Firewall

def main():
    fail2ban_jails_config_object = core.config.load_config_file()
    fail2ban_jails_info = fail2ban_jails_config_object["FAIL2BAN_JAILS"]

    fail2ban_jails = fail2ban_jails_info["jails"].split(',')
    jail_details = Jails(fail2ban_jails).get_jail_details()

    firewall = Firewall(jail_details[0])
    firewall.start_firewall()

if __name__ == '__main__':
    main()
