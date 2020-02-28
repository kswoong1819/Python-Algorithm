import sys

sys.stdin = open('../../2020_02/20200227/input.txt')

def lis(arr):
    if not arr:
        return 0

    ret = 1
    for i in range(len(arr)-ret):
        nxt = []
        for j in range(i + 1, len(arr)):
            if arr[i] < arr[j]:
                nxt.append(arr[j])
        ret = max(ret, 1 + lis(nxt))
    return ret


T = int(input())

for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))

    print('#{} {}'.format(t+1, lis(arr)))
