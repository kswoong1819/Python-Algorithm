import sys
sys.stdin = open('input.txt')
from collections import deque

dr = [0,1,0,-1]
dc = [1,0,-1,0]




def find(ch):
    cctv = deque()
    cctv.append(ch)
    while cctv:
        r, c, num = cctv.popleft()
        if num == 1:
            




N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

cnt_zero = 0
camera = []
for i in range(N):
    for j in range(M):
        if office[i][j] == 0:
            cnt_zero += 1
        if office[i][j] != 0 and office[i][j] != 6:
            camera.append([i, j, office[i][j]])

find(camera)