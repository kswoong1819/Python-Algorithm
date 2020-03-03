import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    N = int(input())

    ans = 0
    for i in range(N):
        p, x = input().split()
        ans += float(p)*int(x)

    print('#{} {:.6f}'.format(t+1, ans))