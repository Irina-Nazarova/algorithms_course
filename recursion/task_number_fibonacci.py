i = dict()


def fib_rec(num):
    """
    :param num: 3
    :return: 3
    """
    if num < 2:
        return 1
    if num in i.keys():
        return i[num]
    else:
        i[num] = fib_rec(num - 1) + fib_rec(num - 2)
        return i[num]
