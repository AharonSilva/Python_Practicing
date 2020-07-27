numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

doubled_numbers = map(lambda x: x * 2, numbers)
odd_numbers = filter(lambda x: x % 2, numbers)

print(f'{list(doubled_numbers)} \n{list(odd_numbers)}')