def fibonacci(n):
    list_old = [int(x) for x in range(n)]

    list_new = [0, 1]

    for i in range(2, len(list_old)):
        list_new.append(list_new[i - 1] + list_new[i - 2])
    for i in range(len(list_old)):
        yield list_new[i]