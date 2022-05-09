import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    N, M, L = map(int, input().split())
    nums = list(map(int, input().split()))
    for i in range(M):
        idx, num = map(int, input().split())
        nums.insert(idx, num)
    print('#{} {}'.format(t+1, nums[L]))