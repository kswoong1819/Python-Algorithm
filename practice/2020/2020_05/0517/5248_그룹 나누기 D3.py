def go(n, visited):
    visited[n] = 1
    for i in graph[n]:
        if visited[i] == 0:
            go(i, visited)


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    nums = list(map(int, input().split()))
    for i in range(0, M * 2, 2):
        graph[nums[i]].append(nums[i + 1])
        graph[nums[i + 1]].append(nums[i])

    cnt = 0
    visited = [0] * (N + 1)
    for i in range(1, N + 1):
        if visited[i]:
            continue
        cnt += 1
        go(i, visited)

    print('#{} {}'.format(t + 1, cnt))
