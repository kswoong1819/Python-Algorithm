import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T):
    nums = list(map(int, input().split()))

    nums.sort()
    result = round(sum(nums[1:9])/8)

    print('#{} {}'.format(t+1, result))