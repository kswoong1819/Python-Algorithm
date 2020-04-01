import sys
sys.stdin = open('input.txt')

from heapq import heappush, heappop

V, E = map(int, input().split())
road = [] * (E+1)

