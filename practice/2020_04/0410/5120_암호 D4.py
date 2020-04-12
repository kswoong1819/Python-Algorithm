T = int(input())

for t in range(T):
    N, M, K = map(int, input().split())
    nums = list(map(int, input().split()))

    ni = 0
    for i in range(K):
        ni += M
        if ni >= len(nums):
            ni -= len(nums)
        if ni == 0:
            nums.append(nums[ni-1]+nums[ni])
            ni -= 1
        else:
            nums.insert(ni, nums[ni-1]+nums[ni])

    print('#{}'.format(t+1), end=' ')
    i = 1
    while len(nums) >= i and 10 >= i:
        print(nums[-i], end=' ')
        i += 1
    print()