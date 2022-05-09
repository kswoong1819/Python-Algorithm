import sys
input = sys.stdin.readline
from collections import deque

def bfs(st):
    q = deque()
    q.append(st)
    c = [0] * (N+1)
    c[st] = 1
    ans = 0
    while q:
        n = q.pop(0)
        ans += 1
        for i in arr[n]:
            if c[i] == 0:
                c[i] = 1
                q.append(i)
    return ans

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]

for i in range(M):
    x, y = map(int, input().split())
    arr[y].append(x)

count_list = []
max_cnt = 0
for i in range(1, N+1):
    if arr[i]:
        tmp = bfs(i)
        if max_cnt <= tmp:
            if max_cnt < tmp:
                count_list = []
            max_cnt = tmp
            count_list.append(i)

print(' '.join(map(str, count_list)))
