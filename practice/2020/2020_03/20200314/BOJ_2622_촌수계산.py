import sys
sys.stdin = open('input.txt')


def bfs(st, ed, cnt):
    q = [(st, cnt)]
    visited = [st]
    while q:
        n, cnt = q.pop(0)
        if n == ed:
            return cnt
        if n not in visited:
            visited.append(n)
        for i in range(1, N + 1):
            if check[n][i] == 1 and i not in visited:
                q.append((i, cnt + 1))


N = int(input())
st, ed = map(int, input().split())
T = int(input())
check = [[0] * (N + 1) for _ in range(N + 1)]
for t in range(T):
    x, y = map(int, input().split())
    check[x][y] = check[y][x] = 1

tmp = bfs(st, ed, 0)
if tmp == None:
    print('-1')
else:
    print(tmp)
