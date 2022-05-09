import sys
sys.stdin = open('input.txt', 'r')


def game(x, y):
    if cards[x] == cards[y]:
        return x
    if cards[x] == 1:
        if cards[y] == 2:
            return y
        else:
            return x
    elif cards[x] == 2:
        if cards[y] == 1:
            return x
        else:
            return y
    elif cards[x] == 3:
        if cards[y] == 1:
            return y
        else:
            return x


def rec(st, ed):
    if st == ed:
        return st
    l = rec(st, (st + ed) // 2)
    r = rec((st + ed) // 2 + 1, ed)
    return game(l, r)


T = int(input())

for t in range(T):
    N = int(input())
    cards = list(map(int, input().split()))

    print('#{} {}'.format(t + 1, rec(0, N - 1) + 1))
