import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def find(n):
    if parent[n] == n:
        return n
    parent[n] = find(parent[n])
    return parent[n]


def union(n1, n2):
    n1 = find(n1)
    n2 = find(n2)
    if n1 == n2:
        return
    if ranks[n1] < ranks[n2]:
        n1, n2 = n2, n1
    parent[n2] = n1
    if ranks[n1] == ranks[n2]:
        ranks[n1] += 1


n, m = map(int, input().split())
ranks = [0] * (n + 1)
parent = [i for i in range(n + 1)]
for _ in range(m):
    n, a, b = map(int, input().split())
    if n == 0:
        union(a, b)
    if n == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
