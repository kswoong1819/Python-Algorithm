def short_path():
    key = [float('inf')] * (N + 1)
    visited = [False] * (N + 1)
    check = set()
    check.add(0)
    key[0] = 0
    while True:
        min_key = float('inf')
        s = -1
        for i in check:
            if key[i] < min_key:
                min_key = key[i]
                s = i

        visited[s] = True
        check.remove(s)
        if s == N:
            return key[s]

        for e, w in link[s]:
            if key[e] > key[s] + w and not visited[e]:
                key[e] = key[s] + w
                check.add(e)


T = int(input())
for test_case in range(1, 1 + T):
    N, E = map(int, input().split())
    link = {}
    for _ in range(E):
        s, e, w = map(int, input().split())
        if s not in link:
            link[s] = [(e, w)]
        else:
            link[s] += [(e, w)]
    print('#{} {}'.format(test_case, short_path()))
