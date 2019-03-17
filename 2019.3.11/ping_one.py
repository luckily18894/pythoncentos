
import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)  # 关闭不必要的报错
from kamene.all import *
from kamene.layers.inet import IP, ICMP

# ping_pkt = IP(dst='114.114.114.114')/ICMP()  # 制造一个Ping包
# ping_result = sr1(ping_pkt, timeout=2, verbose=False)  # Ping并且把返回结果复制给ping_result
# ping_result.show()  # 查看回显结果


def ping1(ipadd):
    ping_pkt = IP(dst=ipadd) / ICMP()
    ping_result = sr1(ping_pkt, timeout=2, verbose=False)
    # print(ping_result)
    if ping_result:
        r = '1'
    else:
        r = '0'
    return r


if __name__ == '__main__':
    print(ping1('114.114.114.114'))


