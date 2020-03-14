T = int(input())

for t in range(T):
    N = int(input())
    nums = []
    while len(nums) < N:
        nums += input().split()

    nums = ''.join(nums)

    for i in range(0, 1000):
        if str(i) not in nums:
            print('#{} {}'.format(t+1, i))
            break