# Supercalc
Calculate the broadest single subnet which covers the provided IP addresses
## Usage
```
$ python supernet.py 192.168.1.1 192.168.4.5
# Output:
From IP: 192.168.1.1/32
To IP: 192.168.4.5/32
-------
Matching Supernet: 192.168.0.0/21
Host address: 192.168.0.0
Network address: 192.168.0.0
Broadcast address: 192.168.7.255
Netmask: 255.255.248.0
Number of hosts: 2048
Number of usable hosts: 2046
Usable range: 192.168.0.1 - 192.168.7.254
```
## Installation
There should be no dependencies, just run the script with Python 3.

## Todo
- [ ] Add support for IPv6
- [ ] Add support for common likely splits (e.g. It's likely that 192.168.1.1 and 192.168.10.20 will be two /24s instead of a single /16)
- [ ] Add support for suggesting common IPs within subnets for enumeration