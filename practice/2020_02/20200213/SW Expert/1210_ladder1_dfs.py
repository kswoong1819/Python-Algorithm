import sys
sys.stdin = open('input.txt', 'r')

dr = [0,0,-1]
dc = [-1,1,0]

def dfs(r,c):
    global ans
    if ans != -1:
        return
    if r == 0:
        ans = c
        return
    for i in range(3):
        nr = r+dr[i]
        nc = c+dc[i]
        if nr < 0 or nr >=N or nc<0 or nc>=N:
            continue
        if ladder[nr][nc] == 1:
            ladder[nr][nc] = 2
            dfs(nr, nc)


for tc in range(10):
    tc_num = int(input())
    N = 100
    ladder = [list(map(int, input().split())) for _ in range(N)]
    ans = -1

    for i in range(N):
        if ladder[N-1][i] == 2:
            sC = i
            break

    dfs(N-1, sC)
    print("#{} {}".format(tc_num, ans))