# Intended for exercises!
card = '4000003972196502'
check_dig = [int(x) for x in card]
sum_dig = 0
last_dig = check_dig[-1]
if len(check_dig) != 16:
    status = 1
    print(status)
if check_dig[0] != 4:
    status = 1
    print(status)
check_dig.pop(-1)
for i in range(0, len(check_dig)):
    if i % 2 == 0:
        check_dig[i] *= 2
for i in range(0, len(check_dig)):
    if check_dig[i] > 9:
        check_dig[i] -= 9
for i in range(0, len(check_dig)):
    sum_dig += check_dig[i]
if ((sum_dig + last_dig) % 10) != 0:
    status = 1
    print(status)
