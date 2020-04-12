import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    N, M, L = map(int, input().split())
    nums = list(map(int, input().split()))
    for i in range(M):
        idx_li = list(input().split())
        if idx_li[0] == 'I':
            nums.insert(int(idx_li[1]), int(idx_li[2]))
        if idx_li[0] == 'D':
            nums.pop(int(idx_li[1]))
        if idx_li[0] == 'C':
            nums[int(idx_li[1])] = idx_li[2]
    ans = '-1'
    if len(nums) >= L:
        ans = nums[L]
    print('#{} {}'.format(t+1, ans))