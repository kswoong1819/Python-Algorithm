T = int(input())

for t in range(T):
    N = int(input())
    score = list(map(int, input().split()))
    visited = [0] * (N * 100 + 1)
    visited[0] = 1

    tmp = 0
    for i in range(N):
        tmp += score[i]
        for j in range(tmp, -1, -1):
            if visited[j]:
                visited[j + score[i]] = 1

    print('#{} {}'.format(t + 1, sum(visited)))
