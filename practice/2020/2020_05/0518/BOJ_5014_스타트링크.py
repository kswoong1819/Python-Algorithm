import sys

sys.stdin = open('input.txt')
from collections import deque

F, S, G, U, D = map(int, input().split())

visited = [0] * (F + 1)
visited[S] = 1
flag = False
q = deque([[S, 0]])
while q:
    floor, cnt = q.popleft()
    if floor == G:
        flag = True
        print(cnt)
        break
    if 0 < floor + U <= F and visited[floor + U] == 0:
        visited[floor + U] = 1
        q.append([floor + U, cnt + 1])
    if 0 < floor - D <= F and visited[floor - D] == 0:
        visited[floor - D] = 1
        q.append([floor - D, cnt + 1])

if flag == False:
    print('use the stairs')
