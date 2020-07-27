import itertools

flower_names = ['rose', 'tulip', 'sunflower']

for f in itertools.combinations(flower_names, 1):
    print(f)
for f2 in itertools.combinations(flower_names, 2):
    print(f2)
for f3 in itertools.combinations(flower_names, 3):
    print(f3)
