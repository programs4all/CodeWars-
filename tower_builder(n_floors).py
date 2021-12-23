import sys


def tower_builder(n_floors):
    # build here
    res = []
    for i in range(1, n_floors + 1):
        num = (i * 2) - 1
#       print(f'floors: {n_floors} | i: {i} | num: {num}')
        sen = ' ' * (n_floors - i) + "*" * num + ' ' * (n_floors - i)
        res.append(sen)
#   print(res)
    return res


def display_tower(n):
    lst = tower_builder(n)
    for i in lst:
        print(i)


# display_tower(5)
# print(sys.argv[0], sys.argv[1])


if __name__ == "__main__":
    display_tower(int(sys.argv[1]))
