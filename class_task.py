import logging
logging.getLogger("kamene.runtime").setLevel(logging.ERROR)
from kamene.all import *
from kamene.layers.inet import IP, ICMP


class MYPING:
    def __init__(self, ip):
        self.ip = ip
        self.srcip = None
        self.size = 100
        self.pkt = IP(dst=self.ip, src=self.srcip) / ICMP() / (b'v' * self.size)

    def src(self, srcip):
        self.srcip = srcip
        self.pkt = IP(dst=self.ip, src=self.srcip) / ICMP() / (b'v' * self.size)

    def size(self, size):
        self.size = size
        self.pkt = IP(dst=self.ip, src=self.srcip) / ICMP() / (b'v' * self.size)

    def one(self):
        result = sr1(self.pkt, timeout=2, verbose=False)
        if result:
            print(self.ip, '可达！')
        else:
            print(self.ip, '不可达！')

    def ping(self):
        for a in range(5):
            res = sr1(self.pkt, timeout=2, verbose=False)
            if res:
                print('!', end='', flush=True)
            else:
                print('.', end='', flush=True)

    def __str__(self):
        if self.srcip:
            return 'srcip: {0}, dstip: {1}, size: {2}'.format(self.srcip, self.ip, self.size)
        else:
            return 'dstip: {0}, size: {1}'.format(self.ip, self.size)


class PINGPLUS(MYPING):
    def ping(self):
        for a in range(5):
            res = sr1(self.pkt, timeout=1, verbose=False)
            if res:
                print('+', end='', flush=True)
            else:
                print('?', end='', flush=True)
    print()


if __name__ == '__main__':
    # ping = MYPING('192.168.1.4')
    # print(ping)
    # ping.one()
    # ping.ping()
    # ping.size = 200
    # print(ping)
    # ping.src('10.10.10.10')
    # print(ping)
    # ping.ping()
    ping = PINGPLUS('192.168.1.4')
    print(ping)
    ping.ping()
    ping.src('10.10.101.1')
    print(ping)
    ping.ping()
