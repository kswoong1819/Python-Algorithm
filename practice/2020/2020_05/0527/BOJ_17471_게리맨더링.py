import sys

sys.stdin = open('input.txt')
from collections import deque


def bfs(area):
    q = deque()
    q.append(area[0])
    visited = [0] * N
    visited[area[0]] = 1
    cnt, ans = 1, 0
    while q:
        n = q.popleft()
        ans += people[n]
        for nxt in connect[n]:
            if nxt in area and not visited[nxt]:
                visited[nxt] = 1
                cnt += 1
                q.append(nxt)
    if cnt == len(area):
        return ans
    else:
        return 0


def dfs(cnt, st, end):
    global min_ans
    if cnt == end:
        area1 = deque()
        area2 = deque()
        for i in range(N):
            if check[i]:
                area1.append(i)
            else:
                area2.append(i)
        ans1 = bfs(area1)
        if not ans1:
            return
        ans2 = bfs(area2)
        if not ans2:
            return
        min_ans = min(min_ans, abs(ans2 - ans1))
        return

    for i in range(st, N):
        if check[i]:
            continue
        check[i] = 1
        dfs(cnt + 1, i, end)
        check[i] = 0


N = int(input())
people = list(map(int, input().split()))
connect = [[] for _ in range(N)]
for n in range(N):
    line = list(map(int, input().split()))
    for i in range(1, line[0] + 1):
        connect[n].append(line[i] - 1)

min_ans = float('inf')
for i in range(1, N // 2 + 1):
    check = [0] * N
    dfs(0, 0, i)

if min_ans == float('inf'):
    print('-1')
else:
    print(min_ans)
