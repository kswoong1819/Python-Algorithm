TC = int(input())
for i in range(1, TC + 1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))

    li = []
    for j in range(N - M + 1):
        sum = 0
        for k in range(j, j + M):
            sum += a[k]
        li.append(sum)

    max = li[0]
    for x in range(1, len(li)):
        if max < li[x]:
            max = li[x]

    min = li[0]
    for x in range(1, len(li)):
        if min > li[x]:
            min = li[x]

    q = max - min

    print(f'#{i} {q}')