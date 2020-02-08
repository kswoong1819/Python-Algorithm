import sys
sys.stdin = open('../list_2/input.txt', 'r')

for t in range(10):
    N = int(input())
    arr = list(map(int, input().split()))

    arr_5 = [[arr[i] for i in range(j, j+5)] for j in range(N-4)]

    result = 0
    for i in range(len(arr_5)):
        if max(arr_5[i]) == arr_5[i][2]:
            arr_5[i].sort()
            result += arr_5[i][-1] - arr_5[i][-2]
    print('#{}'.format(t+1))
    print(result)