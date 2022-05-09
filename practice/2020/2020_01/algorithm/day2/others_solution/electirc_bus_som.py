import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = 0
    nxt = K
    for j in range(M):
        if a[j] == nxt:
            nxt += K
            cnt += 1
        elif a[j] > nxt:
            if a[j - 1] + K < a[j]:
                cnt = 0
                break
            else:
                nxt = a[j - 1] + K
                cnt += 1

        if j == M - 1:
            if nxt < N:
                if (a[j] + K) >= N:
                    cnt += 1
                else:
                    cnt = 0
    print('#{} {}'.format(tc, cnt))