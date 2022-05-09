import sys

sys.stdin = open('../../미해결/SW Expert/input.txt', 'r')


def go(check):
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            volume = li[i][0]
            value = li[i][1]
            if j < volume:
                check[i][j] = check[i - 1][j]
            else:
                check[i][j] = max(value + check[i - 1][j - volume], check[i - 1][j])
    return check[N][K]


T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    li = [[0, 0]]
    for i in range(N):
        li.append(list(map(int, input().split())))

    check = [[0] * (K + 1) for _ in range(N + 1)]
    ans = go(check)

    print('#{} {}'.format(t + 1, ans))
