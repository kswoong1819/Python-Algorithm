import sys
sys.stdin = open('input2.txt', 'r')

dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1, 0, -1, -1]

def init():
    n = N // 2
    othello[n][n] = othello[n+1][n+1] = 2
    othello[n+1][n] = othello[n][n+1] = 1

def col_change(r,c,color):
    othello[r][c] = color

    for i in range(8):
        nr = r
        nc = c
        while 1:
            nr += dr[i]
            nc += dc[i]
            if nr <= 0 or nr > N or nc <= 0 or nc > N:
                break
            if othello[nr][nc] == 0:
                break
            if othello[nr][nc] == color:
                while not (nr == r and nc == c):
                    nr -= dr[i]
                    nc -= dc[i]
                    othello[nr][nc] = color
                break

def count(num):
    count = 0
    for i in range(N+1):
        for j in range(N+1):
            if othello[i][j] == num:
                count += 1
    return  count

T = int(input())

for t in range(T):
    N, M = map(int, input().split())

    othello = [[0] * (N+1) for _ in range(N+1)]
    init()

    for i in range(M):
        r, c, color = map(int, input().split())
        col_change(r,c,color)

    count_B = count(1)
    count_W = count(2)

    print('#{} {} {}'.format(t+1,count_B,count_W))