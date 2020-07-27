import itertools
import string

message = string.digits + string.ascii_lowercase
password = []
count = 0
match = '0'


def password_gen():
    pattern = string.digits + string.ascii_lowercase
    n = []
    for i in range(1, 4):
        for combination in itertools.combinations(pattern, i):
            n.append(''.join(combination))
    yield n


for x in next(password_gen()):
    print(x)

