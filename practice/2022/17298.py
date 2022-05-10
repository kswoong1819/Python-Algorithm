import sys
sys.stdin = open("input.txt")

''' 시간초과
n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
dp[-1] = -1

for i in range(n-2, -1, -1):
    for j in range(1, n-i):
        if arr[i] < arr[i+j]:
            dp[i] = arr[i+j]
            break
    if not dp[i]:
        dp[i] = -1

print(*dp)
'''

n = int(input())
arr = list(map(int, input().split()))

answer = [-1] * n
stack = []

stack.append(0)
for i in range(1, n):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i)

print(*answer)
