T = int(input())

for t in range(T):
    N, R = map(int, input().split())

    first = 1
    second = 1
    for i in range(N):
        first *= N
        N -= 1
    for i in range(R):
        second *= R
        R -= 1

    ans = round(first/second) % 1234567891
    print('#{} {}'.format(t+1, ans))