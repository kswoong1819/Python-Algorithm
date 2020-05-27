from collections import deque
dx = [1,-1, 0, 0]
dy = [0, 0, -1, 1]
dr = [-2, -1, 1, 2, -2, -1, 1, 2]
dc = [-1, -2, -2, -1, 1, 2, 2, 1]

def bfs():

    q = deque()
    visited[0][0][0] = 1
    q.append((0,0,0))

    while q:
        r, c, z = q.popleft()

        if r == H-1 and c == W-1 :
            print(visited[r][c][z]-1)
            return False

        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if nr < 0 or nr >= H or nc < 0 or nc >= W:
                continue
            if arr[nr][nc] == 0 and visited[nr][nc][z] == 0:
                visited[nr][nc][z] = visited[r][c][z]+1
                q.append((nr, nc, z))

        if z < K:
            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]
                if nr < 0 or nr >= H or nc < 0 or nc >= W :
                    continue
                if arr[nr][nc] == 0 and visited[nr][nc][z+1] == 0:
                    visited[nr][nc][z+1] = visited[r][c][z] + 1
                    q.append((nr, nc, z+1))
    return True

K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]

visited = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]

if bfs():
    print(-1)