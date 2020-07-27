from itertools import count, product
from string import ascii_lowercase, digits
from socket import socket
from sys import argv


class Hacking:
    def __init__(self):
        self.pass_list = []

    @staticmethod
    def permute(inp):
        n = len(inp)

        # Number of permutations is 2^n
        mx = 1 << n

        # Converting string to lower case
        inp = inp.lower()

        # Create a list
        full_comb = []

        # Using all subsequences and permuting them
        for _i in range(mx):
            # If j-th bit is set, we convert it to upper case
            combination = [k for k in inp]
            for j in range(n):
                if ((_i >> j) & 1) == 1:
                    combination[j] = inp[j].upper()
            temp = ""
            # Printing current combination
            for _i in combination:
                temp += _i
            full_comb.append(temp)

        return full_comb

    def get_cheat_list(self):
        path = 'C:\\users\\yagoa\\Downloads\\passwords.txt'
        with open(path, 'r', encoding='utf-8') as file:
            for _l in file:
                self.pass_list.append(_l.strip())

    def generate_password(self):
        self.get_cheat_list()
        full_list = []
        while True:
            for item in self.pass_list:
                for item2 in self.permute(item):
                    full_list.append(item2)
            return full_list

    def check_data(self):
        for i in self.generate_password():
            if i == 'qwerty':
                print(i)
                break


print(Hacking().check_data())