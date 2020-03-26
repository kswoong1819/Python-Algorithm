sys.stdin = open('input.txt')
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coin = [int(input()) for i in range(n)]

result = [0] * (k + 1)
result[0] = 1
for i in coin:
    for j in range(i, k + 1):
        result[j] += result[j - i]

print(result[k])
