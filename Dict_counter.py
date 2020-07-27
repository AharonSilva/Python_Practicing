entry = input()
entry = entry.split()
dic_comb = {}
new_dic = {}
counter = 0

for _x in entry:
    dic_comb[counter] = _x.lower()
    counter += 1

for _y in dic_comb.values():
    new_dic[_y] = 0

for x in dic_comb:
    if dic_comb[x] in new_dic.keys():
        new_dic[dic_comb[x]] += 1

for x in new_dic:
    print(f'{x} {new_dic[x]}')