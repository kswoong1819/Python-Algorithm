import sys
sys.stdin = open('input.txt')

def go(k, cur):
    global min_ans
    if cur >= B:
        tmp = cur - B
        if min_ans > tmp:
            min_ans = tmp
    if k == N:
        return
    go(k+1, cur + S[k])
    go(k+1, cur)

T = int(input())

for t in range(T):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))

    min_ans = 987654321
    go(0,0)

    print('#{} {}'.format(t+1, min_ans))