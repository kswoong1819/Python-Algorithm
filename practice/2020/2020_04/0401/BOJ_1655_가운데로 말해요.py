import sys
sys.stdin = open('../../2020_03/20200331/input.txt')

input = sys.stdin.readline
from heapq import heappush, heappop

N = int(input())
left, right = [], []
for i in range(N):
    x = int(input())
    if len(left) == len(right):
        heappush(left, (-x, x))
    else:
        heappush(right, (x, x))

    if right and left[0][1] > right[0][1]:
        left_value = heappop(left)[1]
        right_value = heappop(right)[1]
        heappush(right, (left_value, left_value))
        heappush(left, (-right_value, right_value))

    print(left[0][1])