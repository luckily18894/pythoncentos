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
        result = sr1(self.pkt, timeout=1, verbose=False)
        if result:
            print(self.ip, '可达！')
        else:
            print(self.ip, '不可达！')

    def ping(self):
        for i in range(5):
            result = sr1(self.pkt, timeout=1, verbose=False)
            if result:
                print('!', end='', flush=True)
            else:
                print('.', end='', flush=True)

    def __str__(self):
        if self.srcip:
            return '{0:srcip}  {1:dstip}  {2:size}'.format(self.srcip, self.ip, str(self.size))
        else:
            return '{0:dstip}  {1:size}'.format(self.ip, str(self.size))


class PINGPLUS(MYPING):
    def ping(self):
        for i in range(5):
            result = sr1(self.pkt, timeout=1, verbose=False)
            if result:
                print('+', end='', flush=True)
            else:
                print('?', end='', flush=True)
        print()


if __name__ == '__main__':
    ping = MYPING('192.168.1.5')
    ping.ping()


