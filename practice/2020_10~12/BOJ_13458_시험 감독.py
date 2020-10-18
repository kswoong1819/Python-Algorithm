import sys

sys.stdin = open('input.txt')

N = int(input())
Ai = list(map(int, input().split()))
B, C = map(int, input().split())

result = N
for i in range(N):
    n = Ai[i]
    if n >= B:
        n -= B
    else:
        n = 0
    result += n // C
    if n % C > 0:
        result += 1

print(result)
