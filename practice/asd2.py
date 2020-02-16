dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dfs(r,c):
    global ans
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nc < 0 or nc>=N or nr<0 or nr>=N :
            continue
        if maze[nr][nc] == 0 or maze[nr][nc] == 3:
            if maze[nr][nc] == 3:
                ans = 1
                return
            maze[nr][nc] = 1
            dfs(nr,nc)

for tc in range(1):
    tc_num = int(input())
    N = 16
    maze = [list(map(int, input())) for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sR = i
                sC = j

    print(dfs(sR, sC))
    print("#{} {}".format(tc_num, ans))