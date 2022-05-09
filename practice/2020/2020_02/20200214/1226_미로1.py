import sys
sys.stdin = open('input.txt', 'r')

dr = [0,0,-1,1]
dc = [-1,1,0,0]

def dfs():
    visited = [[0]*16 for _ in range(16)]
    visited[1][1] = 2
    stack = list()
    stack.append((1,1))
    while len(stack) > 0:
        r,c = stack.pop()
        visited[r][c] = 2
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 1 <= nc < len(arr) and 0 <= nr < len(arr) and visited[nr][nc] == 0:
                if arr[nr][nc] == 0:
                    stack.append((nr,nc))
                elif arr[nr][nc] == 3:
                    return 1
    return 0

for t in range(10):
    T = int(input())
    arr = [[int(i) for i in input()] for _ in range(16)]

    print('#{} {}'.format(T, dfs()))