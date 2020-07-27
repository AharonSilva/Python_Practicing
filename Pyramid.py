height = int(input())

list_1 = []

blank_list = []

for i in range(1, height + height):
    list_1.append(i * "#")

hashtag_list = [x for x in list_1 if len(x) % 2 != 0]

for i in reversed(range(height)):
    blank_list.append(i * " ")

for i in range(height):
    print(blank_list[i] + hashtag_list[i])
