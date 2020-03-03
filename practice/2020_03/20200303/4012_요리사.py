import sys

sys.stdin = open('input.txt')


def go(k, st):
    global min
    if k == N // 2:
        B = []
        for i in range(N):
            if check[i] == False:
                B.append(i)
        tmp = 0
        for x in range(N // 2):
            for y in range(x + 1, N // 2):
                tmp += S[A[x]][A[y]]
        tmp_2 = 0
        for x in range(N // 2):
            for y in range(x + 1, N // 2):
                tmp_2 += S[B[x]][B[y]]
        result = abs(tmp - tmp_2)
        if result < min:
            min = result
        return

    for i in range(st, N):
        if check[i]:
            continue
        check[i] = True
        A.append(i)
        go(k + 1, i + 1)
        A.pop()
        check[i] = False


T = int(input())

for t in range(T):
    N = int(input())
    S = []
    for s in range(N):
        S.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(i + 1, N):
            S[i][j] += S[j][i]

    min = 97654321
    check = [False] * N
    A = []
    go(0, 0)

    print('#{} {}'.format(t + 1, min))
