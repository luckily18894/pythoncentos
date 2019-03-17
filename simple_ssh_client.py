
from argparse import ArgumentParser
from paramiko_ssh import py_ssh

if __name__ == '__main__':

    usage = "usage:python Simple_SSH_Client -i ipaddr -u username -p password -c command"

    parser = ArgumentParser(usage=usage)
    # parser.add_argument('-h ', '--help', dest=helps, help='show this help message and exit')
    parser.add_argument('-i ', '--ipaddr ', dest='ip', help='SSH server')
    parser.add_argument('-u ', '--username ', dest='username', help='SSH username')
    parser.add_argument('-p ', '--password ', dest='password', help='SSH password')
    parser.add_argument('-c ', '--command ', dest='cmd', help='shell command')

    args = parser.parse_args()

    print(py_ssh(args.ip, args.username, args.password, cmd=args.cmd))

