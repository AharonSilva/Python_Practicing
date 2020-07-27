prime_numbers = []

'''for n in prime_numbers:
    for i in range(2, n - 1):
        print(n % i == 0)
        '''

for val in range(1, 1001):
    if val > 1:
        for n in range(2, val//2 + 2):
            if (val % n) == 0:
                break
            else:
                if n == val//2 + 1:
                    prime_numbers.append(val)

print(prime_numbers)