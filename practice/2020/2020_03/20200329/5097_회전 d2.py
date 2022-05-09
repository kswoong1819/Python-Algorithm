T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    for i in range(M):
        nums.append(nums.pop(0))

    print('#{} {}'.format(t+1, nums[0]))