import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())
heap = []
for i in range(N):
    x = int(input())
    heappush(heap, x)
    sort = sorted(heap)
    print(sort[i//2])