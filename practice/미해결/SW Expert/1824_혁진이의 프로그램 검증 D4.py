import sys
sys.stdin = open('../../2020_03/20200309/input.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def go(st, ed):
    r,c = st
    i = 0
    while 1:
        nr = r + dr[i]
        nc = c + dc[i]
        if sign[nr][nc] == '<':
            i = 2
        elif sign[nr][nc] == '>':
            i = 1
        elif sign[nr][nc] == '^':
            i = 3
        elif sign[nr][nc] == 'v':
            i = 0
        elif sign[nr][nc] == '_':
            if sign[nr][nc] == 0:
                i = 0
            else:
                i = 2
        elif sign[nr][nc] == '|':
            if sign[nr][nc] == 0:
                i = 1
            else:
                i = 3
        elif sign[nr][nc] == '?':
            i = (i+1)%4
        elif sign[nr][nc] == '.':
            continue
        elif sign[nr][nc] == '@':
            break
        elif sign[nr][nc] == '+':

        elif sign[nr][nc] == '-':




T = int(input())

for t in range(T):
    R, C = int(input())
    sign = [list(input()) for _ in range(R)]

    go((0,0), (R,C))