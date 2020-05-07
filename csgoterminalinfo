#!/usr/bin/env python3

import a2s
import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.expanduser('~/.config/csgoterminalinfo/config.ini'))
address = (config['servers']['address'], int(config['servers']['port']))
#address = ("ttt.defyclan.com", 27015)
query = a2s.info(address)
#print(a2s.info(address).player_count)
if config.has_option('servers', 'name'):
    if not config['servers']['name']:
        servername = query.server_name
    else: 
        servername = config['servers']['name']
else:
        servername = query.server_name
print(f"{servername} currently has {query.player_count} players online and is on the map {query.map_name}.")
