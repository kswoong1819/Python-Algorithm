def go(k, cur):
    if visited[k][cur]:
        return
    visited[k][cur] = 1
    if k == N:
        return
    go(k + 1, cur + score[k])
    go(k + 1, cur)


T = int(input())

for t in range(T):
    N = int(input())
    score = list(map(int, input().split()))
    visited = [[0] * (N * 100 + 1) for _ in range(N + 1)]

    go(0, 0)

    print('#{} {}'.format(t + 1, sum(visited[N])))
