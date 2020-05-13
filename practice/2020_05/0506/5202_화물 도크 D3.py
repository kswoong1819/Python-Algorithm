T = int(input())

for t in range(T):
    N = int(input())
    time = [list(map(int, input().split())) for _ in range(N)]

    time.sort(key=lambda e: e[1])

    result = [time[0]]
    for i in range(1, N):
        if result[-1][1] <= time[i][0]:
            result.append(time[i])

    print('#{} {}'.format(t + 1, len(result)))
