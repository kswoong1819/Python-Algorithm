import sys
sys.stdin = open('input.txt')
from collections import deque


def bfs(st):



T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    time = [[0] * N for _ in range(N)]
    for n in range(N-1):
        nums = list(map(int, input().split()))
        for i in range(N-1-n):
            time[n][i+n+1] = nums[i]
            time[i+n+1][n] = nums[i]
    point = []
    airport = 0
    for n in range(N):
        place = list(input().split())
        if place == 'A':
            airport = n
        point.append(place)

    visited = [0] * N
    visited[airport] = 1
    bfs(airport)