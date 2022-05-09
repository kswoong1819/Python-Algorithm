from heapq import heappush, heappop


def find(n):
    if check[n] == n:
        return n
    check[n] = find(check[n])
    return check[n]


def merge(n1, n2):
    n1 = find(n1)
    n2 = find(n2)
    if ranks[n1] < ranks[n2]:
        n1, n2 = n2, n1
    check[n2] = n1
    if ranks[n1] == ranks[n2]:
        ranks[n1] += 1


T = int(input())

for t in range(T):
    V, E = map(int, input().split())
    ranks = [1] * (1 + V)
    lines = []
    check = [i for i in range(V + 1)]
    for e in range(E):
        n1, n2, w = map(int, input().split())
        heappush(lines, (w, n1, n2))

    ans = 0
    while lines:
        w, n1, n2 = heappop(lines)
        if find(n1) != find(n2):
            merge(n1, n2)
            ans += w

    print('#{} {}'.format(t + 1, ans))
