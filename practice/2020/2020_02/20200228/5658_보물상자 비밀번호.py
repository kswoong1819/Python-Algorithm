import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    nums = input()
    p = N // 4

    num_set = set()
    for x in range(p):
        for i in range(0, N, p):
            num_set.add(int(nums[i:i + p], 16))
        tmp = nums[-1]
        nums = tmp + nums[:-1]

    num_li = list(num_set)
    num_li.sort()

    print('#{} {}'.format(t + 1, num_li[len(num_li) - K]))
