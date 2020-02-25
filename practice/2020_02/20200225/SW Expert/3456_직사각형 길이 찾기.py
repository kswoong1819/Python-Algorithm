T = int(input())

for t in range(T):
    nums = list(map(int, input().split()))

    total = 0
    ls = []
    for i in nums:
        total += i
        if i not in ls:
            ls.append(i)

    if len(ls) == 2:
        tmp = 2 * (ls[0] + ls[1])
    else:
        tmp = ls[0] * 4

    print('#{} {}'.format(t+1, tmp-total))