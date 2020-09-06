import re
import subprocess
import sys

from core.log import Log

class Jails:

    def __init__(self, jails = [], debug = False):
        self._jails = jails
        self._debug = debug

    def get_jail_details(self):
        jails_status = []

        for jail in self._jails:
            exec_fail2ban = subprocess.check_output("fail2ban-client status "\
                                + jail,
                                shell=True,
                                stderr=subprocess.DEVNULL).decode('utf-8')

            jails_status.append(self.jail_ip_banned_list(exec_fail2ban))

        print(jails_status)

        return jails_status

    def generate_ip_banned_list(self, ip_banned_list):
        return [ip.split() for ip in ip_banned_list][0]

    def jail_ip_banned_list(self, jail_output):
        ip_banned_list = []

        ip_banned = re.search(r"Banned IP list:(.*\b)", jail_output, re.IGNORECASE | re.MULTILINE)

        if ip_banned:
            ip_banned_list.append(ip_banned.group(1).strip())

        if self._debug:
            print("Total banned count: {0}".format(ip_banned_list))

        return self.generate_ip_banned_list(ip_banned_list)
