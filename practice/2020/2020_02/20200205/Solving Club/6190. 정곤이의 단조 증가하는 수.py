import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    result_list = []

    for i in range(N-1):
        for z in range(i+1, N-1):
            check = str(A[i] * A[z])
            for j in range(len(check)-1):
                if int(check[j]) > int(check[j+1]):
                    break
            else:
                result_list.append(int(check))
    print(result_list)

    result = 0
    for x in result_list:
        if result < x:
            result = x

    if result == 0:
        print('#{} -1'.format(t+1))
    else:
        print('#{} {}'.format(t+1,result))