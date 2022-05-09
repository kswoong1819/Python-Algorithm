import sys

sys.stdin = open('input.txt')


def go(j, cur):
    global max_ans
    if cur == 0 or max_ans >= cur:
        return
    if j == N:
        if max_ans < cur:
            max_ans = cur
        return
    for i in range(N):
        if check[i]:
            continue
        check[i] = True
        go(j + 1, cur * staff[j][i]/100)
        check[i] = False


T = int(input())

for t in range(T):
    N = int(input())
    staff = []
    for i in range(N):
        staff.append(list(map(int, input().split())))

    check = [False] * N
    max_ans = 0
    go(0, 100)
    print('#{} {:.6f}'.format(t+1, max_ans))