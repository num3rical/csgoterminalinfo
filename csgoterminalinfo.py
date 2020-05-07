#!/usr/bin/env python3

import a2s
import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.expanduser('~/.config/csgoterminalinfo/config.ini'))
address = (config['servers']['address'], int(config['servers']['port']))

query = a2s.info(address)

if config.has_option('servers', 'name'):
    if not config['servers']['name']:
        servername = query.server_name
    else: 
        servername = config['servers']['name']
else:
        servername = query.server_name

print(f"{servername} currently has {query.player_count} players online and is on the map {query.map_name}.")
