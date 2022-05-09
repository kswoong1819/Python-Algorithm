import sys
sys.stdin = open('input.txt')

def check_num(step, l, arr):
    total = 0
    for i in range(l):
        s = 0
        total += arr[i]
        for j in range(i, i+l):
            s += arr[j%l]
            if s <= ps:
                dp[step][s] += 1
            else:
                break
    if total <= ps:
        dp[step][total] = 1

ps = int(input())
m, n = map(int, input().split())
a_arr = [int(input()) for _ in range(m)]
b_arr = [int(input()) for _ in range(n)]

dp = [[0]*(ps+1) for _ in range(2)]

check_num(0, m, a_arr)
check_num(1, n, b_arr)


result = dp[0][ps] + dp[1][ps]
for i in range(1, ps):
    result += dp[0][i] * dp[1][ps-i]

print(result)
