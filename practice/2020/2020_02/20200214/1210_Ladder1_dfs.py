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
        nr = r + dr[i]
        nc = c + dc[i]
        if nr < 0 or nr >= 100 or nc < 0 or nc >= 100:
            continue
        if ladder[nr][nc] == 1:
            ladder[nr][nc] = 2
            dfs(nr,nc)


for t in range(10):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    ans = -1

    for i in range(100):
        if ladder[99][i] == 2:
            sc = i
            break

    dfs(99,sc)
    print("#{} {}".format(T, ans))
