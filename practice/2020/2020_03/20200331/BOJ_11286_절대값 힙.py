import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())
heap = []
for i in range(N):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heappop(heap)[1])
    else:
        heappush(heap, (abs(x), x))