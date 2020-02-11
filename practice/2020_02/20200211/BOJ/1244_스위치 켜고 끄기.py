import sys
sys.stdin = open('input.txt', 'r')

switch_N = int(input())
status = list(map(int, input().split()))
stu_N = int(input())

for i in range(stu_N):
    S, N = map(int, input().split())
    n = N-1

    if S == 1:
        for i in range(n, switch_N, N):
            if status[i] == 0:
                status[i] = 1
            else:
                status[i] = 0
    if S == 2:
        for x in range(switch_N//2):
            if n-x < 0 or n+x >= switch_N:
                break
            if status[n-x] == status[n+x]:
                if status[n-x] == 0:
                    status[n-x] = status[n+x] = 1
                else:
                    status[n - x] = status[n + x] = 0
            else:
                break

for i in range(1, switch_N+1):
    print(status[i-1], end=' ')
    if i % 20 == 0:
        print()