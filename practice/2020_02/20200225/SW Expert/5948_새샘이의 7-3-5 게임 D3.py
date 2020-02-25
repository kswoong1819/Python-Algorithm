import sys
sys.stdin = open('input.txt', 'r')

def go(k, start):
    if k == 3:
        tmp = sum(A)
        if tmp not in sum_li:
            sum_li.append(sum(A))
    for i in range(start, 7):
        if check[i]:
            continue
        check[i] = True
        A.append(nums[i])
        go(k+1, i+1)
        A.pop()
        check[i] = False

T = int(input())

for t in range(T):
    nums = list(map(int, input().split()))

    sum_li = []
    A = []
    check = [False] * 7
    go(0, 0)
    sum_li.sort()
    print('#{} {}'.format(t+1, sum_li[-5]))