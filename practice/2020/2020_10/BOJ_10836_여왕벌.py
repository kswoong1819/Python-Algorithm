import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

M, N = map(int, input().split())
matrix = [1] * (2 * M - 1)
for _ in range(N):
    grow = list(map(int, input().split()))
    i = 0
    for g in range(3):
        for k in range(grow[g]):
            matrix[i] += g
            i += 1

first = matrix[M - 1:]
second = matrix[M:]
print(' '.join(map(str, first)))
for i in range(M - 2, -1, -1):
    print(matrix[i], end=' ')
    print(' '.join(map(str, second)))
