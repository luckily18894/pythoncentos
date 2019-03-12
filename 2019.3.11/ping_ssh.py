from ping_one import ping1
from paramiko_ssh import py_ssh


def ping_ssh(ipaddr, cname, passw, cmd='ls'):
    for a in ipaddr:
        if ping1(a) == '1':
            res = py_ssh(a, username=cname, password=passw, cmd=cmd)
            print(a+'可达！')
            print('登陆'+a+'执行命令'+cmd+'回显结果如下：')
            print(res)
        else:
            print(a+'不可达！')


if __name__ == '__main__':
    ipaddr = ['192.168.1.4', '192.168.1.6']
    cname = 'root'
    passw = 'luCKi1y'

    ping_ssh(ipaddr, cname, passw)

