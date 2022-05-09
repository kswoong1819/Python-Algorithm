def func(n):
    flag = None
    l = 0
    r = N - 1
    while l <= r:
        m = (l + r) // 2
        if n == A[m]:
            return True
        elif n < A[m]:
            r = m - 1
            check = 'left'
        elif n > A[m]:
            l = m + 1
            check = 'right'
        if flag == check:
            return False
        flag = check
    return False


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))

    cnt = 0
    for num in B:
        if func(num):
            cnt += 1

    print('#{} {}'.format(t + 1, cnt))
