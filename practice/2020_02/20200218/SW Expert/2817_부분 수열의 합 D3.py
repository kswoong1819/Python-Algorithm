import sys
sys.stdin = open('input.txt', 'r')

'''
def go(k, n, start):
    global cnt
    if k == n:
        sum = 0
        for i in order:
            sum += i
        if sum == K:
            cnt += 1
    for i in range(start, N):
        if check[i]:
            continue
        check[i] = True
        order.append(nums[i])
        go(k+1, n+1, i)
        order.pop()
        check[i] = False


T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))

    check = [False] * N
    order = []
    cnt = 0

    go(0, 0, 0)

    print('#{} {}'.format(t+1,cnt))
'''


def go(k, cur):
    global cnt
    if cur > K:
        return
    if k == N:
        if cur == K:
            cnt += 1
    else:
        go(k+1, cur + nums[k])
        go(k+1, cur)

T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    cnt = 0

    go(0, 0)

    print('#{} {}'.format(t+1,cnt))
