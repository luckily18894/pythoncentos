
import ipaddress
from ping_one import ping1

l1 = []
ipaddr = ipaddress.ip_network('192.168.1.0/29')
for ip in ipaddr:
    if ping1(str(ip)) == '1':
        l1.append(str(ip))


print(l1)



