T = int(input())
count_N = [2,3,5,7,11]

for t in range(T):
    N = int(input())
    result = ''
    for i in count_N:
        count = 0
        while N % i == 0:
            count += 1
            N /= i
        result += str(count) + ' '
    print('#{} {}'.format(t+1, result))