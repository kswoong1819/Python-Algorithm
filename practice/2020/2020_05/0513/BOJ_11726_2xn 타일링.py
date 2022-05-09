import sys

sys.stdin = open('input.txt')

n = int(input())
memo = [0, 1, 2]
for i in range(3, n + 1):
    memo.append(memo[i - 2] + memo[i - 1])
print(memo[n] % 10007)
