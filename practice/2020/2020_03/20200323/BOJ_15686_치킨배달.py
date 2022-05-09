import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline


def find(ch):
    total = 0
    for r1, c1 in home:
        minans = 98765421
        for r2, c2 in ch:
            tmp = abs(r1 - r2) + abs(c1 - c2)
            minans = min(minans, tmp)
        total += minans
    return total


def choice_store(k, st):
    global result
    if k == M:
        tmp = find(A)
        result = min(result, tmp)
        return
    for i in range(st, num):
        if visited[i]:
            continue
        visited[i] = 1
        A.append(chicken[i])
        choice_store(k + 1, i + 1)
        A.pop()
        visited[i] = 0


N, M = map(int, input().split())
store = [list(map(int, input().split())) for _ in range(N)]

home = []
chicken = []
for i in range(N):
    for j in range(N):
        if store[i][j] == 1:
            home.append((i, j))
        elif store[i][j] == 2:
            chicken.append((i, j))

result = 987654321
num = len(chicken)
visited = [0] * num
A = []
choice_store(0, 0)

print(result)
