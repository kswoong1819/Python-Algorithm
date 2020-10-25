import sys

sys.stdin = open('input.txt')

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(st):
    global fish_cnt, shark_size
    nq = deque()
    nq.append(st)
    result = 0
    eating = 0
    while nq:
        if fish_cnt == 0:
            return result
        st2 = nq.popleft()
        q = deque()
        q.append(st2)
        visited = [[0] * N for _ in range(N)]
        visited[st2[0]][st2[1]] = 1
        tmp_cnt = 500
        nxt_nr, nxt_nc = 100, 100
        while q:
            r, c, cnt = q.popleft()
            if cnt > tmp_cnt:
                continue
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                    if matrix[nr][nc] <= shark_size:
                        q.append([nr, nc, cnt + 1])
                        visited[nr][nc] = 1
                        if 0 < matrix[nr][nc] < shark_size:
                            tmp_cnt = min(tmp_cnt, cnt)
                            if nxt_nr > nr:
                                nxt_nr, nxt_nc = nr, nc
                            elif nxt_nr == nr:
                                nxt_nc = min(nxt_nc, nc)
        if tmp_cnt != 500:
            nq.append([nxt_nr, nxt_nc, 0])
            matrix[nxt_nr][nxt_nc] = 0
            result += tmp_cnt + 1
            eating += 1
            fish_cnt -= 1
            if eating == shark_size:
                eating = 0
                shark_size += 1

    return result


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
fish_cnt = 0
shark = []
shark_size = 2
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 9:
            shark = [i, j, 0]
            matrix[i][j] = 0
        elif matrix[i][j] != 0:
            fish_cnt += 1

print(bfs(shark))
