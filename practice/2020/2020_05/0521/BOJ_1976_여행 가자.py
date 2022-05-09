import sys

sys.stdin = open('input.txt')


def find(n):
    if check[n] == n:
        return n
    check[n] = find(check[n])
    return check[n]


def union(n1, n2):
    n1 = find(n1)
    n2 = find(n2)
    if ranks[n1] < ranks[n2]:
        n1, n2 = n2, n1
    check[n2] = n1
    if ranks[n1] == ranks[n2]:
        ranks[n1] += 1


N = int(input())
M = int(input())
connect = [list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))
ranks = [1] * (N + 1)
check = [i for i in range(N + 1)]

for i in range(N):
    for j in range(N):
        if connect[i][j] == 1:
            union(i, j)

result = set([check[i - 1] for i in plan])
if len(result) == 1:
    print('YES')
else:
    print('NO')
