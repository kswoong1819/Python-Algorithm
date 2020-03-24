import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

def parent_find(x):
    if gate[x] == x:
        return x
    gate[x] = parent_find(gate[x])
    return gate[x]


def union(x, y):
    x = parent_find(x)
    y = parent_find(y)
    gate[x] = y


G = int(input())
P = int(input())
plane = []
for _ in range(P):
    plane.append(int(input()))

gate = [i for i in range(G + 1)]
cnt = 0
for i in plane:
    re = parent_find(i)
    if re == 0:
        break
    union(re, re - 1)
    cnt += 1

print(cnt)
