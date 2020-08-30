import sys

sys.stdin = open('input.txt')

N = int(input())
people = [list(map(int, input().split())) for _ in range(N)]
result = [1] * N

for i in range(N):
    x, y = people[i][0], people[i][1]
    for j in range(N):
        if i == j:
            continue
        a, b = people[j][0], people[j][1]
        if x < a and y <b:
            result[i] += 1

print(' '.join(map(str, result)))