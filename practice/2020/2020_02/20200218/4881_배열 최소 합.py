import sys

sys.stdin = open('input.txt', 'r')


def go(idx, n, j):
    global ansmin
    if sum(order) > ansmin:
        return
    if idx == n:
        print(order)
        if sum(order) < ansmin:
            ansmin = sum(order)
    for i in range(n):
        if check[i]:
            continue
        check[i] = True
        order.append(arr[j][i])
        go(idx + 1, n, j + 1)
        order.pop()
        check[i] = False

T = int(input())

for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    check = [False] * N
    order = []
    ansmin = 123123
    go(0, N, 0)
    print('#{} {}'.format(t+1,ansmin))
