import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    N = int(input())

    cnt = [0] * 5000
    for n in range(N):
        Ai, Bi = map(int, input().split())
        for i in range(Ai, Bi+1):
            cnt[i] += 1

    P = int(input())
    result = []
    for i in range(P):
        Cj = int(input())
        result.append(str(cnt[Cj]))

    print('#{} {}'.format(t+1, ' '.join(result)))