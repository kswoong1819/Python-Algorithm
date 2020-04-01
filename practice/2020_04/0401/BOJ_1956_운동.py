import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline
from heapq import heappush, heappop

def bfs(st):
    dist = [float('inf')]


V, E = map(int, input().split())
road = [] * (E + 1)
for i in range(V + 1):
    a, b, c = map(int, input().split())
    road[a].append((b, c))

for i in range(V):
    bfs(i)