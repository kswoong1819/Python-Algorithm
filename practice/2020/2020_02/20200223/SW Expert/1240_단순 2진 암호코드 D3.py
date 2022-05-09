import sys
sys.stdin = open('input.txt', 'r')

def point():
    for i in range(N):
        for j in range(M):
            if arr[i][-j - 1] == '1':
                return i, M - j

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    cord = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}

    I, J = point()
    tmp = arr[I][J-7*8:J]

    nums = []
    for i in range(0, 56, 7):
        change = ''
        for j in range(i, i+7):
            change += tmp[j]
        nums.append(cord[change])

    odd = 0
    even = 0
    for i in range(8):
        if i % 2:
            even += nums[i]
        else:
            odd += nums[i]
    result = odd * 3 + even

    if result % 10:
        print('#{} 0'.format(t+1))
    else:
        print('#{} {}'.format(t+1, sum(nums)))
