import sys
sys.stdin = open('input.txt', 'r')

dr = [-1,-1,-1,0,1,1,1,0]
dc = [-1,0,1,1,1,0,-1,-1]

def init():
    matrix[N//2+1][N//2] = matrix[N//2][N//2+1] = 1
    matrix[N//2][N//2] = matrix[N//2+1][N//2+1] = 2

def change_color(r,c,color):
    matrix[r][c] = color

    for i in range(8):
        nr = r
        nc = c
        while 1:
            nr += dr[i]
            nc += dc[i]
            if nr <= 0 or nr > N or nc <= 0 or nc > N:
                break
            if matrix[nr][nc] == 0:
                break
            if matrix[nr][nc] == color:
                while not (nr == r and nc == c):
                    nr -= dr[i]
                    nc -= dc[i]
                    matrix[nr][nc] = color
                break

def count(n):
    count = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if matrix[i][j] == n:
                count += 1
    return count

T = int(input())

for t in range(T):
    N, M = map(int, input().split())

    matrix = [[0] * (N+1) for _ in range(N+1)]
    init()

    for i in range(M):
        c, r, color = map(int, input().split())
        change_color(r,c,color)

    count_B = count(1)
    count_W = count(2)

    print('#{} {} {}'.format(t+1, count_B, count_W))