import sys

sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N, M, K, A, B = map(int, input().split())
    ai = [0] + list(map(int, input().split()))
    bj = [0] + list(map(int, input().split()))
    k = list(map(int, input().split()))
    visited = [[0, 0, 0, 0] for _ in range(K + 1)]
    a_used = [0] * (N + 1)
    b_used = [0] * (M + 1)
    a_waiting = []
    b_waiting = []

    time = 0
    idx = 1
    endpoint = K
    result = 0
    while endpoint:
        while k:
            if k[0] == time:
                tmp = k.pop(0)
                a_waiting.append(idx)
                idx += 1
            else:
                break
        tmp = []
        for vi in range(1, K + 1):
            if visited[vi][0] > 0:
                visited[vi][0] -= 1
                if visited[vi][0] == 0:
                    tmp.append([visited[vi][2], vi])
                    a_used[visited[vi][2]] = 0
        tmp.sort()
        for t1, t2 in tmp:
            b_waiting.append(t2)
        for au in range(1, N + 1):
            if not len(a_waiting):
                break
            if a_used[au] == 0:
                a = a_waiting.pop(0)
                a_used[au] = 1
                visited[a][0] = ai[au]
                visited[a][2] = au

        for vi in range(1, K + 1):
            if visited[vi][1] > 0:
                visited[vi][1] -= 1
                if visited[vi][1] == 0:
                    b_used[visited[vi][3]] = 0
        for bu in range(1, M + 1):
            if not len(b_waiting):
                break
            if b_used[bu] == 0:
                b = b_waiting.pop(0)
                b_used[bu] = 1
                visited[b][1] = bj[bu]
                visited[b][3] = bu
                endpoint -= 1
                if visited[b][2:] == [A, B]:
                    result += b
        time += 1

    if result:
        print('#{} {}'.format(t + 1, result))
    else:
        print('#{} {}'.format(t + 1, -1))
