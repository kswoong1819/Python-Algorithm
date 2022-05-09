import sys

sys.stdin = open('input.txt')


def go(k, st):
    global ans
    if k == N // 2:
        x = y = 0
        for j in range(N):
            if check[j]:
                x += position[j][0]
                y += position[j][1]
            else:
                x -= position[j][0]
                y -= position[j][1]
        V = x ** 2 + y ** 2
        if ans > V:
            ans = V
        return
    for i in range(st, N):
        if check[i]:
            continue
        check[i] = True
        go(k + 1, i + 1)
        check[i] = False


T = int(input())
res = []
for t in range(T):
    N = int(input())
    position = []
    for i in range(N):
        x, y = map(int, input().split())
        position.append([x, y])
    V = 0
    ans = float('inf')
    check = [False] * N
    go(0, 0)
    res.append('#{} {}'.format(t + 1, ans))
print('\n'.join(res))
