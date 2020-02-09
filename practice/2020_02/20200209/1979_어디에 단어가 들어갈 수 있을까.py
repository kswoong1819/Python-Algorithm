import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            if arr[i][j] == 0 or j == N-1:
                if cnt == K:
                    ans += 1
                cnt = 0

        for k in range(N):
            if arr[k][i] == 1:
                cnt += 1
            if arr[k][i] == 0 or k == N-1:
                if cnt == K:
                    ans += 1
                cnt = 0

    print('#{} {}'.format(t+1, ans))