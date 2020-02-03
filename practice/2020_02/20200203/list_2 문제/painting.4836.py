import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for t in range(T):
    N = int(input())
    count = 0
    matrix = [[0 for _ in range(10)] for _ in range(10)]
    for n in range(N):
        arr_num = list(map(int, input().split()))
        for x in range(arr_num[0], arr_num[2]+1):
            for y in range(arr_num[1], arr_num[3]+1):
                matrix[x][y] += 1
    for i in matrix:
        for j in i:
            if j == 2:
                count += 1
    print('#{} {}'.format(t+1, count))