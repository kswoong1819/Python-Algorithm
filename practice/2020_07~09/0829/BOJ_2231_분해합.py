import sys

sys.stdin = open('input.txt')


def totalsum(num):
    total = 0
    while num != 0:
        total += num % 10
        num //= 10
    return total


N = int(input())
l = len(str(N))

result = 0
for i in range(l * 9, l * 1 - 1, -1):
    if N < i:
        continue
    num = N - i
    tmp = totalsum(num)
    if tmp == i:
        result = num
        break

print(result)
