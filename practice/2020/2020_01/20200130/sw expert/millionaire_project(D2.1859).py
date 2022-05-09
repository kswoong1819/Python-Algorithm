import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    if max(arr) == arr[0]:
        print('0')
    else:
        i = 0
        while index(max(arr)) == i:
            result += arr[i]
            i += 1
            