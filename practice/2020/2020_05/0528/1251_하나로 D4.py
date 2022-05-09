import sys
sys.stdin = open('input.txt')


def go(visited, cost):
    while 0 in visited:
        ans = float('inf')
        idx = -1
        for i in range(N):
            if not visited[i] and cost[i] < ans:
                ans = cost[i]
                idx = i
        visited[idx] = 1
        for j in range(N):
            if not visited[j]:
                cost[j] = min(cost[j], island[idx][j])
    return


T = int(input())

for t in range(T):
    N = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    island = [[0] * N for _ in range(N)]
    E = float(input())
    for i in range(N - 1):
        for j in range(i + 1, N):
            X = (x[i] - x[j]) ** 2
            Y = (y[i] - y[j]) ** 2
            d = X + Y
            island[i][j] = island[j][i] = d

    visited = [0] * N
    cost = [float('inf')] * N
    cost[0] = 0

    go(visited, cost)

    tmp = sum(cost) * E

    print('#{} {}'.format(t + 1, round(tmp)))
