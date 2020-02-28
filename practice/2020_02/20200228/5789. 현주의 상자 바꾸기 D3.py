T = int(input())

for t in range(T):
    N, Q = map(int, input().split())

    check = [0] * N
    for i in range(Q):
        st, ed = map(int, input().split())
        for j in range(st, ed+1):
            check[j-1] = i+1

    print('#{} {}'.format(t+1, ' '.join(map(str, check))))