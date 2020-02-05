import sys

sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    num = list(map(int, input().split()))

    arr = []
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            result = num[i] * num[j]
            arr.append(result)

    res = []
    for i in arr:
        prev = 10
        while i > 0:
            aa = i % 10
            if aa > prev:
                break
            aaa += aa
            i = i // 10
            prev = aa


    if -1 in res:
        print('#{} {}'.format(tc, max(res)))
