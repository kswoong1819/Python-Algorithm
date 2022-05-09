import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))

    check = [0] * N
    for b in range(M):
        for a in range(N):
            if Ai[a] <= Bi[b]:
                check[a] += 1
                break

    ans = check.index(max(check)) + 1
    print('#{} {}'.format(t+1, ans))