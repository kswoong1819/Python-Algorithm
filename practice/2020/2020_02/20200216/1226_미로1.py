dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dfs(r,c):
    global ans
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nc < 0 or nc >= N or nr < 0 or nr >= N:
            continue
        if maze[nr][nc] == 3:
            ans = 1
            return
        if maze[nr][nc] == 0:
            maze[nr][nc] = 1
            dfs(nr,nc)

for t in range(10):
    T = int(input())
    N = 16
    maze = [list(map(int, input())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sR = i
                sC = j

    dfs(sR, sC)

    print(ans)