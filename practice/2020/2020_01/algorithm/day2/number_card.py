import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(T):
    N = int(input())
    arr = list(input())
    arr_count = [0]*10
    for a in arr:
        arr_count[int(a)] += 1

    find_max = 0
    idx = 0
    for i in range(9,0,-1):
        if find_max < arr_count[i]:
            find_max = arr_count[i]
            idx = i
    print('#{} {} {}'.format(t+1,idx, find_max))