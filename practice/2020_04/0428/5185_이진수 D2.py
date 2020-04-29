T = int(input())
for t in range(T):
    N, num = input().split()

    value = int(num, 16)
    num_2 = str(format(value, 'b'))
    zero = int(N)*4 - len(num_2)
    ans = '0' * zero + num_2
    print('#{} {}'.format(t+1, ans))