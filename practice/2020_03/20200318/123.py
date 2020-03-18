import sys

sys.stdin = open('input.txt')


def find_line(X):
    N = 1
    ls = [1]
    while X >= ls[-1]:
        tmp = ls[N - 1] + N
        ls.append(tmp)
        N += 1
    return [ls[-2], N - 2]


T = int(input())
res = []
for t in range(T):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a

    st_idx = find_line(a)
    ed_idx = find_line(b)

    st = (st_idx[1], a - st_idx[0])
    ed = (ed_idx[1], b - ed_idx[0])

    ans = 0
    gap = ed[0] - st[0]
    if gap != 0:
        if st[1]+gap < ed[1]:
            ans += ed[1]-(st[1]+gap)
        elif st[1] > ed[1]:
            ans += st[1] - ed[1]

    res.append('#{} {}'.format(t+1, ans+gap))
print('\n'.join(res))