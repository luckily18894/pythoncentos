#
import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)  # 关闭不必要的报错
from kamene.all import *
from kamene.layers.inet import IP, ICMP

ping_pkt = IP(dst='192.168.157.129')/ICMP()  # 制造一个Ping包
ping_result = sr1(ping_pkt, timeout=2, verbose=False)  # Ping并且把返回结果复制给ping_result
ping_result.show()
#
#
# from http.server import HTTPServer, CGIHTTPRequestHandler
# port = 80
# httpd = HTTPServer(('',port), CGIHTTPRequestHandler)
# print('Starting simple httpd on port: ' + str(httpd.server_port))
# httpd.serve_forever()


import paramiko
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.157.129', port=22, username='root', password='luCKi1y', timeout=5, compress=True)
stdin,stdout,stderr = ssh.exec_command('ls')
x = stdout.read().decode()
print(x)

