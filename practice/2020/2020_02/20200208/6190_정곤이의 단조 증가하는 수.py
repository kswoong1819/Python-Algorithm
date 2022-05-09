import sys
sys.stdin = open('input.txt', 'r')

def check(num):
    n = str(num)
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            return -1
    return num

T = int(input())

for t in range(T):
    N = int(input())
    nums = list(map(int, input().split()))

    result = -1
    for i in range(N-1):
        for j in range(i+1, N):
            tmp = check(nums[i] * nums[j])
            if result < tmp:
                result = tmp
    print('#{} {}'.format(t+1, result))
