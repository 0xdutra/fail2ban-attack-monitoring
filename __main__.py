#!/usr/bin/env python3

from core.jail import Jails
from core.firewall import Firewall

def main():
    jails = ['sshd', 'vsftpd']

    jail_details = Jails(jails, debug=True).get_jail_details()

    firewall = Firewall()

    for jail in jail_details:
    	firewall.start_firewall(jail)
    
if __name__ == '__main__':
    main()
