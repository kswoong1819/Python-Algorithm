import sys
sys.stdin = open('input.txt', 'r')

def min_max(a):
    idx_max = 0
    for i in range(1, len(a)):
        if a[idx_max] < a[i]:
            idx_max = i
    a[idx_max] -= 1
    idx_min = 0
    for j in range(1, len(a)):
        if a[idx_min] > a[j]:
            idx_min = j
    a[idx_min] += 1
    return

for T in range(10):
    dum = int(input())
    arr = list(map(int, input().split()))
    for i in range(dum):
        min_max(arr)
    print('#{} {}'.format(T+1,max(arr)-min(arr)))