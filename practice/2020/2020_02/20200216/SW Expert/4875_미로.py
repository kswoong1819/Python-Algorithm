import sys
sys.stdin = open('input.txt', 'r')

dr = [0,0,1,-1]
dc = [1,-1,0,0]

def dfs(r,c):
    global ans
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= N or nc < 0 or nc >= N or maze[nr][nc] == 1:
            continue
        if maze[nr][nc] == 3:
            ans = 1
            return
        if maze[nr][nc] == 0:
            maze[nr][nc] = 1
            dfs(nr,nc)

for t in range(10):
    T = int(input())
    N = 100
    maze = [list(map(int, input())) for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sr = i
                sc = j
                break
    dfs(sr,sc)
    print(ans)