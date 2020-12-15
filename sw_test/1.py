import sys

sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    ms, ma = map(int, input().split())
    N, L = map(int, input().split())
    month = [list(map(int, input().split())) for _ in range(N)]
    st = ms + (ma * L)
    for i in range(L):
        my_stack = 0
        diff = []
        for j in range(N):
            tmp = month[j][i + 1] - month[j][i]
            diff.append([tmp, j])
        diff.sort(reverse=True)
        for value, idx in diff:
            if value <= 0:
                break
            price = month[idx][i]
            cnt = ms // price
            ms %= price
            my_stack += month[idx][i + 1] * cnt
        ms += ma
        ms += my_stack
    print('#{} {}'.format(t + 1, ms - st))
