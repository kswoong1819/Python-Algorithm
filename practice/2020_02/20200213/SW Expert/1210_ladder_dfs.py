import sys
sys.stdin = open('input.txt', 'r')

dc = [-1,1]

def dir_ch(r, c):
    for i in range(2):
        nc = c + dc[i]
        if nc < 0 or nc >= 10:
            continue
        if ladder[r][nc] == 1:
            return i
    return 2

def dfs(visited, V):
    col = V
    for i in range(10):
        dir = dir_ch(i, col)
        if dir < 2:
            nc = col + dc[dir]
            if ladder[nc][i] == 1 and i not in visited:
                dfs(visited, i)


T = int(input())

for t in range(T):
    ladder = [list(map(int, input().split())) for _ in range(10)]

    for i in range(10):
        if ladder[0][i] == 1:
            dfs([i], i)