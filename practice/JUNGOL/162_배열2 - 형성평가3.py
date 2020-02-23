N, M = map(int, input().split())

nums = [N, M]
for i in range(2, 10):
    tmp = (nums[i-2] + nums[i-1]) % 10
    nums.append(tmp)

for i in range(10):
    print(nums[i], end=' ')