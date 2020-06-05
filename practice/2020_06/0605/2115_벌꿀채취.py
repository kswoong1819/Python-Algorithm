import sys

sys.stdin = open('input.txt')


def collection(r, c):
    max_ans = 0
    value = []
    for i in range(M):
        value.append(honey[r][c])
        c += 1
    used = [0] * (M + 1)
    max1 = calcul(value, used, 0)
    for i in range(r, N):
        for j in range(N - M + 1):
            if i == r and j < c:
                continue
            value2 = []
            for k in range(M):
                value2.append(honey[i][j])
                j += 1
            used = [0] * (M + 1)
            max2 = calcul(value2, used, 0)
            if max_ans < max2:
                max_ans = max2
    max_ans += max1
    return max_ans


def calcul(nums, used, cur):
    if cur > C:
        return
    tmp = 0
    for k in range(M):
        if used[k]:
            tmp += nums[k] ** 2
    if used[M] < tmp:
        used[M] = tmp
    for i in range(M):
        if used[i]:
            continue
        used[i] = 1
        calcul(nums, used, cur + nums[i])
        used[i] = 0
    return used[M]


T = int(input())
for t in range(T):
    N, M, C = map(int, input().split())
    honey = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(N):
        for j in range(N - M + 1):
            tmp = collection(i, j)
            if result < tmp:
                result = tmp
    print('#{} {}'.format(t + 1, result))
