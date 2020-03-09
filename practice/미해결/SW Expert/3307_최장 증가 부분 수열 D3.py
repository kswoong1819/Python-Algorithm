import sys

sys.stdin = open('input.txt')

def go(st, cnt):
    global ans
    if ans < cnt:
        ans = cnt
    for i in range(st, N):
        for j in range(i+1, N):
            if arr[i] < arr[j]:
                go(j, cnt + 1)


T = int(input())

for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    visited = [0] * N

    ans = 0
    go(0, 1)

    print('#{} {}'.format(t+1, ans))
