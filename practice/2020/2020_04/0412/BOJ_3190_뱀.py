import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def go(nhr, nhc, x, d, snake):
    global time, flag
    for i in range(x):
        time += 1
        nhr += dr[d]
        nhc += dc[d]
        if 0 >= nhr or nhr > N or 0 >= nhc or nhc > N:
            flag = True
            return 0, 0, []
        if [nhr, nhc] in snake:
            flag = True
            return 0, 0, []
        snake.append([nhr, nhc])
        if matrix[nhr][nhc] == 1:
            matrix[nhr][nhc] = 0
            continue
        if matrix[nhr][nhc] == 0:
            snake.popleft()
    return nhr, nhc, snake


N = int(input())
K = int(input())
matrix = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(K):
    x, y = map(int, input().split())
    matrix[x][y] = 1

L = int(input())
flag = False
time = 0
dir = 0
snake = deque()
snake.append([1, 1])
hr, hc = 1, 1
for _ in range(L):
    X, C = input().split()
    hr, hc, snake = go(hr, hc, int(X) - time, dir, snake)
    if flag:
        break
    if C == 'L':
        dir = (dir - 1) % 4
    if C == 'D':
        dir = (dir + 1) % 4
if flag == False:
    go(hr, hc, 100, dir, snake)

print(time)
