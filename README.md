# csgoterminalinfo

A simple Python program that displays information about a CS:GO server in the terminal.

This program currently runs in Linux and it probably won't work in Windows due to the way configuration files are currently handled, but I will most likely work on compatibility eventually.

## Dependencies

[python-a2s](https://github.com/Yepoleb/python-a2s)

## Configuration

The script searches for the file `config.ini` in `.config/csgoterminalinfo`.

Example configuration file:
```
[servers]

name = MyServer
address = play.myserver.com
port = 27015
```
## TODO
* write a better readme
* add colored text output
* add support for multiple servers
* add notifiers of user-specified players being online
  - This will, for example, allow a player to know if an admin is online so that they can avoid joining.
