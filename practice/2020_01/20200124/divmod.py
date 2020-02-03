T = int(input())

for t in range(T):
    num_a, num_b = map(int, input().split(' '))
    result = divmod(num_a, num_b)
    print('#{} {} {}'.format(t+1, result[0], result[1]))