T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    for i in range(M-1):
        n_nums = list(map(int, input().split()))
        for j in range(len(nums)):
            if n_nums[0] < nums[j]:
                nums[j:j] = n_nums
                break
        else:
            nums.extend(n_nums)

    print('#{}'.format(t+1), end=' ')
    for i in range(-1, -11, -1):
        print(nums[i], end=' ')
    print()